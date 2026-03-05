# Lab 1: NORMAL vs ATTACK Classification

## Objective

Build your first ML classifier that distinguishes normal web requests from attacks using TF-IDF vectorization and Logistic Regression.

## What You'll Learn

- Text vectorization with TF-IDF
- Training a binary classifier
- Evaluating model performance
- Understanding the decision boundary

## Run

```bash
python classify.py
```

## Expected Output

```
Training samples: 800
Test samples: 200

Classification Report:
              precision    recall  f1-score   support
      NORMAL       0.95      0.97      0.96       150
      ATTACK       0.89      0.84      0.86        50

Accuracy: 0.94
```
