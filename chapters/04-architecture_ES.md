# Capítulo 4: La Arquitectura del Pensamiento

## *Cómo Funcionan Realmente las Redes Neuronales*

> *"Una red neuronal no es un cerebro. Es un aproximador de funciones que aprende de ejemplos. Una vez que entendés eso, todo encaja."*

---

## 4.1 El Perceptrón Revisitado

La red neuronal más simple es una sola neurona — el perceptrón:

```
        Entradas        Pesos          Suma        Activación    Salida
        ┌───┐          ┌──────┐
  x₁ ──│   │── w₁ ──┐ │      │
        └───┘         │ │      │
        ┌───┐         ├▶│  Σ   │──▶ f(z) ──▶ ŷ
  x₂ ──│   │── w₂ ──┤ │      │
        └───┘         │ │      │
        ┌───┐         │ │      │
  x₃ ──│   │── w₃ ──┘ │      │
        └───┘          └──────┘
                  (+b sesgo)

  z = w₁x₁ + w₂x₂ + w₃x₃ + b
  ŷ = f(z)
```

Cada red neuronal, desde el clasificador más simple hasta GPT-4, está construida a partir de esta unidad básica.

---

## 4.2 Funciones de Activación

La función de activación `f(z)` decide si una neurona "dispara". Sin ella, una red neuronal es solo álgebra lineal — solo puede aprender líneas rectas.

### Función Escalón (Perceptrón Original)
```
f(z) = 1 si z ≥ 0
f(z) = 0 si z < 0

  1 ─────────────────
                    │
  0 ────────────────┘
                    0
```
**Problema**: No es diferenciable. No se puede usar descenso de gradiente.

### Sigmoide
```
f(z) = 1 / (1 + e⁻ᶻ)

  1 ────────────╱─────
               ╱
  0.5 ────────╱───────
             ╱
  0 ────────╱─────────
            0

Salida: (0, 1) — útil para probabilidades
```
**Problema**: Gradientes que se desvanecen en redes profundas.

### ReLU (Unidad Lineal Rectificada)
```
f(z) = max(0, z)

        ╱
       ╱
  0 ──╱───────────────
     0

Salida: [0, ∞)
```
**Por qué ganó**: Simple, rápida, resuelve el gradiente desvanecido. Opción por defecto para capas ocultas.

### Softmax (Capa de Salida)
```
f(zᵢ) = e^zᵢ / Σ e^zⱼ

Convierte puntajes crudos en probabilidades que suman 1.
Se usa para clasificación multi-clase.

Ejemplo: [2.0, 1.0, 0.5] → [0.59, 0.24, 0.13]
```

---

## 4.3 Capas — La Profundidad es Poder

Un solo perceptrón solo puede aprender problemas **linealmente separables**. Apilalos en capas, y pueden aprender *cualquier cosa*.

```
CAPA DE ENTRADA      CAPAS OCULTAS            CAPA DE SALIDA
(características)    (representaciones)       (predicción)

  ○ ───────┐    ┌──── ○ ────┐    ┌──── ○ ───────── ○ (clase A)
            ├───┤            ├───┤
  ○ ───────┤    ├──── ○ ────┤    ├──── ○ ───────── ○ (clase B)
            ├───┤            ├───┤
  ○ ───────┤    ├──── ○ ────┤    └──── ○
            ├───┤            │
  ○ ───────┘    └──── ○ ────┘

Capa 1: Características crudas (píxeles, bytes, tokens)
Capa 2: Patrones simples (bordes, combos de caracteres)
Capa 3: Patrones complejos (formas, firmas de ataque)
Salida:  Decisión (normal vs ataque)
```

**Teorema de Aproximación Universal**: Una red neuronal con al menos una capa oculta puede aproximar *cualquier* función continua, con suficientes neuronas.

---

## 4.4 Cómo Funciona el Aprendizaje — Retropropagación

Entrenar una red neuronal es un problema de optimización:

1. **Pasada hacia adelante**: Alimentar entrada, obtener predicción
2. **Calcular pérdida**: ¿Qué tan equivocada fue la predicción?
3. **Pasada hacia atrás**: Calcular gradiente de la pérdida con respecto a cada peso
4. **Actualizar pesos**: Mover los pesos en la dirección que reduce la pérdida

```
PASADA HACIA ADELANTE ─────────────────────────▶

  Entrada ──▶ Capa 1 ──▶ Capa 2 ──▶ Salida ──▶ Pérdida
                                                 │
◀──────────────────────────────── PASADA ATRÁS  │
                                                 │
  ∂L/∂w₁ ◀── ∂L/∂w₂ ◀── ∂L/∂w₃ ◀── ∂L/∂ŷ ◀──┘

  w_nuevo = w_viejo - tasa_aprendizaje × gradiente
```

### La Tasa de Aprendizaje

```
Muy alta:  ○ ──── ○ ──── ○ ──── ○   (oscila, nunca converge)
                    ╲    ╱
                     ╲  ╱
                      ╳
                     ╱  ╲

Justa:     ○ ─── ○ ── ○ ─ ○        (converge suavemente)
                       ╲
                        mínimo

Muy baja:  ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○     (muy lenta, puede quedarse atascada)
```

---

## 4.5 En la Práctica — Un Ejemplo de Seguridad

Supongamos que queremos clasificar requests web como NORMAL o ATAQUE:

```python
import numpy as np

# Vector de características para un request web:
# [largo_request, num_chars_especiales, tiene_union_select, entropía, ...]
X = np.array([
    [45,  2, 0, 3.2],    # Normal GET /index.html
    [312, 18, 1, 6.8],   # SQLi: ' UNION SELECT ...
    [28,  1, 0, 2.9],    # Normal GET /api/status
    [256, 22, 1, 7.1],   # SQLi: ' OR 1=1 --
])

y = np.array([0, 1, 0, 1])  # 0=normal, 1=ataque

# Una red simple de 2 capas aprendería:
# Capa 1: "muchos chars especiales + UNION → patrón sospechoso"
# Capa 2: "patrón sospechoso + alta entropía → ATAQUE"
```

La red no sabe SQL injection. Aprende el *patrón* de SQL injection a partir de ejemplos. Dale suficientes ejemplos, y detectará ataques que nunca vio antes.

Este es el poder fundamental — y el riesgo fundamental — de las redes neuronales.

---

## 4.6 Puntos Clave

1. **Las neuronas son simples** — suma ponderada + función de activación
2. **La profundidad crea poder** — múltiples capas pueden aprender cualquier función
3. **Aprender = optimizar** — minimizar la pérdida mediante descenso de gradiente
4. **Las funciones de activación importan** — ReLU para ocultas, sigmoide/softmax para salida
5. **La tasa de aprendizaje es crítica** — muy alta oscila, muy baja se estanca

---

*Siguiente: [Capítulo 5 — Algoritmos que Aprenden →](05-algorithms.md)*
