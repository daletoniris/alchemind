# Lab Environment Setup

## Minimal Requirements

- **Python**: 3.10+
- **Docker**: 20+ (optional, recommended)
- **RAM**: 4GB minimum
- **GPU**: Not required (all labs run on CPU)

---

## Option 1: Docker (Recommended)

```bash
cd labs
docker compose up -d

# Access Jupyter at http://localhost:8888
# PostgreSQL available at localhost:5432
```

## Option 2: Manual Setup

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Start Jupyter
jupyter notebook
```

## Option 3: Google Colab

Each lab includes a Colab-compatible notebook. Click the "Open in Colab" badge at the top of each lab's README.

---

## Dependencies

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

## Verify Installation

```python
import sklearn
import pandas as pd
import numpy as np

print(f"scikit-learn: {sklearn.__version__}")
print(f"pandas: {pd.__version__}")
print(f"numpy: {np.__version__}")
print("✅ Ready for Alchemind labs!")
```
