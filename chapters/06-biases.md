# Chapter 6: Biases, Shortcuts & The Art of Validation

## *Why a 99% accurate model might be completely useless*

> *"Your model isn't learning the attack. It's learning the timestamp."*

---

## 6.1 Class Imbalance — The Silent Killer

In security datasets, attacks are rare. A typical WAF log might have:
- 99% normal requests
- 1% attacks

A model that **always predicts "normal"** gets 99% accuracy. It also **misses every attack**.

```
Confusion Matrix of a "99% accurate" useless model:

                  Predicted
              Normal    Attack
Actual ┌──────────┬──────────┐
Normal │   9900   │    0     │  ← All correct
       ├──────────┼──────────┤
Attack │   100    │    0     │  ← ALL MISSED!
       └──────────┴──────────┘

Accuracy: 99%
Recall (attacks): 0%
Real-world value: ZERO
```

### Solutions
1. **Oversampling** attacks (SMOTE)
2. **Undersampling** normal traffic
3. **Class weights** — penalize missing attacks more heavily
4. **Use the right metric** — F1, Recall, not Accuracy

---

## 6.2 Shortcuts — When Models Cheat

Models find the **easiest pattern**, not the **right pattern**.

### Example: The Tank Legend
An apocryphal but instructive story: a neural network trained to detect tanks in photos achieved 100% accuracy on training data. Turns out, all tank photos were taken on cloudy days and non-tank photos on sunny days. The model learned **weather**, not tanks.

### In Security
```
Training data:
  - Attacks happen between 2-4 AM (when attackers are active)
  - Normal traffic happens 9 AM - 5 PM

Model learns:
  ❌ "2 AM = attack" (timestamp shortcut)
  ✅ Should learn: "UNION SELECT = attack" (content pattern)
```

### Prevention
- **Remove timestamp features** from security models
- **Validate on different time periods** (temporal validation)
- **Inspect feature importance** — if "hour_of_day" is the top feature, something is wrong

---

## 6.3 Temporal Validation

Standard cross-validation shuffles data randomly. For security data, this causes **data leakage** — the model sees future attacks during training.

```
❌ WRONG: Random split
┌────────────────────────────────────┐
│ Train: Jan ◆ Mar ◆ May ◆ Jul      │  ← Model sees future
│ Test:  Feb ◆ Apr ◆ Jun             │  ← Not realistic
└────────────────────────────────────┘

✅ CORRECT: Temporal split
┌────────────────────────────────────┐
│ Train: Jan → Feb → Mar → Apr      │  ← Past only
│ Test:  May → Jun → Jul             │  ← Future only
└────────────────────────────────────┘
```

The model must predict the future from the past — just like in production.

---

## 6.4 The Metrics That Matter

### For Security Classification

| Metric | Formula | Meaning | Priority |
|--------|---------|---------|----------|
| **Recall** | TP / (TP + FN) | "Of all attacks, how many did we catch?" | **#1** |
| **Precision** | TP / (TP + FP) | "Of what we flagged, how much was real?" | #2 |
| **F1** | 2 × (P × R) / (P + R) | Balance of precision and recall | #3 |
| **Accuracy** | (TP + TN) / Total | "Overall correctness" | **Useless alone** |

### The Trade-off
```
High Recall, Low Precision:    → Catch all attacks, many false alarms
High Precision, Low Recall:    → Few false alarms, miss real attacks
                                 ← THIS GETS YOU BREACHED

In security: ALWAYS favor recall.
A false alarm is annoying.
A missed attack is a breach.
```

---

## 6.5 The Confusion Matrix — Your Best Friend

```
                      Predicted
                 Normal       Attack
          ┌────────────┬────────────┐
  Actual  │    TN      │    FP      │
  Normal  │ True Neg   │ False Pos  │ ← "False alarm"
          │ (correct)  │ (annoying) │
          ├────────────┼────────────┤
  Actual  │    FN      │    TP      │
  Attack  │ False Neg  │ True Pos   │ ← FN = BREACH
          │ (DANGER!)  │ (correct)  │
          └────────────┴────────────┘

FN (False Negative) = You said "normal" but it was an attack
                    = The attacker got through
                    = THE WORST OUTCOME IN SECURITY
```

### Real Numbers Example
```
Your WAF processed 10,000 requests:
  - 9,800 normal
  - 200 attacks

Your model results:
  TN = 9,750 (normal, correctly passed)
  FP = 50    (normal, incorrectly blocked) → 50 annoyed users
  TP = 190   (attacks, correctly blocked)  → 190 threats stopped
  FN = 10    (attacks, missed)             → 10 POTENTIAL BREACHES

  Accuracy: 99.4% ← looks great
  Recall:   95.0% ← 10 attacks got through
  Precision: 79.2% ← 20% of blocks were false alarms

  Question: Is 95% recall acceptable?
  Answer:   Depends on what those 10 missed attacks were.
```

---

## 6.6 Key Takeaways

1. **Never trust accuracy alone** — especially with imbalanced data
2. **Always check for shortcuts** — inspect feature importance
3. **Use temporal validation** — never let the model see the future
4. **In security, recall > precision** — false alarms are better than breaches
5. **The confusion matrix tells the truth** — learn to read it

---

*Next: [Chapter 7 — The Warden (El Guardián) →](07-the-warden.md)*
