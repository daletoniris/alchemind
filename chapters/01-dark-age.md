# Chapter 1: La Etapa Oscura de la Inteligencia Artificial

## *The Dark Age of Artificial Intelligence*

> *"Before we can understand where AI is going, we must understand where it almost died — twice."*

---

## 1.1 The Mathematical Neuron (1943)

In 1943, Warren McCulloch (neurophysiologist) and Walter Pitts (logician) published a paper that would change everything: **"A Logical Calculus of the Ideas Immanent in Nervous Activity."**

They proposed the first mathematical model of a neuron:

```
Inputs (x₁, x₂, ..., xₙ) → Weighted Sum → Threshold → Output (0 or 1)

If Σ(wᵢ × xᵢ) ≥ θ → fire (1)
If Σ(wᵢ × xᵢ) < θ → silent (0)
```

It was crude. It was binary. It was **revolutionary**.

For the first time, someone had shown that biological thought processes could be expressed mathematically. A neuron wasn't magic — it was computation.

**Key insight**: They didn't try to replicate the brain. They tried to capture the *logic* of the brain. This distinction matters: we're not building brains, we're building systems that learn.

---

## 1.2 Turing's Question (1950)

Alan Turing didn't ask "Can machines think?" — he asked something more subversive:

> **"Can a machine behave in a way that is indistinguishable from thinking?"**

The Turing Test wasn't about consciousness. It was about **functional equivalence**. If a machine's outputs are indistinguishable from a human's, does the internal mechanism matter?

This question haunts AI to this day. Every chatbot, every LLM, every autonomous agent exists in the shadow of Turing's reframing.

---

## 1.3 The Perceptron — Hope (1958)

Frank Rosenblatt built the **Mark I Perceptron** at Cornell — a physical machine that could learn. Not programmed. *Learn*.

```
┌──────────────────────────────┐
│        PERCEPTRON            │
│                              │
│  x₁ ──[w₁]──┐               │
│  x₂ ──[w₂]──┤               │
│  x₃ ──[w₃]──┼── Σ ── f() ── y
│  ...         │               │
│  xₙ ──[wₙ]──┘               │
│                              │
│  y = f(Σ wᵢxᵢ + b)          │
└──────────────────────────────┘
```

The New York Times wrote: *"The Navy has revealed the embryo of an electronic computer that it expects will be able to walk, talk, see, write, reproduce itself, and be conscious of its existence."*

The hype was real. The expectations were **impossible**.

### How the Perceptron Learns

1. Initialize weights randomly
2. Present an input
3. Compare output to expected
4. **Adjust weights** in the direction that reduces error
5. Repeat

This is the fundamental algorithm of all learning: **try, fail, adjust, repeat**.

---

## 1.4 The Assassination — Minsky & Papert (1969)

Marvin Minsky and Seymour Papert published **"Perceptrons"** — a mathematical proof that single-layer perceptrons could not solve the **XOR problem**.

```
XOR Truth Table:
┌───┬───┬─────┐
│ A │ B │ XOR │
├───┼───┼─────┤
│ 0 │ 0 │  0  │
│ 0 │ 1 │  1  │
│ 1 │ 0 │  1  │
│ 1 │ 1 │  0  │  ← Not linearly separable!
└───┴───┴─────┘
```

They were **technically correct**: a single layer cannot separate XOR. But the implication — that neural networks were a dead end — was **devastatingly wrong**.

Multi-layer networks CAN solve XOR. But the damage was done.

---

## 1.5 The First Winter (1970s)

Funding dried up. Research labs closed. The word "neural network" became career poison.

```
Perceptron hype (1958) → Minsky's critique (1969) → Funding collapse (1970s)

         ┌─────────┐
    Hype │█████████ │
         │█████████ │
         │████      │
         │          │
         │          │ ← AI Winter
         │          │
         └──────────┘
         1958     1975
```

Researchers who believed in neural networks went underground. They changed their terminology. They published in obscure journals. They survived.

---

## 1.6 The Underground Revival — Backpropagation (1986)

Rumelhart, Hinton, and Williams published the **backpropagation algorithm** — the mathematical method that allows multi-layer networks to learn.

```
Forward Pass:  Input → Hidden → Output → Error
Backward Pass: Error → Adjust hidden weights → Adjust input weights

The chain rule of calculus, applied to learning.
```

This was the answer to Minsky: you don't need one layer. You need **many layers**, and you need a way to propagate errors backward through all of them.

But the second winter was coming.

---

## 1.7 The Second Winter (1990s)

Despite backpropagation, neural networks were:
- Slow to train (limited compute)
- Prone to overfitting
- Difficult to scale
- Outperformed by Support Vector Machines and ensemble methods

```
         ┌──────────────────┐
    Hype │██████████         │
         │██████████  ██     │
         │████       ████    │
         │           ██████  │ ← SVMs dominate
         │                   │
         └───────────────────┘
         1986      1995    2000
```

Again, the believers went underground. Again, they survived.

---

## 1.8 The Resurrection — Deep Learning (2012)

In 2012, Alex Krizhevsky's **AlexNet** won the ImageNet competition by a massive margin using a deep convolutional neural network trained on GPUs.

Everything changed:
- **GPUs** made training 100x faster
- **Big data** solved the overfitting problem
- **ReLU** activation solved the vanishing gradient problem
- **Dropout** provided regularization

The neural network researchers who had survived two winters were suddenly the most important people in tech.

```
         ┌───────────────────────────────┐
    Hype │██████████         ████████████│
         │██████████  ██     ████████████│
         │████       ████    ████████████│
         │           ██████  ████████████│
         │                   ████████████│ ← We are here
         └───────────────────────────────┘
         1958      1995    2012    2026
```

---

## 1.9 The Lesson

The history of AI teaches us one thing:

> **The truth doesn't care about consensus. Minsky was wrong. The funders were wrong. The researchers who kept working in the dark were right.**

This is why we study history — not to admire the past, but to recognize when the present is making the same mistakes.

Today, people say:
- "LLMs are just stochastic parrots"
- "AI will never be truly intelligent"
- "Neural networks are a dead end"

Sound familiar?

---

*Next: [Chapter 2 — La Profecía de Villaguay →](02-prophecy.md)*
