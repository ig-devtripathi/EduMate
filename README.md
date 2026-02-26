  <img src="https://via.placeholder.com/150x150.png?text=EduMate+Logo" alt="EduMate Logo" width="150"/>
  <h1>📚 EduMate</h1>
  <p><strong>Intelligent AI Learning Platform & Academic Tutor</strong></p>
  <p>
    <a href="https://streamlit.io/"><img src="https://img.shields.io/badge/Framework-Streamlit-FF4B4B.svg?style=flat&logo=Streamlit" alt="Streamlit"></a>
    <a href="https://ai.google.dev/"><img src="https://img.shields.io/badge/AI_Engine-Gemini_2.5_Flash-4285F4.svg?style=flat&logo=google" alt="Google Gemini"></a>
    <a href="https://python.org"><img src="https://img.shields.io/badge/Python-3.11+-3776AB.svg?style=flat&logo=python" alt="Python"></a>
  </p>
</div>

---

## 📖 Project Overview

**EduMate** is a production-grade, AI-powered academic learning hub engineered to provide students with a deeply interactive, highly restricted, and intelligent tutoring experience. Built on **Streamlit** and powered by a dual-engine architecture prioritizing the **Google Gemini REST API** with a seamless **Groq (Llama 3) fallback**. EduMate functions as a comprehensive study companion—capable of analyzing multimodal documents, generating structured quizzes, summarizing dense notes, and breaking down complex concepts.

The application features a bespoke **Antigravity Glassmorphism UI**, delivering a premium, immersive, and modern visual experience rarely seen in standard data applications.

---

## ✨ Key Features

### 1. 🎓 Ask EduMate (Strict Academic Tutor)
A multimodal, conversational AI tutor designed explicitly for academic learning.
- **Multimodal Uploads**: Solves doubts directly from uploaded PDFs, DOCX files, and Images.
- **Academic Guardrails**: Strictly programmed to reject non-academic queries (politics, casual chat, etc.) to maintain a focused learning environment.
- **Human-like Encouragement**: Responses are structured with a supportive, pedagogical tone ("Let's break this down step-by-step").
- **Identity Protection**: Masked backend engine; the system identifies uniquely as "Ask EduMate".

### 2. 🧠 Concept Explainer
Deconstructs difficult academic topics into easily digestible explanations.
- **Dynamic Difficulty**: Supports targeted audience framing, including *ELI5 (Explain Like I'm 5)*, *High School Level*, *College Level*, and *Expert*.
- **Custom Prompts**: Allows users to define custom explanation constraints (e.g., "Explain using video game analogies").

### 3. 📝 Note Summarizer
An intelligent text processor that condenses lengthy, dense lecture or reading notes into highly optimized, study-ready bullet points.

### 4. 🎯 Quiz Generator
An automated assessment engine.
- **Structured JSON Output**: Uses forced JSON parsing logic to reliably generate 5-10 question multiple-choice quizzes (MCQs).
- **Interactive Scoring**: Evaluates user answers dynamically, providing real-time scores and detailed explanations for incorrect choices.

### 5. 📄 Document Analyzer
A robust document interrogation tool.
- Upload any standard academic document (PDF, Word) or diagram (JPG/PNG).
- Query the document context directly for summaries, specific data points, or conceptual breakdowns.

---

## 🏗️ Architecture & System Design

EduMate operates on a lightweight, highly efficient serverless-style architecture leveraging Streamlit's reactive execution model.

1. **Frontend Layer (Streamlit + Custom CSS)**: Handles UI rendering, state management (`st.session_state`), and file uploads. Features a globally synced `api_locked` state to prevent race conditions or double-fire API calls during asynchronous generation.
2. **Integration Layer (Python)**: Utilizes `PyPDF2` and `python-docx` for local binary extraction. Extracts text payloads before transmitting to the LLM to reduce token latency.
3. **AI Engine (Dual-Route HTTP REST)**: Direct HTTP REST integration (`requests`) with Google Gemini 2.5 Flash as the primary engine. If Gemini hits quota limits, the system transparently reroutes the payload to `llama-3.3-70b-versatile` (Groq), guaranteeing 100% uptime without alerting the user.

### Why Direct REST API?
Integrating via direct REST endpoints rather than standard SDK wrappers provides granular control over timeout configurations, payload construction, and allows for seamless engine-switching (Gemini -> Groq) by trapping raw 429 Quota errors before they reach the UI.

---

## 💻 Tech Stack

- **Frontend**: Streamlit
- **Styling**: Custom CSS (Premium Glassmorphism Design System)
- **Backend / LLM Bridge**: Google Gemini REST API (Primary) + Groq API (Fallback)
- **Document Processing**: `PyPDF2` (PDF Parsing), `python-docx` (Word Parsing), `Pillow` (Image Processing)
- **Environment Management**: `python-dotenv`
- **Network**: `requests`

---

## 📂 Project Structure

```text
E:\ANTIGRAVITY\EDUMATE
|   .env
|   app.py
|   README.md
|   requirements.txt
|
+---pages
|       1_Concept_Explainer.py
|       2_Note_Summarizer.py
|       3_Quiz_Generator.py
|       4_Document_Analyzer.py
|       5_Ask_EduMate.py
|
\---utils
        ai_service.py
        file_utils.py
        theme.py
```

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.11 or higher
- A valid Google Gemini API Key

### Step-by-Step Guide

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/EduMate.git
   cd EduMate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**
   Create a `.env` file in the root directory and add your secret API keys:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Launch the Application**
   ```bash
   streamlit run app.py
   ```

---

## 🛡️ Robust Error & API Rate Limit Handling

EduMate is built for production resilience:
- **Sticky Error States**: Uses a global `st.session_state.app_error` mechanism to catch transient backend exceptions and survive Streamlit's aggressive `st.rerun()` lifecycle, ensuring errors are highly visible to users.
- **Rate Limit Trapping**: Intercepts raw JSON dumps during API 429 (Quota Exceeded) events, instantly cleanly unlocking the UI and presenting a human-readable "System Error: API rate limit exceeded" toast.
- **Button Locking**: Employs global state locking (`disabled=True`) across all 5 tools to prevent concurrent API saturation from impatient users.

---

## 🌐 Deployment (Streamlit Cloud)

EduMate is optimized for 1-click deployment on Streamlit Community Cloud:
1. Push your repository to GitHub.
2. Log into [Streamlit Cloud](https://share.streamlit.io/).
3. Create a new app, link your GitHub repository, and select `app.py` as the entry point.
4. Go to **Advanced Settings > Secrets** and input your environment variables:
   ```toml
   GEMINI_API_KEY="your_api_key_here"
   GROQ_API_KEY="your_groq_key_here"
   ```
5. Deploy!

---

## 📸 Screenshots

*(Add screenshots of your UI here)*
- `[Screenshot 1: Main Dashboard / Glassmorphism UI]`
- `[Screenshot 2: Ask EduMate interacting with an uploaded PDF]`
- `[Screenshot 3: Dynamic Quiz Generation]`

---

## 🔮 Future Enhancements (Roadmap)
- **Vector Database Integration (RAG)**: Implement FAISS or ChromaDB to allow students to query entire textbook libraries rather than single-context uploads.
- **Authentication System**: Firebase integration for user accounts to save generated quizzes and session histories.
- **Export Functionality**: Allow 1-click PDF exporting of generated Note Summaries and Quiz results.

---

## 💎 Why This Project is Unique
EduMate bridges the gap between raw LLM wrappers and polished EdTech platforms. Instead of exposing a generic chat interface, it strictly controls the AI's identity, heavily structures output (like forced JSON for quizzes), and wraps the entire experience in a modern, state-of-the-art UI with robust error-handling safeguards.

---

## 📄 Resume Description Snippet

> **EduMate – AI Academic Tutor & Learning Platform**
> *Engineered a multimodal web application leveraging Streamlit and the Google Gemini HTTP REST API to assist students with dynamic note summarization, structured JSON quiz generation, and targeted concept explanations. Architected a custom "Antigravity Glassmorphism" UI and implemented robust concurrency locks and rate-limit interceptors (`st.session_state`) to handle API timeouts and prevent memory leaks. Integrated PyPDF2 and python-docx for seamless document interrogation.*

---

## 📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👨‍💻 Developer
Developed by **Devraj Tripathi**.

---
*If you like this project, please leave a star! ⭐*
