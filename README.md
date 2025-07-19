# 🧠 AI Microservices Backend – Showcase Project

This project demonstrates a modular microservice architecture for AI tasks using **FastAPI**, **Docker**, and **Groq's blazing-fast LLMs**.

Each microservice handles a distinct AI-related task — including transcription, summarization, classification, and secure authentication.

---

## 🚀 Services Overview

| Service        | Port | Description                                       | Powered by         |
|----------------|------|---------------------------------------------------|---------------------|
| **Auth**       | 8004 | JWT-based user authentication                     | FastAPI + JWT       |
| **Transcribe** | 8001 | Converts audio files to text                      | Whisper via Groq    |
| **Summarize**  | 8002 | Summarizes long text or transcripts               | LLaMA-3 via Groq    |
| **Classify**   | 8003 | Classifies text into predefined categories        | LLaMA-3 via Groq    |

---

## 📦 Requirements

- Docker + Docker Compose
- Groq API key (https://console.groq.com)
- (Optional) OpenAI key if you want to compare outputs

---

## 🛠 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/ai-microservices.git
cd ai-microservices

