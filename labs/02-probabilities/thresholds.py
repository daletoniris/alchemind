"""
Lab 2: Working with Probabilities
===================================
Understand how threshold tuning affects security decisions.

Key insight: In security, missing an attack (FN) is worse than
a false alarm (FP). Tune your threshold accordingly.
"""

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score

# Reuse dataset from Lab 1
normal = [
    "GET /index.html HTTP/1.1",
    "GET /api/users?page=1 HTTP/1.1",
    "POST /api/login HTTP/1.1 user=admin&pass=secure",
    "GET /static/main.css HTTP/1.1",
    "GET /api/products HTTP/1.1",
    "POST /api/contact HTTP/1.1 name=John&msg=Hello",
    "GET /api/health HTTP/1.1",
    "GET /dashboard HTTP/1.1",
    "GET /api/search?q=python HTTP/1.1",
    "GET /about HTTP/1.1",
] * 80

attacks = [
    "GET /api/users?id=1' UNION SELECT * FROM users-- HTTP/1.1",
    "GET /search?q=<script>alert(1)</script> HTTP/1.1",
    "GET /../../etc/passwd HTTP/1.1",
    "POST /login HTTP/1.1 user=admin'-- HTTP/1.1",
    "GET /api?id=1 OR 1=1 HTTP/1.1",
    "POST /comment HTTP/1.1 <img src=x onerror=alert(1)>",
    "GET /api/file?path=../../../etc/shadow HTTP/1.1",
    "GET /search?q='; DROP TABLE users;-- HTTP/1.1",
    "POST /login HTTP/1.1 pass=' OR '1'='1 HTTP/1.1",
    "GET /exec?cmd=cat+/etc/passwd HTTP/1.1",
] * 20

X_raw = normal + attacks
y = np.array([0] * len(normal) + [1] * len(attacks))

X_train_raw, X_test_raw, y_train, y_test = train_test_split(
    X_raw, y, test_size=0.2, random_state=42, stratify=y
)

vectorizer = TfidfVectorizer(analyzer='char_wb', ngram_range=(3, 5), max_features=3000)
X_train = vectorizer.fit_transform(X_train_raw)
X_test = vectorizer.transform(X_test_raw)

model = LogisticRegression(class_weight='balanced', max_iter=1000, random_state=42)
model.fit(X_train, y_train)

# Get probabilities (not just predictions)
probabilities = model.predict_proba(X_test)[:, 1]  # P(attack)

# ============================================================
# TEST DIFFERENT THRESHOLDS
# ============================================================
print("=" * 70)
print("THRESHOLD ANALYSIS — How the cutoff changes everything")
print("=" * 70)

thresholds = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]

print(f"\n{'Threshold':>10} {'Precision':>10} {'Recall':>10} {'F1':>10} {'FP':>6} {'FN':>6} {'Verdict':>20}")
print("-" * 70)

for threshold in thresholds:
    y_pred = (probabilities >= threshold).astype(int)

    precision = precision_score(y_test, y_pred, zero_division=0)
    recall = recall_score(y_test, y_pred, zero_division=0)
    f1 = f1_score(y_test, y_pred, zero_division=0)

    fp = sum((y_pred == 1) & (y_test == 0))  # False alarms
    fn = sum((y_pred == 0) & (y_test == 1))  # Missed attacks

    if fn == 0:
        verdict = "Perfect recall"
    elif fn <= 2:
        verdict = "Acceptable"
    else:
        verdict = "DANGEROUS - attacks missed!"

    print(f"{threshold:>10.1f} {precision:>10.2f} {recall:>10.2f} {f1:>10.2f} {fp:>6d} {fn:>6d} {verdict:>20}")

print()
print("=" * 70)
print("KEY INSIGHT:")
print()
print("  Lower threshold (0.3-0.4):")
print("    + Catches more attacks (high recall)")
print("    - More false alarms (low precision)")
print("    = SAFER for security — prefer this")
print()
print("  Higher threshold (0.6-0.8):")
print("    + Fewer false alarms (high precision)")
print("    - Misses real attacks (low recall)")
print("    = DANGEROUS for security — avoid this")
print()
print("  In security: FN (missed attack) > FP (false alarm)")
print("  A false alarm wastes time. A missed attack causes a breach.")
print("=" * 70)
print()
print("Next: Lab 3 — Confusion Matrix Deep Dive")
