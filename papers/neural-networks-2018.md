# Redes Neuronales como nunca te las explicaron

### *Neural Networks Like Nobody Ever Explained Them (2018)*

> *Paper educativo — Daniel Dieser*

---

## Abstract

This paper explains neural networks from first principles, using analogies, history, and zero gatekeeping. Written in 2018 when the topic was still considered "advanced" — the goal was to make it accessible to anyone with basic math.

---

## 1. ¿Qué es una neurona artificial?

Imaginá una neurona como una **persona en una reunión** que tiene que tomar una decisión:

1. **Recibe opiniones** (inputs) de varias personas
2. **Cada opinión tiene un peso** — la opinión de tu jefe pesa más que la del pasante
3. **Suma todo** — pondera las opiniones
4. **Decide** — si la suma supera un umbral, actúa; si no, se queda quieta

```
Opinión del jefe (peso: 0.8):    "Hacelo"   → 0.8 × 1 = 0.8
Opinión del pasante (peso: 0.1): "No hagas" → 0.1 × 0 = 0.0
Opinión del cliente (peso: 0.6): "Hacelo"   → 0.6 × 1 = 0.6
                                              ─────────────
                                    Suma:     1.4
                                    Umbral:   1.0
                                    Decisión: SÍ (1.4 > 1.0)
```

Eso es literalmente una neurona artificial. El resto son variaciones sobre este tema.

---

## 2. De una neurona a una red

Una neurona sola es limitada — solo puede tomar decisiones lineales. Pero si conectás **muchas neuronas en capas**, pueden tomar decisiones complejas:

```
Capa 1: Detecta patrones simples
  - "¿Tiene caracteres especiales?"
  - "¿Es un request largo?"
  - "¿Usa método POST?"

Capa 2: Combina patrones
  - "Caracteres especiales + POST + largo = sospechoso"
  - "GET + corto + sin chars especiales = normal"

Capa 3: Decide
  - "ATAQUE" o "NORMAL"
```

Cada capa **abstrae** más. La primera ve píxeles, la segunda ve bordes, la tercera ve formas, la cuarta ve objetos. En seguridad: la primera ve bytes, la segunda ve patrones, la tercera ve ataques.

---

## 3. ¿Cómo aprende?

El proceso de aprendizaje es elegantemente simple:

1. **Mostrás un ejemplo**: "Este request es un ataque"
2. **La red predice**: "Yo creo que es normal"
3. **Calculás el error**: "Te equivocaste por 0.85"
4. **Ajustás los pesos**: "Las conexiones que causaron el error se debilitan, las que hubieran acertado se fortalecen"
5. **Repetís** miles de veces

```python
# Pseudocódigo del aprendizaje
for ejemplo in dataset:
    prediccion = red.predecir(ejemplo.input)
    error = ejemplo.label - prediccion
    red.ajustar_pesos(error, learning_rate=0.01)
    # Cada iteración, la red es un poquito menos estúpida
```

Esto se llama **gradient descent** (descenso por gradiente) y es la base de TODO el deep learning moderno. GPT-4, Stable Diffusion, AlphaFold — todos usan variaciones de este algoritmo de 1986.

---

## 4. Las funciones de activación

Sin función de activación, una red neuronal es solo una ecuación lineal elegante. La activación introduce **no-linealidad** — la capacidad de aprender curvas, no solo rectas.

### Sigmoid — La S elegante
```
Comprime cualquier número al rango (0, 1).
Útil para probabilidades: "¿Cuán probable es que esto sea un ataque?"
Problema: en redes profundas, los gradientes se desvanecen.
```

### ReLU — La navaja suiza
```
Si el número es positivo, lo deja pasar.
Si es negativo, lo convierte en cero.
Simple, rápido, y funciona sorprendentemente bien.
Es el default de la industria desde ~2012.
```

### Softmax — El jurado
```
Toma un vector de números y los convierte en probabilidades
que suman 1. Como un jurado que vota:
  [2.1, 1.0, 0.5] → [61%, 25%, 14%]
  "61% SQLi, 25% XSS, 14% Normal"
```

---

## 5. ¿Por qué importa esto para la seguridad?

Porque los atacantes **evolucionan** y las reglas estáticas no.

Un WAF basado en reglas necesita que alguien escriba una regla para cada ataque. Una red neuronal necesita **ejemplos** — y puede generalizar a ataques que nunca vio.

```
Regla:  IF request CONTAINS "UNION SELECT" → BLOCK
        (falla con: UNI/**/ON SEL/**/ECT)

Red:    Si se parece a los 10,000 ataques que vi antes → BLOCK
        (generaliza a variantes nuevas)
```

---

## 6. El futuro que predijimos

En 2018, cuando se escribió este paper:

- ChatGPT no existía
- GPT-2 no existía
- Los LLMs no eran mainstream
- "Inteligencia Artificial" todavía sonaba a ciencia ficción para la mayoría

Pero la matemática era clara: **más datos + más cómputo + mejores arquitecturas = mejores modelos**. Era cuestión de tiempo.

Hoy, en 2026, combinamos redes neuronales clásicas (KNN, logistic regression) con LLMs (Claude, GPT) para crear **sistemas autónomos de defensa** — exactamente lo que este paper anticipaba como el siguiente paso natural.

---

## References

1. McCulloch, W. S., & Pitts, W. (1943). A logical calculus of the ideas immanent in nervous activity.
2. Rosenblatt, F. (1958). The perceptron: A probabilistic model for information storage and organization in the brain.
3. Minsky, M., & Papert, S. (1969). Perceptrons.
4. Rumelhart, D. E., Hinton, G. E., & Williams, R. J. (1986). Learning representations by back-propagating errors.
5. Krizhevsky, A., Sutskever, I., & Hinton, G. E. (2012). ImageNet classification with deep convolutional neural networks.

---

*This paper was the seed. [Alchemind](../README.md) is the tree.*
