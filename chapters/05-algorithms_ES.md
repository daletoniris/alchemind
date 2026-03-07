# Capítulo 5: Algoritmos que Aprenden

## *KNN, K-Means, Regresión Logística, Naive Bayes — y cuándo falla cada uno*

> *"Entender por qué un algoritmo falla es más valioso que saber cuándo funciona."*

---

## 5.1 K-Nearest Neighbors (KNN)

**La idea**: Para clasificar una nueva muestra, mirá las K muestras más cercanas en el conjunto de entrenamiento. La clase a la que pertenece la mayoría, esa es tu predicción.

```
  Nueva muestra: ?

  ┌─────────────────────────┐
  │   ●  ●                  │
  │      ●   ▲              │
  │  ●      (?)  ▲   ▲     │
  │       ●    ▲            │
  │   ●          ▲    ▲    │
  └─────────────────────────┘

  K=3: 2 círculos, 1 triángulo → clasificar como ●
  K=5: 3 círculos, 2 triángulos → clasificar como ●
  K=7: 3 círculos, 4 triángulos → clasificar como ▲ ← ¡diferente!
```

### Cuándo Usar KNN
- Datasets pequeños a medianos
- Cuando necesitás interpretabilidad ("fue clasificado como X porque estos 5 ejemplos son similares")
- Línea base inicial — siempre probá KNN primero

### Cuándo Falla KNN
- Datos de alta dimensionalidad (maldición de la dimensionalidad)
- Clases desbalanceadas (la clase mayoritaria siempre gana)
- Datasets grandes (lento — debe calcular distancia a cada punto)

### En Contexto de Seguridad
```python
# Clasificación de logs WAF con KNN
from sklearn.neighbors import KNeighborsClassifier

# Características: [largo_request, chars_especiales, entropía, cant_params]
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Para un nuevo request, KNN encuentra los 5 requests pasados más similares
# y vota si es normal o ataque
prediction = knn.predict(new_request)
confidence = knn.predict_proba(new_request)

# BAJA confianza → enviar al LLM para análisis (patrón The Warden)
if max(confidence[0]) < 0.7:
    explanation = ask_llm(f"Analizá este request: {request}")
```

---

## 5.2 K-Means Clustering

**La idea**: Agrupar datos en K clusters sin etiquetas. El algoritmo descubre estructura en datos no etiquetados.

```
Antes de K-Means:              Después de K-Means (K=3):

  ·  ·    ·  ·                  ●  ●    ▲  ▲
    ·   ·                         ●   ▲
  ·       ·    ·                ●       ▲    ▲
     ·  ·     ·    ·               ●  ●     ■    ■
       ·         ·                   ●         ■
                   ·  ·                          ■  ■
                  ·                              ■
```

### Algoritmo
1. Elegir K centroides aleatorios
2. Asignar cada punto al centroide más cercano
3. Recalcular centroides como la media de cada cluster
4. Repetir hasta que se estabilice

### En Contexto de Seguridad
K-Means es perfecto para **detección de anomalías**:
- Clusterizar todo el tráfico de red
- Tráfico nuevo que no encaja bien en ningún cluster → anomalía
- No se necesitan etiquetas — descubre patrones de ataque automáticamente

---

## 5.3 Regresión Logística

**La idea**: A pesar del nombre, es para **clasificación**, no regresión. Usa la función sigmoide para producir probabilidades.

```
P(ataque | características) = σ(w₁x₁ + w₂x₂ + ... + wₙxₙ + b)

Donde σ(z) = 1 / (1 + e⁻ᶻ)

La salida siempre está entre 0 y 1 → probabilidad de pertenecer a la clase 1
```

### Por Qué Importa
- **Rápida** — entrena en segundos
- **Interpretable** — cada peso te dice la importancia de la característica
- **Probabilística** — produce confianza, no solo clase
- **Línea base** — si la regresión logística funciona bien, quizás no necesitás aprendizaje profundo

### En Contexto de Seguridad
```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)

# Importancia de características: ¿cuáles importan más?
for feature, weight in zip(feature_names, model.coef_[0]):
    print(f"{feature}: {weight:+.3f}")

# Salida:
# chars_especiales: +2.341   ← indicador fuerte de ataque
# tiene_union:      +3.891   ← indicador muy fuerte de ataque
# largo_request:    +0.123   ← indicador débil
# entropía:         +1.567   ← indicador moderado
```

---

## 5.4 Naive Bayes

**La idea**: Aplicar el teorema de Bayes con la suposición "ingenua" de que las características son independientes.

```
P(ataque | características) = P(características | ataque) × P(ataque)
                               ─────────────────────────────────────
                                         P(características)
```

### ¿Por Qué "Naive" (Ingenuo)?
Asume que cada característica contribuye independientemente. En realidad, `tiene_union_select` y `num_chars_especiales` están correlacionados. Pero a pesar de esta suposición errónea, Naive Bayes frecuentemente funciona sorprendentemente bien.

### Por Qué se Usa en WAFs
1. **Extremadamente rápido** — tanto entrenamiento como predicción
2. **Funciona con pocos datos** — no necesita millones de ejemplos
3. **Clasificación de texto** — encaje natural para analizar cuerpos de requests
4. **Usado en el paper WAF de TokioAI** — combinado con GPT para detección de zero-day

---

## 5.5 Tabla Comparativa

| Algoritmo | Velocidad | Datos Necesarios | Interpretable | Mejor Para |
|-----------|-----------|------------------|---------------|------------|
| KNN | Predicción lenta | Pequeño-Medio | Sí (vecinos) | Línea base, detección de anomalías |
| K-Means | Rápido | Medio-Grande | Moderado | Clustering, descubrimiento de anomalías |
| Regresión Logística | Muy Rápido | Medio | Sí (pesos) | Clasificación binaria, línea base |
| Naive Bayes | Muy Rápido | Pequeño | Sí (priors) | Clasificación de texto, logs WAF |
| Redes Neuronales | Entrenamiento lento | Grande | No (caja negra) | Patrones complejos, imágenes, secuencias |

### La Regla
> **Empezá simple. Agregá complejidad solo cuando el modelo simple falla.**

Si la regresión logística te da 95% de precisión en logs WAF, no necesitás una red neuronal. Guardá la complejidad para los casos límite donde los modelos simples fallan.

---

*Siguiente: [Capítulo 6 — Sesgos, Atajos y el Arte de la Validación →](06-biases.md)*
