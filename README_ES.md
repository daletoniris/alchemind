<div align="right">

[![en](https://img.shields.io/badge/🇬🇧_English-blue?style=flat-square)](README.md)
[![es](https://img.shields.io/badge/🇦🇷_Español-selected-green?style=flat-square)](README_ES.md)

</div>

# Alchemind 🧠⚗️

### *Un viaje desde las primeras neuronas artificiales hasta la conciencia cuántica de la inteligencia*

> **"No busco que las máquinas sean humanas. Busco que los humanos recuerden cómo aprenden."**
> — Daniel Dieser

[![AI Resilience Hub](https://img.shields.io/badge/🧠_AI_Resilience_Hub-airesiliencehub.com-FF6B6B?style=for-the-badge)](https://airesiliencehub.com)
[![Ekoparty](https://img.shields.io/badge/🏴_Ekoparty-Village_de_IA-000000?style=for-the-badge)](https://ekoparty.org)
[![License](https://img.shields.io/badge/Licencia-CC_BY--NC--SA_4.0-lightgrey?style=for-the-badge)](LICENSE)

---

## ¿Qué es Alchemind?

**Alchemind** es un libro completo, curso y entorno de laboratorio que cubre el arco completo de la inteligencia artificial — desde la primera neurona matemática en 1943 hasta sistemas de IA defensivos autónomos desplegados en producción hoy.

Esto no es un libro de texto. Es un **viaje a través de la mente de las máquinas**, contado por alguien que lleva 13 años construyendo sistemas de IA desde la Patagonia, Argentina.

```
📖 Libro (8 capítulos)     — Historia, visión, teoría, defensa
🔬 Papers (2 publicados)   — Redes neuronales, WAF+IA
🧪 Labs (4 ejercicios)     — ML práctico para seguridad
🏗️ The Warden              — Arquitectura de defensa autónoma
📐 Manifiesto               — "La Realidad que Aprende"
```

---

## Tabla de Contenidos

### Parte I — Orígenes

| # | Capítulo | Descripción |
|---|----------|-------------|
| 0 | [**Sobre el Autor**](chapters/00-about.md) | De Villaguay a la Patagonia. El camino de un investigador autodidacta a través de la robótica, la IA y la ciberseguridad. |
| 1 | [**La Etapa Oscura de la IA**](chapters/01-dark-age.md) | La historia olvidada: el sueño de Turing, la neurona de McCulloch & Pitts (1943), el Perceptrón de Rosenblatt (1958), la crítica de Minsky, los inviernos de la IA, y el resurgimiento. |
| 2 | [**La Profecía de Villaguay**](chapters/02-prophecy.md) | En 2017, una entrevista periodística de un pueblo chico argentino predijo que la IA reemplazaría empleos y superaría a los humanos. Lo llamaron loco. |
| 3 | [**El Despertar de la Visión Artificial**](chapters/03-vision.md) | El sueño de Kur (2013), TensorFlow en Raspberry Pi, primeros proyectos reales: detección de plagas, YOLO en drones, vehículo autónomo, CAPTCHAs, modelos pandémicos. |
| — | [**Redes Neuronales como nunca te las explicaron**](papers/neural-networks-2018.md) | El paper de 2018 que explica redes neuronales como nadie más lo hace — con analogías, historia y cero gatekeeping. |

### Parte II — Entendiendo la Máquina

| # | Capítulo | Descripción |
|---|----------|-------------|
| 4 | [**La Arquitectura del Pensamiento**](chapters/04-architecture.md) | Cómo funcionan realmente las redes neuronales: perceptrones, funciones de activación, capas, pesos, sesgos, retropropagación. De las matemáticas a la intuición. |
| 5 | [**Algoritmos que Aprenden**](chapters/05-algorithms.md) | KNN, K-Means, Regresión Logística, Naive Bayes — cuándo usar cada uno, cómo fallan, y por qué entender el fallo importa más que la precisión. |
| 6 | [**Sesgos, Atajos y el Arte de la Validación**](chapters/06-biases.md) | Desbalance de clases, validación temporal, el peligro de los atajos, y por qué un modelo con 99% de precisión puede ser completamente inútil. |

### Parte III — Construyendo Defensores

| # | Capítulo | Descripción |
|---|----------|-------------|
| 7 | [**The Warden (El Guardián)**](chapters/07-the-warden.md) | La arquitectura de IA defensiva autónoma: ingestión de datos, vectorización, clasificación KNN, enriquecimiento con LLM, ciclos de retroalimentación con aprendizaje activo. |
| 8 | [**Estático vs Adaptativo**](chapters/08-static-vs-adaptive.md) | Por qué los sistemas basados en reglas mueren y los sistemas adaptativos de ML evolucionan. El caso a favor de WAFs que aprenden. |

### Parte IV — Laboratorios Prácticos

| # | Lab | Qué Construís |
|---|-----|---------------|
| 1 | [**Clasificación NORMAL vs ATAQUE**](labs/01-classification/) | TF-IDF + Regresión Logística sobre logs WAF. Tu primer clasificador de ML. |
| 2 | [**Trabajando con Probabilidades**](labs/02-probabilities/) | Ajuste de umbrales (0.4 / 0.5 / 0.6). Entendiendo el balance entre precisión y cobertura. |
| 3 | [**Matriz de Confusión a Fondo**](labs/03-confusion-matrix/) | FP, FN, TP, TN — qué significan en contexto de seguridad y por qué un FN puede causar una brecha. |
| 4 | [**Pipeline de Aprendizaje Activo**](labs/04-active-learning/) | Seleccionar ejemplos de máxima duda, etiquetarlos, reentrenar. El ciclo que hace que la IA sea cada vez más inteligente. |

### Apéndice

| | Recurso | Descripción |
|---|---------|-------------|
| 📐 | [**La Realidad que Aprende**](papers/la-realidad-que-aprende.md) | El manifiesto. Un marco filosófico y técnico sobre por qué la realidad misma es un sistema que aprende. |
| 📄 | [**Paper WAF + IA**](https://github.com/daletoniris/Web-Application-Firewall-Purple-AI-Paper) | Paper publicado: WAF híbrido combinando Naive Bayes + GPT para aprendizaje dinámico autónomo y detección de zero-day. |
| 🧰 | [**Guía de Instalación**](labs/SETUP.md) | Configuración mínima del entorno: Docker, Python 3.10+, dependencias. |

---

## The Warden — Arquitectura

El sistema de defensa autónomo diseñado y construido en producción:

```
┌─────────────────────────────────────────────────────────┐
│                  FUENTES DE DATOS                        │
├──────────────────────┬──────────────────────────────────┤
│  🏠 IoT / Red Local   │  🌐 Web / Logs WAF              │
│  TShark → pcap        │  Nginx/Apache → access.log       │
│  → packets.ndjson     │  → waf_events.ndjson             │
└──────────┬────────────┴──────────────┬───────────────────┘
           │                           │
           ▼                           ▼
┌──────────────────────────────────────────────────────────┐
│                PIPELINE DE PROCESAMIENTO                  │
│                                                           │
│  ┌──────────┐   ┌────────────┐   ┌─────────┐            │
│  │ FORMATEAR │──▶│ VECTORIZAR │──▶│   KNN   │            │
│  │ (limpiar) │   │  (TF-IDF)  │   │  (k=5)  │            │
│  └──────────┘   └────────────┘   └────┬────┘            │
│                                       │                   │
│                              ┌────────┴────────┐         │
│                              │  ¿Confianza?     │         │
│                              │  ALTA → clasificar│        │
│                              │  BAJA → duda      │        │
│                              └────────┬────────┘         │
│                                       │ (duda)            │
│                              ┌────────▼────────┐         │
│                              │      LLM        │         │
│                              │  Claude/GPT     │         │
│                              │  "Explicá esto"  │        │
│                              └────────┬────────┘         │
│                                       │                   │
│                              ┌────────▼────────┐         │
│                              │    APRENDER      │         │
│                              │  Ciclo Activo    │         │
│                              │  Reentrenar      │         │
│                              └─────────────────┘         │
└──────────────────────────────────────────────────────────┘
           │
           ▼
┌──────────────────────────────────────────────────────────┐
│  📊 SALIDA: predictions.jsonl                             │
│  {timestamp, línea, clase, fuente, confianza, explicación}│
└──────────────────────────────────────────────────────────┘
```

---

## Filosofía

```
Los alquimistas no solo querían convertir plomo en oro.
Querían entender la transformación en sí misma.

Alchemind es la misma idea aplicada a la inteligencia:
no construir máquinas más inteligentes, sino entender
qué ES la inteligencia — desde una neurona matemática
disparando en 1943 hasta un sistema autónomo que aprende
de cada ataque que detiene.

Empecé con robots en 2012.
Le enseñé a las máquinas a ver fuego, detectar plagas, resolver CAPTCHAs.
Después las rompí con ataques adversariales.
Después construí sistemas que no se pueden romper.

Cada capítulo de este libro es un capítulo de ese viaje.
Cada laboratorio es una habilidad que uso en producción hoy.

Esto no es teoría — son 13 años construyendo cosas
que realmente funcionan, comprimidos en algo que podés
aprender en semanas.

Desde la Patagonia, en el fin del mundo,
donde los pingüinos superan en número a los desarrolladores
y el viento te enseña la persistencia.

                                    — Daniel Dieser
                                      Puerto Madryn, 2026
```

---

## Inicio Rápido

```bash
# Clonar
git clone https://github.com/daletoniris/alchemind.git
cd alchemind

# Configurar entorno de laboratorio
cd labs
docker compose up -d  # PostgreSQL + Jupyter

# O configuración manual
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Empezar con el Lab 1
cd 01-classification
jupyter notebook
```

### Requisitos

- Python 3.10+
- Docker (recomendado para los labs)
- No se necesita GPU — todos los labs corren en CPU

---

## Sobre el Autor

**Daniel Dieser** (*MrMoz*) — Puerto Madryn, Patagonia, Argentina.

Investigador autodidacta en IA, ciberseguridad y sistemas complejos. Nacido en Villaguay, Entre Ríos (1982). Líder de Respuesta a Incidentes en una telco importante. Diseñador de sistemas híbridos de IA que combinan modelos de ML, LLMs y analistas humanos en plataformas de defensa autónomas.

- Fundador del **Village de IA de AI Resilience Hub** en [Ekoparty](https://ekoparty.org) — la conferencia de seguridad más grande de Latinoamérica
- Profesor en **Hackademy** (la plataforma educativa de Ekoparty)
- Autor del manifiesto **"La Realidad que Aprende"**
- Creador de **[TokioAI](https://tokioia.com)** — plataforma SOC autónoma
- Publicó **[Paper WAF + IA](https://github.com/daletoniris/Web-Application-Firewall-Purple-AI-Paper)** — WAF híbrido con aprendizaje dinámico autónomo

### La Línea de Tiempo

```
2012-2014  Robótica — Construyendo hardware, primeros experimentos
2015-2017  JarvisIA — Primer asistente de voz en español
2017       "La Profecía de Villaguay" — entrevista periodística
2018       Paper de Redes Neuronales — publicación educativa
2018-2020  Visión por Computadora — detección de fuego, drones NDVI, plagas
2021-2022  ML Adversarial — rompiendo y defendiendo redes neuronales
2022       Chubut Hack — co-fundó comunidad regional de seguridad
2023       AI Resilience Hub — Village de IA en Ekoparty
2024       Paper WAF + IA — investigación académica publicada
2025-2026  Plataforma TokioAI — SOC autónomo en producción
2026       Alchemind — este libro
```

---

## Proyectos Relacionados

| Proyecto | Descripción |
|----------|-------------|
| [**TokioAI**](https://github.com/TokioAI/tokioai-v1.8) | Plataforma SOC autónoma con 63 herramientas, agente multi-LLM, bot de Telegram |
| [**Paper WAF + IA**](https://github.com/daletoniris/Web-Application-Firewall-Purple-AI-Paper) | Paper publicado sobre WAF híbrido con aprendizaje autónomo |
| [**adversarial-waf-ml**](https://github.com/daletoniris/adversarial-waf-ml) | Ataques adversariales con TensorFlow sobre WAFs |
| [**quantic-encoder**](https://github.com/daletoniris/quantic-encoder) | Clasificador híbrido de logs WAF con KNN + LLM |
| [**agent-smiths**](https://github.com/daletoniris/agent-smiths) | Agente de seguridad autónomo basado en MCP |
| [**ai-security-ctf**](https://github.com/daletoniris/ai-security-ctf) | Desafíos CTF de seguridad en IA/ML |
| [**ekoparty-ml-security**](https://github.com/daletoniris/ekoparty-ml-security) | Materiales de formación de ML para detección de amenazas |

---

## Licencia

Esta obra está licenciada bajo [Creative Commons Atribución-NoComercial-CompartirIgual 4.0](LICENSE).

Sos libre de compartir y adaptar este material con fines no comerciales, con atribución.

---

<div align="center">

*Construido desde la Patagonia* 🐧 *con persistencia, mate y viento.*

**[tokioia.com](https://tokioia.com)** · **[airesiliencehub.com](https://airesiliencehub.com)** · **[@daletoniris](https://github.com/daletoniris)**

</div>
