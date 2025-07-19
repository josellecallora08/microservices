# 🧠 AI Microservices Backend – Showcase Project

This project demonstrates a modular microservice architecture for AI tasks using **FastAPI**, **Docker**, and **Groq's blazing-fast LLMs**.

Each microservice handles a distinct AI-related task — including transcription, summarization, and classification — all running independently and deployed via Render.

---

## 🚀 Services Overview

| Service        | Description                                       | Powered by         |
|----------------|---------------------------------------------------|---------------------|
| **Transcribe** | Converts audio files to text                      | Whisper via Groq    |
| **Summarize**  | Summarizes long text or transcripts               | LLaMA-3 via Groq    |
| **Classify**   | Classifies text into predefined categories        | LLaMA-3 via Groq    |

---

## 🌐 Live API Endpoints (Deployed on Render)

| Service         | Endpoint URL                                             | Method | Description                       |
|-----------------|----------------------------------------------------------|--------|-----------------------------------|
| 🎙 Transcribe    | [`/transcribe`](https://microservices-t0t5.onrender.com/transcribe)  | `POST` | Upload an audio file → text       |
| ✂️ Summarize     | [`/summarize`](https://summarizer-0vgx.onrender.com/summarize)      | `POST` | Summarize long text               |
| 🏷 Classify      | [`/classify`](https://classifier-lph7.onrender.com/classify)        | `POST` | Classify a user message or text   |

---

## 📦 Requirements

- Docker + Docker Compose
- Groq API key (https://console.groq.com)

---

## 🛠 Setup Instructions (Local)

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/ai-microservices.git
cd ai-microservices
