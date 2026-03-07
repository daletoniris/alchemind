# Lab 1: Clasificación NORMAL vs ATAQUE

## Objetivo

Construí tu primer clasificador ML que distingue requests web normales de ataques usando vectorización TF-IDF y Regresión Logística.

## Qué Vas a Aprender

- Vectorización de texto con TF-IDF
- Entrenar un clasificador binario
- Evaluar el rendimiento del modelo
- Entender la frontera de decisión

## Ejecutar

```bash
python classify.py
```

## Salida Esperada

```
Muestras de entrenamiento: 800
Muestras de test: 200

Reporte de Clasificación:
              precision    recall  f1-score   support
      NORMAL       0.95      0.97      0.96       150
      ATAQUE       0.89      0.84      0.86        50

Accuracy: 0.94
```
