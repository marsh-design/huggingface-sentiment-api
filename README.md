# Sentiment Analysis API (Hugging Face + FastAPI + Docker)

This project is a containerized inference service built using FastAPI and Hugging Face Transformers. It exposes a simple `/predict` endpoint that returns sentiment predictions for text inputs. The API is served using Uvicorn and designed to handle multiple parallel requests, validated through simulation in a Jupyter notebook.

## 🧠 Model

The model used is [`distilbert-base-uncased-finetuned-sst-2-english`](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english), a fast and lightweight sentiment classifier pre-trained on SST-2.

I chose this model for its:
- ✅ Low latency
- ✅ Small footprint
- ✅ Relevance for real-time user feedback analysis

## 🧰 Tech Stack

- `FastAPI` – Web API framework
- `Uvicorn` – ASGI server supporting async and concurrency
- `Transformers` – Model loading and inference (Hugging Face)
- `Docker` – Containerization
- `Jupyter Notebook` – Testing parallel requests

---

## 🚀 How to Run

### 1. Build the container

```bash
docker build -t huggingface-api .

### 💡 Scaling & Production Notes

This demo uses Uvicorn to serve the API within a single Docker container — enough to support concurrent requests for this task.  

In a production environment, I would consider the following upgrades:

- **Gunicorn + multiple Uvicorn workers** for parallelism on multi-core systems
- **NGINX** for load balancing, SSL termination, and reverse proxying
- **Structured request logging** and **Prometheus/Grafana** for observability
- **Input validation, authentication**, and rate limiting for security
- **Model caching or batching** if latency or cost were concerns