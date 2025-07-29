# 📝 Essay Assistant

Essay Assistant is a web-based AI tool that generates well-structured essays in simple and fluent language. Built with FastAPI, OpenAI, and HTML/CSS, this assistant helps users quickly produce essays with key sections like **Introduction**, **Necessity**, **Advantages**, **Disadvantages**, and **Conclusion**.

## 🚀 Features

- Generate essays by entering any topic
- AI-powered content with a minimum of 5–10 paragraphs
- Beautiful, clean web UI
- Responsive and user-friendly interface
- Cross-origin enabled for frontend communication

## 🛠️ Tech Stack

| Technology | Purpose                          |
|------------|----------------------------------|
| FastAPI    | Backend server and API routing   |
| HTML/CSS   | Frontend UI design               |
| OpenAI API | AI-powered essay generation      |
| dotenv     | Environment variable management  |

## 📁 Project Structure
essay-assistant/ ├── essay_assistant.py # Core logic for AI essay generation ├── fast_api.py # FastAPI backend and API routes ├── index.html # Web-based frontend interface ├── .env # Environment variables for API settings

## 📄 How It Works

1. User enters a topic into the input field.
2. On clicking **Generate Essay**, the frontend sends a POST request to `/generate`.
3. FastAPI receives the request and calls the `generate_essay()` function.
4. OpenAI’s API responds with a detailed essay.
5. The essay appears instantly in the frontend.

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/essay-assistant.git
cd essay-assistant
BASE_URL=https://api.openai.com/v1
API_KEY=your_openai_api_key
MODEL_NAME=gpt-4  # or your preferred model

pip install fastapi uvicorn python-dotenv openai

uvicorn fast_api:app --reload
