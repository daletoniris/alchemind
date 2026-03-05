"""
Lab 3: Confusion Matrix Deep Dive
====================================
Understanding TP, TN, FP, FN in security context.

The confusion matrix is your best friend in security ML.
Learn to read it like a security analyst reads logs.
"""

import numpy as np

# Simulated predictions from a WAF classifier
# In production, these come from your model's predict()
np.random.seed(42)

n_samples = 1000
n_attacks = 50  # 5% attack rate (realistic)
n_normal = n_samples - n_attacks

# True labels
y_true = np.array([0] * n_normal + [1] * n_attacks)

# Simulated model predictions (imperfect classifier)
y_pred = y_true.copy()

# Introduce errors:
# 30 false positives (normal flagged as attack)
fp_indices = np.random.choice(range(n_normal), 30, replace=False)
y_pred[fp_indices] = 1

# 5 false negatives (attacks missed) — THE DANGEROUS ONES
fn_indices = np.random.choice(range(n_normal, n_samples), 5, replace=False)
y_pred[fn_indices] = 0

# ============================================================
# BUILD CONFUSION MATRIX
# ============================================================
TP = sum((y_pred == 1) & (y_true == 1))  # Correctly blocked attacks
TN = sum((y_pred == 0) & (y_true == 0))  # Correctly passed normal
FP = sum((y_pred == 1) & (y_true == 0))  # False alarms
FN = sum((y_pred == 0) & (y_true == 1))  # MISSED ATTACKS

print("=" * 60)
print("CONFUSION MATRIX — WAF Classifier Results")
print("=" * 60)
print()
print("                        PREDICTED")
print("                   Normal      Attack")
print("              ┌────────────┬────────────┐")
print(f"  ACTUAL      │  TN={TN:4d}   │  FP={FP:4d}   │")
print(f"  Normal      │ (correct)  │ (annoying) │")
print("              ├────────────┼────────────┤")
print(f"  ACTUAL      │  FN={FN:4d}   │  TP={TP:4d}   │")
print(f"  Attack      │ (BREACH!)  │ (correct)  │")
print("              └────────────┴────────────┘")

print()
print("─" * 60)
print("METRICS")
print("─" * 60)

accuracy = (TP + TN) / (TP + TN + FP + FN)
precision = TP / (TP + FP) if (TP + FP) > 0 else 0
recall = TP / (TP + FN) if (TP + FN) > 0 else 0
f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
fpr = FP / (FP + TN) if (FP + TN) > 0 else 0

print(f"  Accuracy:   {accuracy:.4f} ({accuracy:.1%})")
print(f"  Precision:  {precision:.4f} ({precision:.1%}) — Of blocks, how many were real attacks?")
print(f"  Recall:     {recall:.4f} ({recall:.1%}) — Of attacks, how many did we catch?")
print(f"  F1 Score:   {f1:.4f}")
print(f"  FP Rate:    {fpr:.4f} ({fpr:.1%}) — Of normal traffic, how much was blocked?")

print()
print("─" * 60)
print("SECURITY ANALYSIS")
print("─" * 60)
print()
print(f"  Total requests processed: {n_samples}")
print(f"  Attacks in dataset:       {n_attacks} ({n_attacks/n_samples:.1%})")
print()
print(f"  Attacks CAUGHT:    {TP}/{n_attacks} — These threats were stopped")
print(f"  Attacks MISSED:    {FN}/{n_attacks} — These got through to your server")
print(f"  False alarms:      {FP}/{n_normal} — Legitimate users blocked")
print()

if FN > 0:
    print(f"  !! WARNING: {FN} attacks were NOT detected !!")
    print(f"  This means {FN} potential breaches went unnoticed.")
    print(f"  In a real environment, each missed attack could mean:")
    print(f"    - Data exfiltration")
    print(f"    - Server compromise")
    print(f"    - Lateral movement")
    print()

print(f"  False alarm rate: {FP} out of {n_normal} normal requests ({fpr:.2%})")
print(f"  This means {FP} legitimate users were temporarily blocked.")
print(f"  Annoying? Yes. Dangerous? No.")
print()
print("  CONCLUSION: In security, we ALWAYS prefer FP over FN.")
print("              A blocked user complains. A missed attack breaches.")
print()
print("Next: Lab 4 — Active Learning Pipeline")
