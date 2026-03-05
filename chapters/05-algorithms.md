# Chapter 5: Algorithms That Learn

## *KNN, K-Means, Logistic Regression, Naive Bayes — and when each one fails*

> *"Understanding why an algorithm fails is more valuable than knowing when it succeeds."*

---

## 5.1 K-Nearest Neighbors (KNN)

**The idea**: To classify a new sample, look at the K closest samples in the training set. Whatever class the majority belongs to, that's your prediction.

```
  New sample: ?

  ┌─────────────────────────┐
  │   ●  ●                  │
  │      ●   ▲              │
  │  ●      (?)  ▲   ▲     │
  │       ●    ▲            │
  │   ●          ▲    ▲    │
  └─────────────────────────┘

  K=3: 2 circles, 1 triangle → classify as ●
  K=5: 3 circles, 2 triangles → classify as ●
  K=7: 3 circles, 4 triangles → classify as ▲ ← different!
```

### When to Use KNN
- Small to medium datasets
- When you need interpretability ("it was classified as X because these 5 examples are similar")
- Initial baseline — always try KNN first

### When KNN Fails
- High-dimensional data (curse of dimensionality)
- Imbalanced classes (majority class always wins)
- Large datasets (slow — must compute distance to every point)

### In Security Context
```python
# WAF log classification with KNN
from sklearn.neighbors import KNeighborsClassifier

# Features: [request_len, special_chars, entropy, param_count]
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# For a new request, KNN finds the 5 most similar past requests
# and votes on whether it's normal or attack
prediction = knn.predict(new_request)
confidence = knn.predict_proba(new_request)

# LOW confidence → send to LLM for analysis (The Warden pattern)
if max(confidence[0]) < 0.7:
    explanation = ask_llm(f"Analyze this request: {request}")
```

---

## 5.2 K-Means Clustering

**The idea**: Group data into K clusters without labels. The algorithm discovers structure in unlabeled data.

```
Before K-Means:               After K-Means (K=3):

  ·  ·    ·  ·                  ●  ●    ▲  ▲
    ·   ·                         ●   ▲
  ·       ·    ·                ●       ▲    ▲
     ·  ·     ·    ·               ●  ●     ■    ■
       ·         ·                   ●         ■
                   ·  ·                          ■  ■
                  ·                              ■
```

### Algorithm
1. Pick K random centroids
2. Assign each point to the nearest centroid
3. Recalculate centroids as the mean of each cluster
4. Repeat until stable

### In Security Context
K-Means is perfect for **anomaly detection**:
- Cluster all network traffic
- New traffic that doesn't fit any cluster well → anomaly
- No labels needed — discovers attack patterns automatically

---

## 5.3 Logistic Regression

**The idea**: Despite the name, it's for **classification**, not regression. Uses the sigmoid function to output probabilities.

```
P(attack | features) = σ(w₁x₁ + w₂x₂ + ... + wₙxₙ + b)

Where σ(z) = 1 / (1 + e⁻ᶻ)

Output is always between 0 and 1 → probability of belonging to class 1
```

### Why It Matters
- **Fast** — trains in seconds
- **Interpretable** — each weight tells you feature importance
- **Probabilistic** — outputs confidence, not just class
- **Baseline** — if logistic regression works well, you might not need deep learning

### In Security Context
```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)

# Feature importance: which features matter most?
for feature, weight in zip(feature_names, model.coef_[0]):
    print(f"{feature}: {weight:+.3f}")

# Output:
# special_chars: +2.341   ← strong attack indicator
# has_union:     +3.891   ← very strong attack indicator
# request_len:   +0.123   ← weak indicator
# entropy:       +1.567   ← moderate indicator
```

---

## 5.4 Naive Bayes

**The idea**: Apply Bayes' theorem with the "naive" assumption that features are independent.

```
P(attack | features) = P(features | attack) × P(attack)
                        ─────────────────────────────────
                                  P(features)
```

### Why "Naive"?
It assumes each feature contributes independently. In reality, `has_union_select` and `num_special_chars` are correlated. But despite this wrong assumption, Naive Bayes often works surprisingly well.

### Why It's Used in WAFs
1. **Extremely fast** — both training and prediction
2. **Works with small data** — doesn't need millions of examples
3. **Text classification** — natural fit for analyzing request bodies
4. **Used in TokioAI's WAF paper** — combined with GPT for zero-day detection

---

## 5.5 Comparison Table

| Algorithm | Speed | Data Needed | Interpretable | Best For |
|-----------|-------|-------------|---------------|----------|
| KNN | Slow predict | Small-Medium | Yes (neighbors) | Baseline, anomaly detection |
| K-Means | Fast | Medium-Large | Moderate | Clustering, anomaly discovery |
| Logistic Regression | Very Fast | Medium | Yes (weights) | Binary classification, baseline |
| Naive Bayes | Very Fast | Small | Yes (priors) | Text classification, WAF logs |
| Neural Networks | Slow train | Large | No (black box) | Complex patterns, images, sequences |

### The Rule
> **Start simple. Add complexity only when the simple model fails.**

If logistic regression gives you 95% accuracy on WAF logs, you don't need a neural network. Save the complexity for the edge cases where simple models break.

---

*Next: [Chapter 6 — Biases, Shortcuts & The Art of Validation →](06-biases.md)*
