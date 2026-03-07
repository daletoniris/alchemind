# Configuración del Entorno de Laboratorio

## Requisitos Mínimos

- **Python**: 3.10+
- **Docker**: 20+ (opcional, recomendado)
- **RAM**: 4GB mínimo
- **GPU**: No requerida (todos los labs corren en CPU)

---

## Opción 1: Docker (Recomendado)

```bash
cd labs
docker compose up -d

# Acceder a Jupyter en http://localhost:8888
# PostgreSQL disponible en localhost:5432
```

## Opción 2: Configuración Manual

```bash
# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Instalar dependencias
pip install -r requirements.txt

# Iniciar Jupyter
jupyter notebook
```

## Opción 3: Google Colab

Cada lab incluye un notebook compatible con Colab. Hacé clic en el badge "Open in Colab" en la parte superior del README de cada lab.

---

## Dependencias

```
scikit-learn>=1.3.0
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
jupyter>=1.0.0
flask>=3.0.0
requests>=2.31.0
```

---

## Verificar Instalación

```python
import sklearn
import pandas as pd
import numpy as np

print(f"scikit-learn: {sklearn.__version__}")
print(f"pandas: {pd.__version__}")
print(f"numpy: {np.__version__}")
print("Listo para los labs de Alchemind!")
```
