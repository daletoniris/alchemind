# Capítulo 8: Estático vs Adaptativo

## *Por Qué los Sistemas Basados en Reglas Mueren y los Sistemas Adaptativos de ML Evolucionan*

> *"Un WAF estático es una pared. Un WAF adaptativo es un sistema inmunológico."*

---

## 8.1 El Problema con las Reglas

Las herramientas de seguridad tradicionales dependen de **firmas** — patrones predefinidos que coinciden con ataques conocidos:

```
# Ejemplo de Regla ModSecurity
SecRule ARGS "@rx (?i:union.*select)" "id:1001,deny,msg:'SQL Injection'"
```

Esta regla detecta `UNION SELECT`. ¿Pero qué pasa con?:

```
UNI/**/ON SEL/**/ECT          ← Bypass por comentarios
%55%4E%49%4F%4E %53%45%4C     ← Codificación URL
uNiOn SeLeCt                  ← Mezcla de mayúsculas/minúsculas
UNION ALL SELECT               ← Variación de sintaxis
0x554E494F4E 0x53454C454354    ← Codificación hexadecimal
```

Por **cada bypass**, alguien tiene que escribir una **nueva regla**. Es una carrera armamentista que los defensores siempre pierden porque los atacantes solo necesitan encontrar **un bypass**.

```
Defensa Estática:
  Nuevo ataque → Humano escribe regla → Desplegar regla → Protegido
  Tiempo: horas a días
  Escala: no escala

Defensa Adaptativa:
  Nuevo ataque → El modelo aprende el patrón → Se adapta instantáneamente
  Tiempo: segundos a minutos
  Escala: infinitamente
```

---

## 8.2 Por Qué lo Adaptativo Gana

| Aspecto | Estático (Reglas) | Adaptativo (ML) |
|---------|-------------------|-----------------|
| Ataques desconocidos | Ciego | Detecta anomalías |
| Evasión | Bypass por regla | Debe engañar al modelo |
| Mantenimiento | Actualización manual de reglas | Auto-mejora |
| Falsos positivos | Umbrales fijos | Confianza calibrada |
| Escala | Lineal (más reglas = más lento) | Constante (modelo entrenado) |
| Contexto | Ninguno (coincidencia de patrones) | Aprende contexto |
| Zero-days | No puede detectar | Puede detectar anomalías |

### La Idea Clave

Las reglas preguntan: **"¿Esto coincide con un ataque conocido?"**
ML pregunta: **"¿Esto se parece al tráfico normal?"**

El primer enfoque requiere conocer todos los ataques. El segundo requiere saber cómo se ve lo "normal". Como el tráfico normal es consistente y los ataques son diversos, aprender lo "normal" es mucho más efectivo.

---

## 8.3 El Enfoque Híbrido

Los mejores sistemas usan **ambos**:

```
Request → Reglas Estáticas (rápidas, seguras)
            │
            ├── Coincide → BLOQUEAR (ataque conocido)
            │
            └── No coincide → Modelo ML
                            │
                            ├── Alta confianza ataque → BLOQUEAR
                            ├── Alta confianza normal → PASAR
                            └── Incierto → Análisis LLM → Aprender
```

Las reglas estáticas manejan lo **conocido conocido** — rápido y certero.
ML maneja lo **conocido desconocido** — patrones similares a ataques pasados.
Los LLMs manejan lo **desconocido desconocido** — ataques novedosos que necesitan razonamiento.

Esta es la arquitectura de The Warden en la práctica.

---

## 8.4 Comparación en el Mundo Real

```
Escenario: Nueva variante de SQLi usando normalización Unicode

WAF Estático (ModSecurity):
  1. Llega el ataque: ＇ ＯＲ １＝１ ＃
  2. Las reglas buscan patrones ASCII → sin coincidencia
  3. Resultado: PASA ← BRECHA

WAF Adaptativo (The Warden):
  1. Llega el ataque: ＇ ＯＲ １＝１ ＃
  2. KNN ve: alta entropía, chars inusuales, endpoint de login
  3. Confianza: 0.62 (DUDA)
  4. Análisis LLM: "Caracteres Unicode fullwidth mapeando a sintaxis SQL"
  5. Resultado: BLOQUEAR + agregar al conjunto de entrenamiento
  6. Próximo ataque similar: confianza 0.93 → BLOQUEO instantáneo
```

---

## 8.5 La Curva de Evolución

```
Efectividad a lo largo del tiempo:

  100% ┤
       │                              ╱── Adaptativo (The Warden)
   80% │                        ╱───╱
       │                  ╱───╱
   60% │            ╱───╱
       │      ╱───╱
   40% │ ───╱─────────────────────── Estático (ModSecurity)
       │╱   ↑                    ↑
   20% │    Nuevo ataque         Otro nuevo ataque
       │    (ambos caen,         (el estático queda abajo,
    0% │    el adaptativo        el adaptativo se recupera
       │    se recupera)         más rápido)
       └──────────────────────────────────────────────
       Mes 1          Mes 6          Mes 12
```

Cada nuevo ataque reduce temporalmente la efectividad de ambos sistemas. Pero el sistema adaptativo **se recupera y mejora**, mientras el estático espera que un humano escriba una nueva regla.

---

## 8.6 Puntos Clave

1. **Las reglas estáticas son necesarias pero insuficientes** — son la base, no la solución
2. **Los modelos ML aprenden patrones, no firmas** — generalizan a ataques no vistos
3. **El enfoque híbrido gana** — reglas para lo conocido, ML para lo desconocido, LLM para lo incierto
4. **Los sistemas adaptativos mejoran con el tiempo** — los estáticos se degradan con el tiempo
5. **La carrera armamentista favorece al que aprende** — los atacantes deben engañar al modelo, no bypassear un regex

---

*Siguiente: [Lab 1 — Clasificación NORMAL vs ATAQUE →](../labs/01-classification/)*
