# Apartment Valuation API (FastAPI)

Simple Python API that serves a mock regression model for apartment valuation.

## Run locally (without Docker)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload

Open:
http://localhost:8000

http://localhost:8000/docs

## Run with Docker (reproducible environment)

docker build -t apartment-api .

Run one instance:
docker run -p 8000:8000 apartment-api

Run two instances on different ports:
docker run -p 8000:8000 apartment-api
docker run -p 8001:8000 apartment-api

Open:
http://localhost:8000/docs

http://localhost:8001/docs