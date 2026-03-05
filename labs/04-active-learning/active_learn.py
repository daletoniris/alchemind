"""
Lab 4: Active Learning Pipeline
=================================
The secret weapon of The Warden: learn from what you don't know.

Active learning selects the samples the model is MOST confused about,
gets labels for them, and retrains. This maximizes learning per label.
"""

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, recall_score
from sklearn.model_selection import train_test_split

# ============================================================
# DATASET — Larger, with some tricky edge cases
# ============================================================
normal = [
    "GET /index.html HTTP/1.1",
    "GET /api/users?page=1 HTTP/1.1",
    "POST /api/login HTTP/1.1 user=admin&pass=secure",
    "GET /api/search?q=python+tutorial HTTP/1.1",
    "GET /api/products?cat=electronics HTTP/1.1",
    "POST /api/contact HTTP/1.1 msg=Hello+world",
    "GET /api/health HTTP/1.1",
    "GET /dashboard HTTP/1.1",
    "GET /about HTTP/1.1",
    "POST /api/feedback HTTP/1.1 rating=5",
] * 50

attacks = [
    "GET /api?id=1' UNION SELECT * FROM users-- HTTP/1.1",
    "GET /q=<script>alert(1)</script> HTTP/1.1",
    "GET /../../etc/passwd HTTP/1.1",
    "POST /login HTTP/1.1 user=admin'-- HTTP/1.1",
    "GET /api?id=1 OR 1=1 HTTP/1.1",
] * 20

# Edge cases — tricky samples that confuse simple models
edge_cases = [
    # Looks like attack but is normal (encoded URL params)
    "GET /api/search?q=what+is+1%3D1+in+SQL HTTP/1.1",  # normal (searching about SQL)
    "GET /api/search?q=how+to+select+from+dropdown HTTP/1.1",  # normal
    "POST /api/code HTTP/1.1 snippet=SELECT+*+FROM+table HTTP/1.1",  # normal (code sharing)
    # Looks normal but is attack (obfuscated)
    "GET /api/data?f=....//....//etc/passwd HTTP/1.1",  # attack (double encoding)
    "POST /api/search HTTP/1.1 q=%3Csvg%20onload%3Dalert(1)%3E",  # attack (encoded XSS)
    "GET /api/user?id=1%27%20AND%201%3D1-- HTTP/1.1",  # attack (encoded SQLi)
]
edge_labels = [0, 0, 0, 1, 1, 1]  # Ground truth

# Combine
X_raw = normal + attacks
y = np.array([0] * len(normal) + [1] * len(attacks))

# Hold out edge cases as "unlabeled pool" — simulating production data
X_pool_raw = edge_cases * 10  # 60 edge cases
y_pool_true = np.array(edge_labels * 10)  # True labels (unknown to model)

# Split main dataset
X_train_raw, X_test_raw, y_train, y_test = train_test_split(
    X_raw, y, test_size=0.2, random_state=42, stratify=y
)

# Include edge cases in test set for evaluation
X_test_raw = list(X_test_raw) + X_pool_raw
y_test = np.concatenate([y_test, y_pool_true])

print("=" * 60)
print("ACTIVE LEARNING — The Warden's Learning Loop")
print("=" * 60)

# ============================================================
# INITIAL MODEL (before active learning)
# ============================================================
vectorizer = TfidfVectorizer(analyzer='char_wb', ngram_range=(3, 5), max_features=3000)
X_train_vec = vectorizer.fit_transform(X_train_raw)
X_test_vec = vectorizer.transform(X_test_raw)

model = LogisticRegression(class_weight='balanced', max_iter=1000, random_state=42)
model.fit(X_train_vec, y_train)

initial_f1 = f1_score(y_test, model.predict(X_test_vec))
initial_recall = recall_score(y_test, model.predict(X_test_vec))

print(f"\nInitial model (trained on {len(X_train_raw)} samples):")
print(f"  F1 Score: {initial_f1:.4f}")
print(f"  Recall:   {initial_recall:.4f}")

# ============================================================
# ACTIVE LEARNING LOOP
# ============================================================
print(f"\n{'─' * 60}")
print("Starting Active Learning Loop...")
print(f"Unlabeled pool: {len(X_pool_raw)} samples")
print(f"{'─' * 60}")

# Copy training data (we'll expand it)
X_active_raw = list(X_train_raw)
y_active = list(y_train)

# Track metrics across rounds
metrics_history = []
batch_size = 10  # Label 10 samples per round
n_rounds = 5

for round_num in range(1, n_rounds + 1):
    # Step 1: Get predictions on unlabeled pool
    X_pool_vec = vectorizer.transform(X_pool_raw)
    probabilities = model.predict_proba(X_pool_vec)[:, 1]

    # Step 2: UNCERTAINTY SAMPLING — select most uncertain samples
    # Uncertainty = how close to 0.5 (maximum doubt)
    uncertainty = np.abs(0.5 - probabilities)

    # Select the most uncertain samples
    uncertain_indices = np.argsort(uncertainty)[:batch_size]

    # Step 3: "Label" them (in practice, a human or LLM does this)
    newly_labeled_X = [X_pool_raw[i] for i in uncertain_indices]
    newly_labeled_y = [y_pool_true[i] for i in uncertain_indices]

    # Show what was selected
    print(f"\nRound {round_num}: Selected {batch_size} most uncertain samples:")
    for i, idx in enumerate(uncertain_indices[:3]):  # Show first 3
        req = X_pool_raw[idx][:50]
        prob = probabilities[idx]
        true_label = "ATTACK" if y_pool_true[idx] == 1 else "NORMAL"
        print(f"  [{i+1}] P(attack)={prob:.3f} | True={true_label} | {req}...")

    # Step 4: Add to training set
    X_active_raw.extend(newly_labeled_X)
    y_active.extend(newly_labeled_y)

    # Step 5: Remove from pool
    remaining = [i for i in range(len(X_pool_raw)) if i not in uncertain_indices]
    X_pool_raw = [X_pool_raw[i] for i in remaining]
    y_pool_true = y_pool_true[remaining]

    # Step 6: RETRAIN
    vectorizer_new = TfidfVectorizer(analyzer='char_wb', ngram_range=(3, 5), max_features=3000)
    X_active_vec = vectorizer_new.fit_transform(X_active_raw)
    X_test_vec_new = vectorizer_new.transform(X_test_raw)

    model_new = LogisticRegression(class_weight='balanced', max_iter=1000, random_state=42)
    model_new.fit(X_active_vec, np.array(y_active))

    # Evaluate
    round_f1 = f1_score(y_test, model_new.predict(X_test_vec_new))
    round_recall = recall_score(y_test, model_new.predict(X_test_vec_new))

    metrics_history.append({
        'round': round_num,
        'samples_added': batch_size,
        'total_training': len(X_active_raw),
        'f1': round_f1,
        'recall': round_recall,
        'pool_remaining': len(X_pool_raw),
    })

    print(f"  After retrain: F1={round_f1:.4f} (was {initial_f1:.4f}), "
          f"Recall={round_recall:.4f}, Pool remaining: {len(X_pool_raw)}")

    # Update model and vectorizer for next round
    model = model_new
    vectorizer = vectorizer_new

# ============================================================
# RESULTS SUMMARY
# ============================================================
print(f"\n{'=' * 60}")
print("ACTIVE LEARNING RESULTS")
print(f"{'=' * 60}")
print(f"\n{'Round':>6} {'Added':>6} {'Total':>6} {'F1':>8} {'Recall':>8} {'Pool':>6}")
print(f"{'─' * 46}")
print(f"{'Init':>6} {'─':>6} {len(X_train_raw):>6} {initial_f1:>8.4f} {initial_recall:>8.4f} {len(edge_cases)*10:>6}")

for m in metrics_history:
    print(f"{m['round']:>6} {m['samples_added']:>6} {m['total_training']:>6} "
          f"{m['f1']:>8.4f} {m['recall']:>8.4f} {m['pool_remaining']:>6}")

final_f1 = metrics_history[-1]['f1']
improvement = ((final_f1 - initial_f1) / initial_f1) * 100

print(f"\nImprovement: {initial_f1:.4f} → {final_f1:.4f} ({improvement:+.1f}%)")
print(f"Labels used: {batch_size * n_rounds} (out of {len(edge_cases)*10} pool samples)")
print()
print("KEY INSIGHT:")
print("  Active learning improved the model by labeling ONLY the samples")
print("  the model was most confused about — not random samples.")
print("  This is The Warden's secret: learn where you're weakest.")
print()
print("  In production:")
print("  1. KNN classifies a request with LOW confidence (doubt)")
print("  2. LLM analyzes it and provides a label + explanation")
print("  3. Human confirms the LLM's label")
print("  4. Sample added to training set")
print("  5. Model retrained → better at similar requests next time")
print(f"\n{'=' * 60}")
