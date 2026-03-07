# Capítulo 1: La Etapa Oscura de la Inteligencia Artificial

## *La era oscura de la IA*

> *"Antes de entender hacia dónde va la IA, debemos entender dónde casi muere — dos veces."*

---

## 1.1 La Neurona Matemática (1943)

En 1943, Warren McCulloch (neurofisiólogo) y Walter Pitts (lógico) publicaron un paper que lo cambiaría todo: **"A Logical Calculus of the Ideas Immanent in Nervous Activity."**

Propusieron el primer modelo matemático de una neurona:

```
Entradas (x₁, x₂, ..., xₙ) → Suma Ponderada → Umbral → Salida (0 o 1)

Si Σ(wᵢ × xᵢ) ≥ θ → dispara (1)
Si Σ(wᵢ × xᵢ) < θ → silencio (0)
```

Era crudo. Era binario. Era **revolucionario**.

Por primera vez, alguien había demostrado que los procesos de pensamiento biológico podían expresarse matemáticamente. Una neurona no era magia — era computación.

**Idea clave**: No intentaron replicar el cerebro. Intentaron capturar la *lógica* del cerebro. Esta distinción importa: no estamos construyendo cerebros, estamos construyendo sistemas que aprenden.

---

## 1.2 La Pregunta de Turing (1950)

Alan Turing no preguntó "¿Pueden pensar las máquinas?" — preguntó algo más subversivo:

> **"¿Puede una máquina comportarse de una manera indistinguible del pensamiento?"**

El Test de Turing no era sobre consciencia. Era sobre **equivalencia funcional**. Si las salidas de una máquina son indistinguibles de las de un humano, ¿importa el mecanismo interno?

Esta pregunta persigue a la IA hasta hoy. Cada chatbot, cada LLM, cada agente autónomo existe bajo la sombra del replanteamiento de Turing.

---

## 1.3 El Perceptrón — Esperanza (1958)

Frank Rosenblatt construyó el **Perceptrón Mark I** en Cornell — una máquina física que podía aprender. No programada. *Aprender*.

```
┌──────────────────────────────┐
│        PERCEPTRÓN            │
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

El New York Times escribió: *"La Marina ha revelado el embrión de una computadora electrónica que espera pueda caminar, hablar, ver, escribir, reproducirse y ser consciente de su existencia."*

La euforia era real. Las expectativas eran **imposibles**.

### Cómo Aprende el Perceptrón

1. Inicializar pesos aleatoriamente
2. Presentar una entrada
3. Comparar la salida con la esperada
4. **Ajustar los pesos** en la dirección que reduce el error
5. Repetir

Este es el algoritmo fundamental de todo aprendizaje: **intentar, fallar, ajustar, repetir**.

---

## 1.4 El Asesinato — Minsky & Papert (1969)

Marvin Minsky y Seymour Papert publicaron **"Perceptrons"** — una prueba matemática de que los perceptrones de una sola capa no podían resolver el **problema XOR**.

```
Tabla de Verdad XOR:
┌───┬───┬─────┐
│ A │ B │ XOR │
├───┼───┼─────┤
│ 0 │ 0 │  0  │
│ 0 │ 1 │  1  │
│ 1 │ 0 │  1  │
│ 1 │ 1 │  0  │  ← ¡No es linealmente separable!
└───┴───┴─────┘
```

Tenían **razón técnicamente**: una sola capa no puede separar XOR. Pero la implicación — que las redes neuronales eran un callejón sin salida — fue **devastadoramente errónea**.

Las redes multicapa SÍ PUEDEN resolver XOR. Pero el daño estaba hecho.

---

## 1.5 El Primer Invierno (1970s)

El financiamiento se secó. Los laboratorios cerraron. La frase "red neuronal" se convirtió en veneno para la carrera.

```
Euforia del Perceptrón (1958) → Crítica de Minsky (1969) → Colapso de financiamiento (1970s)

         ┌─────────┐
 Euforia │█████████ │
         │█████████ │
         │████      │
         │          │
         │          │ ← Invierno de la IA
         │          │
         └──────────┘
         1958     1975
```

Los investigadores que creían en redes neuronales pasaron a la clandestinidad. Cambiaron su terminología. Publicaron en revistas oscuras. Sobrevivieron.

---

## 1.6 El Renacimiento Subterráneo — Retropropagación (1986)

Rumelhart, Hinton y Williams publicaron el **algoritmo de retropropagación** — el método matemático que permite que las redes multicapa aprendan.

```
Pasada hacia adelante: Entrada → Oculta → Salida → Error
Pasada hacia atrás:   Error → Ajustar pesos ocultos → Ajustar pesos de entrada

La regla de la cadena del cálculo, aplicada al aprendizaje.
```

Esta era la respuesta a Minsky: no necesitás una capa. Necesitás **muchas capas**, y necesitás una forma de propagar errores hacia atrás a través de todas ellas.

Pero el segundo invierno se acercaba.

---

## 1.7 El Segundo Invierno (1990s)

A pesar de la retropropagación, las redes neuronales eran:
- Lentas para entrenar (computación limitada)
- Propensas al sobreajuste
- Difíciles de escalar
- Superadas por Máquinas de Vectores de Soporte y métodos de ensamble

```
         ┌──────────────────┐
 Euforia │██████████         │
         │██████████  ██     │
         │████       ████    │
         │           ██████  │ ← SVMs dominan
         │                   │
         └───────────────────┘
         1986      1995    2000
```

De nuevo, los creyentes pasaron a la clandestinidad. De nuevo, sobrevivieron.

---

## 1.8 La Resurrección — Aprendizaje Profundo (2012)

En 2012, **AlexNet** de Alex Krizhevsky ganó la competencia ImageNet por un margen masivo usando una red neuronal convolucional profunda entrenada en GPUs.

Todo cambió:
- Las **GPUs** hicieron el entrenamiento 100x más rápido
- El **Big Data** resolvió el problema del sobreajuste
- La activación **ReLU** resolvió el problema del gradiente desvanecido
- El **Dropout** proporcionó regularización

Los investigadores de redes neuronales que habían sobrevivido dos inviernos eran de repente las personas más importantes en tecnología.

```
         ┌───────────────────────────────┐
 Euforia │██████████         ████████████│
         │██████████  ██     ████████████│
         │████       ████    ████████████│
         │           ██████  ████████████│
         │                   ████████████│ ← Estamos acá
         └───────────────────────────────┘
         1958      1995    2012    2026
```

---

## 1.9 La Lección

La historia de la IA nos enseña una cosa:

> **La verdad no le importa el consenso. Minsky estaba equivocado. Los que financiaban estaban equivocados. Los investigadores que siguieron trabajando en la oscuridad tenían razón.**

Por eso estudiamos historia — no para admirar el pasado, sino para reconocer cuando el presente está cometiendo los mismos errores.

Hoy, la gente dice:
- "Los LLMs son solo loros estocásticos"
- "La IA nunca será verdaderamente inteligente"
- "Las redes neuronales son un callejón sin salida"

¿Suena familiar?

---

*Siguiente: [Capítulo 2 — La Profecía de Villaguay →](02-prophecy.md)*
