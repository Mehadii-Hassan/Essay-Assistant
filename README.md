<h1 align="center">📝 Essay Assistant</h1> 

<p align="center">
  <strong>AI-powered Web Tool for Structured Essay Writing </strong><br>
  Built with <code>FastAPI</code>, <code>OpenAI</code>, and <code>HTML/CSS</code>
</p>

<hr>

<h2>📌 Project Overview</h2>

<p>
Essay Assistant is a web-based AI tool that generates well-structured essays in simple and fluent language.  
It helps users produce essays with key sections such as <strong>Introduction</strong>, <strong>Necessity</strong>, <strong>Advantages</strong>, <strong>Disadvantages</strong>, and <strong>Conclusion</strong>.  
The backend is powered by <strong>FastAPI</strong> and <strong>OpenAI</strong>, while the frontend is styled using clean and responsive HTML/CSS.
</p>

<ul>
  <li>✍️ AI-generated essays with 5–10 paragraphs</li>
  <li>⚡ Responsive and user-friendly web interface</li>
  <li>🔗 Cross-origin enabled for smooth frontend-backend communication</li>
  <li>🧩 Extendable and easy to customize</li>
</ul>

<hr>

<h2>🚀 Features</h2>

<ul>
  <li>📑 Enter any topic to generate an essay</li>
  <li>🤖 AI-powered structured content</li>
  <li>🎨 Beautiful, minimal frontend with HTML/CSS</li>
  <li>🔧 Backend powered by FastAPI + OpenAI</li>
</ul>

<hr>

<h2>🛠️ Tech Stack</h2>

| Technology | Purpose                          |
|------------|----------------------------------|
| FastAPI    | Backend server and API routing   |
| OpenAI API | AI-powered essay generation      |
| dotenv     | Environment variable management  |

<hr>

<h2>🧠 How It Works</h2>

<ol>
  <li>User enters a topic</li>
  <li>FastAPI backend calls the <code>generate_essay()</code> function</li>
  <li>OpenAI API generates a detailed essay with structured sections</li>
  <li>Essay is returned and displayed instantly</li>
</ol>

<hr>

<h2>📂 Folder Structure</h2>

<pre>
essay-assistant/
│
├── essay_assistant.py   ← Core logic for AI essay generation
├── fast_api.py          ← FastAPI backend and API routes
├── requirements.txt     ← Dependencies
├── .env                 ← Environment variables
└── README.md            ← Project documentation
</pre>

<hr>

<h2>⚙️ Setup Instructions</h2>

<ol>
  <li>Clone the repository</li>

  <pre><code>git clone https://github.com/yourusername/essay-assistant.git
cd essay-assistant</code></pre>

  <li>Create and activate a virtual environment</li>

  <pre><code>
python -m venv venv
# For Linux/Mac:
source venv/bin/activate
# For Windows:
venv\Scripts\activate
  </code></pre>

  <li>Install dependencies</li>

  <pre><code>pip install -r requirements.txt</code></pre>

  <li>Configure your <code>.env</code> file</li>

  <pre><code>
BASE_URL=https://api.openai.com/v1
API_KEY=your_openai_api_key
MODEL_NAME=gpt-4   # or your preferred model
  </code></pre>

  <li>Run the project</li>

  <pre><code>uvicorn fast_api:app --reload</code></pre>
</ol>

<hr>

<h2>🧪 Example Usage</h2>

<ul>
  <li><code>Topic: Importance of Education</code> → Generates a full essay with Introduction, Necessity, Advantages, Disadvantages, Conclusion</li>
  <li><code>Topic: Climate Change</code> → Generates an essay covering multiple structured sections</li>
</ul>

<hr>

<h2>🙌 Credits</h2>

<p>
Created by <strong>Mehadi Hassan</strong> using FastAPI + OpenAI + HTML/CSS.
</p>

<hr>

<p align="center">⭐ Star this repo if you find it useful!</p>

