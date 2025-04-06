
# 📄 Project Document: Real-Time Sentiment Analysis System

## 📌 Project Title  
**Real-Time Sentiment Analysis System**

## 🎯 Objective  
To build a real-time pipeline that captures streaming text data (e.g., tweets), applies machine learning-based sentiment analysis, and exposes predictions via an API. The system should be scalable, containerized, and ready for integration into real-world applications like customer feedback monitoring or social media analysis.

---

## 🧱 Architecture Overview

```
[Tweet Stream/API]
       ↓
┌───────────────────┐
│   Kafka Producer   │ ← Simulates tweet stream
└───────────────────┘
       ↓
┌───────────────────┐
│    Kafka Topic     │ ← Message queue
└───────────────────┘
       ↓
┌─────────────────────────┐
│ Kafka Consumer + ML Model│ ← Sentiment prediction
└─────────────────────────┘
       ↓
┌───────────────────┐
│   FastAPI Server   │ ← API for serving predictions
└───────────────────┘
       ↓
     [Client/UI]
```

---

## 🧰 Tech Stack

| Tool           | Purpose                              |
|----------------|--------------------------------------|
| Python         | Core development                     |
| Apache Kafka   | Real-time message streaming          |
| kafka-python   | Kafka producer/consumer integration  |
| Scikit-learn   | Machine Learning model               |
| FastAPI        | Web microservice framework           |
| Docker         | Containerization                     |
| Tweepy (opt.)  | Twitter API access                   |

---

## 🗂️ Folder Structure

```
real-time-sentiment/
├── docker-compose.yml
├── kafka/
│   ├── producer.py
│   └── consumer.py
├── model/
│   ├── train_model.py
│   ├── vectorizer.pkl
│   └── sentiment_model.pkl
├── app/
│   └── main.py
├── requirements.txt
└── README.md
```

---

## 🛠️ Implementation Steps

### 1. Train Sentiment Model
- Use `scikit-learn` to train a simple sentiment classifier (e.g., Naive Bayes).
- Save the model and vectorizer as `.pkl` files for inference.

### 2. Kafka Producer
- Simulate incoming tweets using a Python Kafka producer.
- Send messages to a Kafka topic (`sentiment-topic`).

### 3. Kafka Consumer with ML
- Set up a Kafka consumer that listens to the `sentiment-topic`.
- On receiving a message, use the trained model to predict sentiment.

### 4. FastAPI Microservice
- Create an API endpoint (`/predict`) that accepts text input.
- Return the predicted sentiment as a JSON response.

### 5. Docker Compose Setup
- Use Docker Compose to orchestrate Kafka, Zookeeper, and the FastAPI service.
- Enable modular and scalable deployment.

---

## 🧪 Testing & Validation

- Run the Kafka producer to send test messages.
- Validate consumer logs to see predicted outputs.
- Access `http://localhost:8000/predict?text=I+love+this` to test the API response.

---

## 🚀 Optional Enhancements

- Live tweet ingestion using Twitter API (`tweepy`)
- Store predictions in PostgreSQL or MongoDB
- Visualize sentiment trends in a dashboard (e.g., Plotly Dash)
- Add monitoring via Grafana and Prometheus

---

## 📄 Summary

This project demonstrates a production-style real-time sentiment analysis system using Python, Kafka, and FastAPI. It combines core data engineering practices (streaming, messaging, deployment) with ML deployment and is ideal for portfolio showcasing or real-world implementation in domains like e-commerce, logistics, or social analytics.
