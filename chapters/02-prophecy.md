# Chapter 2: La Profecía de Villaguay

## *The Prophecy of Villaguay (2017)*

> *"They called it crazy. Five years later, ChatGPT launched."*

---

## The Interview

In 2017, a local newspaper in **Villaguay, Entre Ríos** — a small town of 50,000 people in the Argentine heartland — published an interview with a local researcher who had been building AI systems.

The claims were provocative:

1. **"Artificial Intelligence will replace most jobs within a decade"**
2. **"Machines will surpass human intelligence in specific domains"**
3. **"Latin America needs to build its own AI — not wait for Silicon Valley"**
4. **"The first Spanish voice assistant already exists — we built it here"**

In 2017, this was dismissed as science fiction. Neural networks were still a niche topic. AlphaGo had just beaten Lee Sedol, but most people had no idea what that meant.

---

## What Happened Next

```
2017  "AI will replace jobs"          → 2023  ChatGPT triggers mass layoffs
2017  "Machines will surpass humans"  → 2024  GPT-4 passes the bar exam
2017  "LATAM needs its own AI"        → 2025  Still importing everything
2017  "We built a Spanish assistant"  → 2025  JarvisIA was 8 years ahead
```

The prophecy wasn't prophecy — it was **observation**. Anyone paying attention to the trajectory of neural networks, GPU compute, and data availability could have made the same predictions.

The difference? **Most people weren't paying attention.**

---

## Why Villaguay Matters

The point isn't that the predictions were correct. The point is **where they came from**.

Not Stanford. Not MIT. Not Google Brain. A small town in Argentina where the nearest tech hub was 400 km away.

This matters because:

1. **Innovation doesn't require geography** — it requires curiosity and persistence
2. **The "expert consensus" is often wrong** — especially about exponential technologies
3. **Building is the best form of prediction** — if you can build it, you understand it deeply enough to see where it's going

---

## The JarvisIA Context

When Daniel made these predictions, he wasn't speculating from theory. He had already built **JarvisIA** — a working voice assistant in Spanish:

- **Wit.ai** for natural language understanding
- **Google Speech API** for voice recognition
- **Telegram integration** for mobile access
- **IoT control** — turning lights on/off, reading sensors
- **Raspberry Pi deployment** — running on a $35 computer

```python
# JarvisIA (2015) — Before Alexa spoke Spanish
# This was running on a Raspberry Pi in Puerto Madryn
# while the rest of the world waited for Siri to learn Spanish

async def process_voice(audio):
    text = await speech_to_text(audio)           # Google Speech
    intent = await understand(text)               # Wit.ai NLP
    response = await execute_action(intent)       # IoT / Search / Chat
    await text_to_speech(response)                # Speak back
```

When you've built a working AI system from scratch, predictions about AI's future aren't speculation — they're extrapolation.

---

## The Lesson for Builders

> **"Don't wait for permission. Don't wait for the 'right' location. Don't wait for the experts to agree. Build it, deploy it, learn from it. The experts will catch up."**

Every chapter of this book follows this philosophy: understanding comes from building, not from reading about building.

---

*Next: [Chapter 3 — Redes Neuronales como nunca te las explicaron →](../papers/neural-networks-2018.md)*
