# Capítulo 7: The Warden (El Guardián)

## *Una Arquitectura de IA Defensiva Autónoma*

> *"Un guardián que nunca duerme, aprende de cada ataque, y pide ayuda cuando no está seguro."*

---

## 7.1 La Visión

The Warden no es una herramienta única — es una **arquitectura** para construir sistemas de IA defensivos autónomos. Combina tres pilares:

1. **Clasificación ML** — Coincidencia de patrones estadística rápida (KNN)
2. **Análisis LLM** — Razonamiento profundo para casos inciertos (Claude/GPT)
3. **Aprendizaje Activo** — Mejora continua a partir de retroalimentación humana

```
The Warden: "Sé lo que sé, sé lo que no sé,
             y pregunto cuando no estoy seguro."
```

Esta es la diferencia crítica con las herramientas de seguridad tradicionales: The Warden tiene **incertidumbre calibrada**. No solo clasifica — sabe **qué tan seguro** está.

---

## 7.2 Arquitectura

```
┌──────────────────────────────────────────────────────────────┐
│                    FUENTES DE DATOS                            │
│                                                               │
│  🏠 IoT / Red Local               🌐 Web / WAF               │
│  ┌──────────────┐               ┌──────────────┐             │
│  │   TShark     │               │ Nginx/Apache │             │
│  │   tcpdump    │               │ access.log   │             │
│  │   → pcap     │               │ error.log    │             │
│  └──────┬───────┘               └──────┬───────┘             │
│         │                              │                      │
│         ▼                              ▼                      │
│  packets.ndjson                 waf_events.ndjson             │
└─────────┬──────────────────────────────┬─────────────────────┘
          │                              │
          ▼                              ▼
┌──────────────────────────────────────────────────────────────┐
│                PIPELINE DE PROCESAMIENTO                       │
│                                                               │
│  ┌──────────┐   ┌────────────┐   ┌──────────┐               │
│  │1.FORMATEAR│──▶│2.VECTORIZAR│──▶│ 3. KNN   │               │
│  │          │   │            │   │          │               │
│  │ Limpiar  │   │ TF-IDF    │   │ k=5      │               │
│  │Normalizar│   │ Extracción│   │ Distancia│               │
│  │ Parsear  │   │ de Caract.│   │ Ponderada│               │
│  └──────────┘   └────────────┘   └────┬─────┘               │
│                                       │                       │
│                              ┌────────┴─────────┐            │
│                              │ 4. CONFIANZA      │            │
│                              │                   │            │
│                              │  ALTA (≥0.85)     │            │
│                              │  → Auto-clasificar│            │
│                              │                   │            │
│                              │  MEDIA (0.5-0.85) │            │
│                              │  → Marcar + clasif│            │
│                              │                   │            │
│                              │  BAJA (<0.5)      │            │
│                              │  → DUDA → LLM     │            │
│                              └────────┬─────────┘            │
│                                       │ (duda)                │
│                              ┌────────▼─────────┐            │
│                              │ 5. ANÁLISIS LLM  │            │
│                              │                   │            │
│                              │ Claude / GPT      │            │
│                              │ "Analizá este     │            │
│                              │  request y        │            │
│                              │  explicá por qué  │            │
│                              │  podría ser un    │            │
│                              │  ataque"          │            │
│                              └────────┬─────────┘            │
│                                       │                       │
│                              ┌────────▼─────────┐            │
│                              │ 6. APRENDIZAJE   │            │
│                              │    ACTIVO         │            │
│                              │                   │            │
│                              │ Guardar resultado │            │
│                              │ del LLM           │            │
│                              │ Poner en cola para│            │
│                              │ revisión humana   │            │
│                              │ Reentrenar KNN    │            │
│                              │ con etiquetas     │            │
│                              │ confirmadas       │            │
│                              └──────────────────┘            │
└──────────────────────────────────────────────────────────────┘
          │
          ▼
┌──────────────────────────────────────────────────────────────┐
│  📊 SALIDA: predictions.jsonl                                 │
│                                                               │
│  {                                                            │
│    "timestamp": "2026-03-04T14:23:01Z",                      │
│    "line": "GET /api?id=1' UNION SELECT...",                 │
│    "class": "ATAQUE",                                         │
│    "confidence": 0.94,                                        │
│    "source": "knn",                                           │
│    "explanation": "Patrón de SQL injection detectado"         │
│  }                                                            │
└──────────────────────────────────────────────────────────────┘
```

---

## 7.3 La Innovación Clave: Incertidumbre Calibrada

La mayoría de las herramientas de seguridad son binarias: alerta o no alerta. The Warden introduce un **tercer estado**: duda.

```
WAF Tradicional:
  Request → Reglas → BLOQUEAR o PASAR
  (sin punto medio, sin aprendizaje)

The Warden:
  Request → KNN → Puntaje de Confianza

  ALTA confianza   → Actuar inmediatamente (bloquear/pasar)
  BAJA confianza   → Pedir análisis al LLM
  LLM + Humano     → Agregar al conjunto de entrenamiento
  Conjunto entrena. → Reentrenar KNN
  Mejor KNN        → Menos dudas la próxima vez
```

Esto crea un **ciclo virtuoso**: el sistema mejora con el tiempo, específicamente en las áreas donde es más débil.

---

## 7.4 Pipeline Dual: IoT + Web

### Pipeline IoT / Red Local

```python
# Fuente de datos: captura de paquetes TShark
# Formato: packets.ndjson

{
    "timestamp": "2026-03-04T14:23:01.234",
    "src_ip": "192.168.1.105",
    "dst_ip": "203.0.113.50",
    "protocol": "TCP",
    "dst_port": 443,
    "payload_size": 1420,
    "flags": "PSH,ACK",
    "device_mac": "aa:bb:cc:dd:ee:ff"
}

# Características extraídas:
# - Tasa de paquetes por dispositivo
# - Diversidad de destinos (cuántas IPs únicas)
# - Distribución de protocolos
# - Anomalías en tamaño de payload
# - Patrones por hora del día
# - Uso de puertos C2 conocidos
```

**Qué detecta**: Dispositivos IoT comunicándose con servidores C2, movimiento lateral, exfiltración DNS, patrones de tráfico inusuales a las 3 AM.

### Pipeline Web / WAF

```python
# Fuente de datos: logs Nginx/Apache
# Formato: waf_events.ndjson

{
    "timestamp": "2026-03-04T14:23:01.234",
    "client_ip": "203.0.113.50",
    "method": "POST",
    "uri": "/api/login",
    "status": 200,
    "body": "username=admin&password=' OR 1=1 --",
    "user_agent": "Mozilla/5.0...",
    "content_length": 156
}

# Características extraídas:
# - TF-IDF de URI + body (captura patrones de ataque)
# - Ratio de caracteres especiales
# - Entropía de parámetros
# - Tasa de requests desde IP
# - Puntaje de anomalía de user-agent
# - Coincidencias con patrones de ataque conocidos
```

**Qué detecta**: SQLi, XSS, path traversal, credential stuffing, web shells, payloads zero-day (via análisis LLM).

---

## 7.5 Aprendizaje Activo — El Arma Secreta

El aprendizaje activo es lo que hace a The Warden fundamentalmente diferente de las herramientas de seguridad estáticas:

```
┌──────────────────────────────────────────┐
│      CICLO DE APRENDIZAJE ACTIVO         │
│                                          │
│  1. KNN clasifica request                │
│     → confianza = 0.52 (DUDA)            │
│                                          │
│  2. LLM analiza request                  │
│     → "Esto parece ser una variante      │
│        novedosa de inyección XXE"         │
│     → clase = ATAQUE                     │
│                                          │
│  3. Humano revisa decisión del LLM       │
│     → Confirma: ATAQUE ✓                 │
│                                          │
│  4. Agregar al conjunto de entrenamiento │
│     → (características, ATAQUE) agregado │
│                                          │
│  5. Reentrenar KNN                       │
│     → El modelo ahora reconoce patrones  │
│       XXE                                │
│                                          │
│  6. Próximo request similar:             │
│     → confianza = 0.91 (ALTA)            │
│     → No se necesita LLM                 │
│     → Más rápido, más barato, autónomo   │
└──────────────────────────────────────────┘
```

### Estrategia de Selección: Máxima Duda

No todas las muestras inciertas son igualmente valiosas. The Warden selecciona ejemplos donde:

```python
# Seleccionar las muestras donde el modelo está MÁS confundido
# Estas son las más valiosas para etiquetar

uncertainty = abs(0.5 - prediction_probability)
# incertidumbre cerca de 0 = máxima duda
# incertidumbre cerca de 0.5 = muy seguro

most_valuable = sorted(unlabeled, key=lambda x: uncertainty(x))[:batch_size]
# Etiquetar estas → máximo aprendizaje por muestra etiquetada
```

---

## 7.6 Despliegue en Producción

The Warden está diseñado para despliegue real, no para papers académicos:

```yaml
# docker-compose.yml (simplificado)
services:
  collector:
    # Colector de logs TShark / Nginx
    volumes:
      - ./data:/data

  classifier:
    # Pipeline KNN + TF-IDF
    # Lee: data/*.ndjson
    # Escribe: predictions.jsonl
    environment:
      - MODEL_PATH=/models/warden_knn.pkl
      - CONFIDENCE_THRESHOLD=0.7
      - LLM_DOUBT_THRESHOLD=0.5

  llm-analyzer:
    # Claude/GPT para casos inciertos
    environment:
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
      - MAX_DAILY_LLM_CALLS=500

  dashboard:
    # Monitoreo en tiempo real
    ports:
      - "8000:8000"

  postgres:
    # Datos de entrenamiento, predicciones, log de auditoría
    volumes:
      - pgdata:/var/lib/postgresql/data
```

---

## 7.7 Principios de Diseño Clave

1. **ML primero, LLM segundo** — ML es rápido y barato. LLM es lento y caro. Usar LLM solo para dudas.
2. **Consciente de la confianza** — Nunca confiar en una clasificación sin saber qué tan segura es.
3. **Siempre aprendiendo** — Cada duda resuelta hace el sistema mejor.
4. **Humano en el ciclo** — El LLM propone, el humano confirma. Sin decisiones autónomas no supervisadas en acciones críticas.
5. **Pipeline dual** — Paquetes de red Y requests web. Diferentes características, misma arquitectura.
6. **Listo para producción** — Docker, PostgreSQL, logging estructurado, dashboard.

---

*Siguiente: [Capítulo 8 — Estático vs Adaptativo →](08-static-vs-adaptive.md)*
