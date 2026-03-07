<div align="right">

[![en](https://img.shields.io/badge/🇬🇧_English-selected-green?style=flat-square)](README.md)
[![es](https://img.shields.io/badge/🇦🇷_Español-blue?style=flat-square)](README_ES.md)

</div>

# Alchemind 🧠⚗️

### *Un viaje desde las primeras neuronas artificiales hasta la conciencia cuántica de la inteligencia*

> **"No busco que las máquinas sean humanas. Busco que los humanos recuerden cómo aprenden."**
> — Daniel Dieser

[![AI Resilience Hub](https://img.shields.io/badge/🧠_AI_Resilience_Hub-airesiliencehub.com-FF6B6B?style=for-the-badge)](https://airesiliencehub.com)
[![Ekoparty](https://img.shields.io/badge/🏴_Ekoparty-AI_Village-000000?style=for-the-badge)](https://ekoparty.org)
[![License](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-lightgrey?style=for-the-badge)](LICENSE)

---

## What is Alchemind?

**Alchemind** is a comprehensive book, course, and lab environment covering the full arc of artificial intelligence — from the first mathematical neuron in 1943 to autonomous defensive AI systems deployed in production today.

This isn't a textbook. It's a **journey through the mind of machines**, told by someone who has been building AI systems for 13 years from Patagonia, Argentina.

```
📖 Book (8 chapters)     — History, vision, theory, defense
🔬 Papers (2 published)  — Neural networks, WAF+AI
🧪 Labs (4 exercises)    — Hands-on ML for security
🏗️ The Warden           — Autonomous defense architecture
📐 Manifesto             — "La Realidad que Aprende"
```

---

## Table of Contents

### Part I — Origins

| # | Chapter | Description |
|---|---------|-------------|
| 0 | [**About the Author**](chapters/00-about.md) | From Villaguay to Patagonia. A self-taught researcher's path through robotics, AI, and cybersecurity. |
| 1 | [**La Etapa Oscura de la IA**](chapters/01-dark-age.md) | The forgotten history: Turing's dream, McCulloch & Pitts' neuron (1943), Rosenblatt's Perceptron (1958), Minsky's critique, the AI winters, and the resurgence. |
| 2 | [**La Profecía de Villaguay**](chapters/02-prophecy.md) | In 2017, a newspaper interview from a small Argentine town predicted AI would replace jobs and surpass humans. They called it crazy. |
| 3 | [**El Despertar de la Visión Artificial**](chapters/03-vision.md) | The Kur dream (2013), TensorFlow on Raspberry Pi, first real projects: pest detection, drone YOLO, autonomous vehicle, CAPTCHAs, pandemic models. |
| — | [**Redes Neuronales como nunca te las explicaron**](papers/neural-networks-2018.md) | The 2018 paper that explains neural networks the way nobody else does — with analogies, history, and zero gatekeeping. |

### Part II — Understanding the Machine

| # | Chapter | Description |
|---|---------|-------------|
| 4 | [**The Architecture of Thought**](chapters/04-architecture.md) | How neural networks actually work: perceptrons, activation functions, layers, weights, biases, backpropagation. From math to intuition. |
| 5 | [**Algorithms That Learn**](chapters/05-algorithms.md) | KNN, K-Means, Logistic Regression, Naive Bayes — when to use each, how they fail, and why understanding failure matters more than accuracy. |
| 6 | [**Biases, Shortcuts & The Art of Validation**](chapters/06-biases.md) | Class imbalance, temporal validation, the danger of shortcuts, and why a 99% accurate model might be completely useless. |

### Part III — Building Defenders

| # | Chapter | Description |
|---|---------|-------------|
| 7 | [**The Warden (El Guardián)**](chapters/07-the-warden.md) | The autonomous defensive AI architecture: data ingestion, vectorization, KNN classification, LLM enrichment, active learning feedback loops. |
| 8 | [**Static vs Adaptive**](chapters/08-static-vs-adaptive.md) | Why rule-based systems die and adaptive ML systems evolve. The case for learning WAFs. |

### Part IV — Hands-On Labs

| # | Lab | What You Build |
|---|-----|---------------|
| 1 | [**NORMAL vs ATTACK Classification**](labs/01-classification/) | TF-IDF + Logistic Regression on WAF logs. Your first ML classifier. |
| 2 | [**Working with Probabilities**](labs/02-probabilities/) | Threshold tuning (0.4 / 0.5 / 0.6). Understanding precision vs recall trade-offs. |
| 3 | [**Confusion Matrix Deep Dive**](labs/03-confusion-matrix/) | FP, FN, TP, TN — what they mean in security context and why FN can get you breached. |
| 4 | [**Active Learning Pipeline**](labs/04-active-learning/) | Select maximum-doubt examples, label them, retrain. The loop that makes AI get smarter. |

### Appendix

| | Resource | Description |
|---|----------|-------------|
| 📐 | [**La Realidad que Aprende**](papers/la-realidad-que-aprende.md) | The manifesto. A philosophical and technical framework on why reality itself is a learning system. |
| 📄 | [**WAF + AI Paper**](https://github.com/daletoniris/Web-Application-Firewall-Purple-AI-Paper) | Published paper: hybrid WAF combining Naive Bayes + GPT for autonomous dynamic learning and zero-day detection. |
| 🧰 | [**Setup Guide**](labs/SETUP.md) | Minimal environment setup: Docker, Python 3.10+, dependencies. |

---

## The Warden — Architecture

The autonomous defensive system designed and built in production:

```
┌─────────────────────────────────────────────────────────┐
│                    DATA SOURCES                          │
├──────────────────────┬──────────────────────────────────┤
│  🏠 IoT / Home Net   │  🌐 Web / WAF Logs              │
│  TShark → pcap       │  Nginx/Apache → access.log       │
│  → packets.ndjson    │  → waf_events.ndjson             │
└──────────┬───────────┴──────────────┬───────────────────┘
           │                          │
           ▼                          ▼
┌──────────────────────────────────────────────────────────┐
│                   PROCESSING PIPELINE                     │
│                                                           │
│  ┌──────────┐   ┌────────────┐   ┌─────────┐            │
│  │  FORMAT   │──▶│ VECTORIZE  │──▶│   KNN   │            │
│  │  (clean)  │   │ (TF-IDF)   │   │ (k=5)   │            │
│  └──────────┘   └────────────┘   └────┬────┘            │
│                                       │                   │
│                              ┌────────┴────────┐         │
│                              │  Confidence?     │         │
│                              │  HIGH → classify │         │
│                              │  LOW  → doubt    │         │
│                              └────────┬────────┘         │
│                                       │ (doubt)           │
│                              ┌────────▼────────┐         │
│                              │      LLM        │         │
│                              │  Claude/GPT     │         │
│                              │  "Explain this"  │         │
│                              └────────┬────────┘         │
│                                       │                   │
│                              ┌────────▼────────┐         │
│                              │     LEARN       │         │
│                              │  Active Loop    │         │
│                              │  Retrain model  │         │
│                              └─────────────────┘         │
└──────────────────────────────────────────────────────────┘
           │
           ▼
┌──────────────────────────────────────────────────────────┐
│  📊 OUTPUT: predictions.jsonl                             │
│  {timestamp, line, class, source, confidence, explain}    │
└──────────────────────────────────────────────────────────┘
```

---

## Philosophy

```
The alchemists didn't just want to turn lead into gold.
They wanted to understand transformation itself.

Alchemind is the same idea applied to intelligence:
not building smarter machines, but understanding
what intelligence IS — from a mathematical neuron
firing in 1943 to an autonomous system that learns
from every attack it stops.

I started with robots in 2012.
I taught machines to see fire, detect pests, solve CAPTCHAs.
Then I broke them with adversarial attacks.
Then I built systems that can't be broken.

Every chapter of this book is a chapter of that journey.
Every lab is a skill I use in production today.

This isn't theory — this is 13 years of building things
that actually work, compressed into something you can
learn in weeks.

From Patagonia, at the end of the world,
where penguins outnumber developers
and the wind teaches you persistence.

                                    — Daniel Dieser
                                      Puerto Madryn, 2026
```

---

## Quick Start

```bash
# Clone
git clone https://github.com/daletoniris/alchemind.git
cd alchemind

# Setup lab environment
cd labs
docker compose up -d  # PostgreSQL + Jupyter

# Or manual setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Start with Lab 1
cd 01-classification
jupyter notebook
```

### Requirements

- Python 3.10+
- Docker (recommended for labs)
- No GPU required — all labs run on CPU

---

## About the Author

**Daniel Dieser** (*MrMoz*) — Puerto Madryn, Patagonia, Argentina.

Self-taught researcher in AI, cybersecurity, and complex systems. Born in Villaguay, Entre Ríos (1982). Lead Incident Response at a major telco. Designer of hybrid AI systems that combine ML models, LLMs, and human analysts into autonomous defense platforms.

- Founded **AI Resilience Hub Village** at [Ekoparty](https://ekoparty.org) — the largest security conference in Latin America
- Professor at **Hackademy** (Ekoparty's education platform)
- Author of **"La Realidad que Aprende"** manifesto
- Creator of **[TokioAI](https://tokioia.com)** — autonomous SOC platform
- Published **[WAF + AI Paper](https://github.com/daletoniris/Web-Application-Firewall-Purple-AI-Paper)** — hybrid WAF with autonomous dynamic learning

### The Timeline

```
2012-2014  Robotics — Building hardware, first experiments
2015-2017  JarvisIA — First Spanish voice assistant
2017       "La Profecía de Villaguay" — newspaper interview
2018       Neural Networks paper — educational publication
2018-2020  Computer Vision — fire detection, NDVI drones, pest detection
2021-2022  Adversarial ML — breaking and defending neural networks
2022       Chubut Hack — co-founded regional security community
2023       AI Resilience Hub — Ekoparty AI Village
2024       WAF + AI Paper — published academic research
2025-2026  TokioAI Platform — production autonomous SOC
2026       Alchemind — this book
```

---

## Related Projects

| Project | Description |
|---------|-------------|
| [**TokioAI**](https://github.com/TokioAI/tokioai-v1.8) | Autonomous SOC platform with 63 tools, multi-LLM agent, Telegram bot |
| [**WAF + AI Paper**](https://github.com/daletoniris/Web-Application-Firewall-Purple-AI-Paper) | Published paper on hybrid WAF with autonomous learning |
| [**adversarial-waf-ml**](https://github.com/daletoniris/adversarial-waf-ml) | TensorFlow adversarial attacks on WAFs |
| [**quantic-encoder**](https://github.com/daletoniris/quantic-encoder) | Hybrid WAF log classifier with KNN + LLM |
| [**agent-smiths**](https://github.com/daletoniris/agent-smiths) | MCP-based autonomous security agent |
| [**ai-security-ctf**](https://github.com/daletoniris/ai-security-ctf) | AI/ML security CTF challenges |
| [**ekoparty-ml-security**](https://github.com/daletoniris/ekoparty-ml-security) | ML for threat detection training materials |

---

## License

This work is licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0](LICENSE).

You are free to share and adapt this material for non-commercial purposes, with attribution.

---

<div align="center">

*Built from Patagonia* 🐧 *with persistence, mate, and wind.*

**[tokioia.com](https://tokioia.com)** · **[airesiliencehub.com](https://airesiliencehub.com)** · **[@daletoniris](https://github.com/daletoniris)**

</div>
