# Tira – AI Voice Assistant 🤖

Tira is a Python-based AI voice assistant that allows users to interact through voice commands and receive intelligent responses. It uses Cohere's AI model for generating responses and integrates speech recognition and text-to-speech technologies to provide an interactive voice-based experience.

## ✨ Features

- **AI-Powered Conversations:** Generates intelligent responses using the Cohere API.
- **Voice Recognition:** Converts spoken commands into text using Speech Recognition.
- **Text-to-Speech:** Responds to users through voice output using pyttsx3.
- **Wikipedia Search:** Retrieves short summaries of topics from Wikipedia.
- **Website Navigation:** Opens Google and YouTube through voice commands.
- **Time-Based Greetings:** Greets users according to the current time of day.
- **Exit Commands:** Supports voice commands such as stop, quit, exit, and goodbye.
- **Real-Time Responses:** Streams AI-generated responses and speaks them sentence by sentence.

## 🛠️ Technologies Used

- Python
- Cohere API
- SpeechRecognition
- PyAudio
- pyttsx3
- Wikipedia API
- Regular Expressions
- Webbrowser Module

## 📁 Project Structure

```text
AI_Chatbot/
│
├── Chatbot.py
├── README.md
└── .gitignore
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/mihikajain03/AI_Chatbot.git
```

### 2. Navigate to the Project Folder

```bash
cd AI_Chatbot
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install Required Libraries

```bash
pip install cohere pyttsx3 SpeechRecognition PyAudio wikipedia
```

Note: PyAudio installation may require additional system dependencies depending on your Python and Windows setup.

### 6. Configure the Cohere API Key

Obtain an API key from the Cohere platform.

Set the API key in PowerShell:

```powershell
$env:COHERE_API_KEY = "your-api-key"
```

Replace `your-api-key` with your actual API key.

**Important:** Never upload your API key to GitHub.

### 7. Run the Project

```bash
python Chatbot.py
```

## 🎤 Example Voice Commands

| Voice Command | Action |
|---|---|
| Open Google | Opens Google |
| Open YouTube | Opens YouTube |
| Search Wikipedia Python | Retrieves a Wikipedia summary |
| What is Artificial Intelligence? | Generates an AI response |
| Goodbye | Exits the assistant |

## 🔐 Environment Variables

| Variable | Description |
|---|---|
| `COHERE_API_KEY` | API key required to access the Cohere AI service |

## 🚀 Future Improvements

- Add support for more voice commands.
- Improve speech recognition accuracy.
- Introduce a graphical user interface (GUI).
- Add support for multiple languages.
- Integrate additional AI capabilities.

## 👩‍💻 Author

Developed as a Python-based AI Voice Assistant project.
