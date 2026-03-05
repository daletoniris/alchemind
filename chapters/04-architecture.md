# Chapter 4: The Architecture of Thought

## *How Neural Networks Actually Work*

> *"A neural network is not a brain. It's a function approximator that learns from examples. Once you understand that, everything clicks."*

---

## 4.1 The Perceptron Revisited

The simplest neural network is a single neuron — the perceptron:

```
        Inputs          Weights        Sum         Activation    Output
        ┌───┐          ┌──────┐
  x₁ ──│   │── w₁ ──┐ │      │
        └───┘         │ │      │
        ┌───┐         ├▶│  Σ   │──▶ f(z) ──▶ ŷ
  x₂ ──│   │── w₂ ──┤ │      │
        └───┘         │ │      │
        ┌───┐         │ │      │
  x₃ ──│   │── w₃ ──┘ │      │
        └───┘          └──────┘
                  (+b bias)

  z = w₁x₁ + w₂x₂ + w₃x₃ + b
  ŷ = f(z)
```

Every neural network, from the simplest classifier to GPT-4, is built from this basic unit.

---

## 4.2 Activation Functions

The activation function `f(z)` decides whether a neuron "fires." Without it, a neural network is just linear algebra — it can only learn straight lines.

### Step Function (Original Perceptron)
```
f(z) = 1 if z ≥ 0
f(z) = 0 if z < 0

  1 ─────────────────
                    │
  0 ────────────────┘
                    0
```
**Problem**: Not differentiable. Can't use gradient descent.

### Sigmoid
```
f(z) = 1 / (1 + e⁻ᶻ)

  1 ────────────╱─────
               ╱
  0.5 ────────╱───────
             ╱
  0 ────────╱─────────
            0

Output: (0, 1) — useful for probabilities
```
**Problem**: Vanishing gradients in deep networks.

### ReLU (Rectified Linear Unit)
```
f(z) = max(0, z)

        ╱
       ╱
  0 ──╱───────────────
     0

Output: [0, ∞)
```
**Why it won**: Simple, fast, solves vanishing gradient. Default choice for hidden layers.

### Softmax (Output Layer)
```
f(zᵢ) = e^zᵢ / Σ e^zⱼ

Converts raw scores into probabilities that sum to 1.
Used for multi-class classification.

Example: [2.0, 1.0, 0.5] → [0.59, 0.24, 0.13]
```

---

## 4.3 Layers — Depth is Power

A single perceptron can only learn **linearly separable** problems. Stack them in layers, and they can learn *anything*.

```
INPUT LAYER          HIDDEN LAYERS           OUTPUT LAYER
(features)           (representations)       (prediction)

  ○ ───────┐    ┌──── ○ ────┐    ┌──── ○ ───────── ○ (class A)
            ├───┤            ├───┤
  ○ ───────┤    ├──── ○ ────┤    ├──── ○ ───────── ○ (class B)
            ├───┤            ├───┤
  ○ ───────┤    ├──── ○ ────┤    └──── ○
            ├───┤            │
  ○ ───────┘    └──── ○ ────┘

Layer 1: Raw features (pixels, bytes, tokens)
Layer 2: Simple patterns (edges, character combos)
Layer 3: Complex patterns (shapes, attack signatures)
Output:  Decision (normal vs attack)
```

**Universal Approximation Theorem**: A neural network with at least one hidden layer can approximate *any* continuous function, given enough neurons.

---

## 4.4 How Learning Works — Backpropagation

Training a neural network is an optimization problem:

1. **Forward pass**: Feed input, get prediction
2. **Calculate loss**: How wrong was the prediction?
3. **Backward pass**: Calculate gradient of loss with respect to each weight
4. **Update weights**: Move weights in the direction that reduces loss

```
FORWARD PASS ──────────────────────────────────▶

  Input ──▶ Layer 1 ──▶ Layer 2 ──▶ Output ──▶ Loss
                                                 │
◀───────────────────────────────── BACKWARD PASS │
                                                 │
  ∂L/∂w₁ ◀── ∂L/∂w₂ ◀── ∂L/∂w₃ ◀── ∂L/∂ŷ ◀──┘

  w_new = w_old - learning_rate × gradient
```

### The Learning Rate

```
Too high:  ○ ──── ○ ──── ○ ──── ○   (oscillates, never converges)
                    ╲    ╱
                     ╲  ╱
                      ╳
                     ╱  ╲

Just right: ○ ─── ○ ── ○ ─ ○        (converges smoothly)
                       ╲
                        minimum

Too low:  ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○     (too slow, might get stuck)
```

---

## 4.5 In Practice — A Security Example

Let's say we want to classify web requests as NORMAL or ATTACK:

```python
import numpy as np

# Feature vector for a web request:
# [request_length, num_special_chars, has_union_select, entropy, ...]
X = np.array([
    [45,  2, 0, 3.2],    # Normal GET /index.html
    [312, 18, 1, 6.8],   # SQLi: ' UNION SELECT ...
    [28,  1, 0, 2.9],    # Normal GET /api/status
    [256, 22, 1, 7.1],   # SQLi: ' OR 1=1 --
])

y = np.array([0, 1, 0, 1])  # 0=normal, 1=attack

# A simple 2-layer network would learn:
# Layer 1: "high special chars + UNION → suspicious pattern"
# Layer 2: "suspicious pattern + high entropy → ATTACK"
```

The network doesn't know SQL injection. It learns the *pattern* of SQL injection from examples. Give it enough examples, and it will detect attacks it has never seen before.

This is the fundamental power — and the fundamental risk — of neural networks.

---

## 4.6 Key Takeaways

1. **Neurons are simple** — weighted sum + activation function
2. **Depth creates power** — multiple layers can learn any function
3. **Learning = optimization** — minimize loss through gradient descent
4. **Activation functions matter** — ReLU for hidden, sigmoid/softmax for output
5. **The learning rate is critical** — too high oscillates, too low stalls

---

*Next: [Chapter 5 — Algorithms That Learn →](05-algorithms.md)*
