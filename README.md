# Apartment Valuation API (FastAPI)

Simple Python API that serves a mock regression model for apartment valuation.

## Run
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn src.main:app --reload
