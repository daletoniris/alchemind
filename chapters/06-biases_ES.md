# Capítulo 6: Sesgos, Atajos y el Arte de la Validación

## *Por qué un modelo con 99% de precisión puede ser completamente inútil*

> *"Tu modelo no está aprendiendo el ataque. Está aprendiendo el timestamp."*

---

## 6.1 Desbalance de Clases — El Asesino Silencioso

En datasets de seguridad, los ataques son raros. Un log WAF típico puede tener:
- 99% requests normales
- 1% ataques

Un modelo que **siempre predice "normal"** obtiene 99% de precisión. También **se pierde todos los ataques**.

```
Matriz de Confusión de un modelo "99% preciso" inútil:

                  Predicho
              Normal    Ataque
Real   ┌──────────┬──────────┐
Normal │   9900   │    0     │  ← Todo correcto
       ├──────────┼──────────┤
Ataque │   100    │    0     │  ← ¡TODOS PERDIDOS!
       └──────────┴──────────┘

Precisión: 99%
Recall (ataques): 0%
Valor en el mundo real: CERO
```

### Soluciones
1. **Sobremuestreo** de ataques (SMOTE)
2. **Submuestreo** de tráfico normal
3. **Pesos de clase** — penalizar más perder ataques
4. **Usar la métrica correcta** — F1, Recall, no Accuracy

---

## 6.2 Atajos — Cuando los Modelos Hacen Trampa

Los modelos encuentran el **patrón más fácil**, no el **patrón correcto**.

### Ejemplo: La Leyenda del Tanque
Una historia apócrifa pero instructiva: una red neuronal entrenada para detectar tanques en fotos logró 100% de precisión en datos de entrenamiento. Resulta que todas las fotos de tanques fueron tomadas en días nublados y las fotos sin tanques en días soleados. El modelo aprendió **el clima**, no tanques.

### En Seguridad
```
Datos de entrenamiento:
  - Los ataques ocurren entre las 2-4 AM (cuando los atacantes están activos)
  - El tráfico normal ocurre de 9 AM a 5 PM

El modelo aprende:
  ❌ "2 AM = ataque" (atajo por timestamp)
  ✅ Debería aprender: "UNION SELECT = ataque" (patrón de contenido)
```

### Prevención
- **Eliminar características de timestamp** de modelos de seguridad
- **Validar en diferentes períodos de tiempo** (validación temporal)
- **Inspeccionar importancia de características** — si "hora_del_día" es la característica principal, algo anda mal

---

## 6.3 Validación Temporal

La validación cruzada estándar mezcla datos aleatoriamente. Para datos de seguridad, esto causa **fuga de datos** — el modelo ve ataques futuros durante el entrenamiento.

```
❌ MAL: División aleatoria
┌────────────────────────────────────┐
│ Train: Ene ◆ Mar ◆ May ◆ Jul      │  ← El modelo ve el futuro
│ Test:  Feb ◆ Abr ◆ Jun             │  ← No es realista
└────────────────────────────────────┘

✅ BIEN: División temporal
┌────────────────────────────────────┐
│ Train: Ene → Feb → Mar → Abr      │  ← Solo el pasado
│ Test:  May → Jun → Jul             │  ← Solo el futuro
└────────────────────────────────────┘
```

El modelo debe predecir el futuro a partir del pasado — igual que en producción.

---

## 6.4 Las Métricas que Importan

### Para Clasificación de Seguridad

| Métrica | Fórmula | Significado | Prioridad |
|---------|---------|-------------|-----------|
| **Recall** | TP / (TP + FN) | "De todos los ataques, ¿cuántos detectamos?" | **#1** |
| **Precisión** | TP / (TP + FP) | "De lo que marcamos, ¿cuánto era real?" | #2 |
| **F1** | 2 × (P × R) / (P + R) | Balance entre precisión y recall | #3 |
| **Accuracy** | (TP + TN) / Total | "Corrección general" | **Inútil sola** |

### El Balance
```
Alto Recall, Baja Precisión:   → Detectar todos los ataques, muchas falsas alarmas
Alta Precisión, Bajo Recall:   → Pocas falsas alarmas, perder ataques reales
                                 ← ESTO TE CAUSA UNA BRECHA

En seguridad: SIEMPRE favorecer recall.
Una falsa alarma es molesta.
Un ataque perdido es una brecha.
```

---

## 6.5 La Matriz de Confusión — Tu Mejor Amiga

```
                      Predicho
                 Normal       Ataque
          ┌────────────┬────────────┐
  Real    │    TN      │    FP      │
  Normal  │ Verdadero  │ Falso      │ ← "Falsa alarma"
          │ Negativo   │ Positivo   │
          │ (correcto) │ (molesto)  │
          ├────────────┼────────────┤
  Real    │    FN      │    TP      │
  Ataque  │ Falso      │ Verdadero  │ ← FN = BRECHA
          │ Negativo   │ Positivo   │
          │ (¡PELIGRO!)│ (correcto) │
          └────────────┴────────────┘

FN (Falso Negativo) = Dijiste "normal" pero era un ataque
                    = El atacante pasó
                    = EL PEOR RESULTADO EN SEGURIDAD
```

### Ejemplo con Números Reales
```
Tu WAF procesó 10,000 requests:
  - 9,800 normales
  - 200 ataques

Resultados de tu modelo:
  TN = 9,750 (normales, correctamente pasados)
  FP = 50    (normales, incorrectamente bloqueados) → 50 usuarios molestos
  TP = 190   (ataques, correctamente bloqueados)    → 190 amenazas detenidas
  FN = 10    (ataques, perdidos)                    → 10 BRECHAS POTENCIALES

  Accuracy: 99.4% ← se ve genial
  Recall:   95.0% ← 10 ataques pasaron
  Precisión: 79.2% ← 20% de los bloqueos fueron falsas alarmas

  Pregunta: ¿Es aceptable 95% de recall?
  Respuesta: Depende de qué eran esos 10 ataques perdidos.
```

---

## 6.6 Puntos Clave

1. **Nunca confiar en accuracy sola** — especialmente con datos desbalanceados
2. **Siempre buscar atajos** — inspeccionar importancia de características
3. **Usar validación temporal** — nunca dejar que el modelo vea el futuro
4. **En seguridad, recall > precisión** — falsas alarmas son mejor que brechas
5. **La matriz de confusión dice la verdad** — aprendé a leerla

---

*Siguiente: [Capítulo 7 — The Warden (El Guardián) →](07-the-warden.md)*
