🎙️ AI Voice Assistant using ML & NLP

A simple Machine Learning-based Voice Assistant built using Python that can understand voice commands and perform basic tasks like telling time, opening applications, and responding to user queries.

📌 Description

A Machine Learning-based Voice Assistant with a simple Flask-based web interface that allows users to interact through voice commands directly from the browser.

It processes speech input, predicts user intent using ML, and responds with voice output, combining NLP + ML + Web Interface in one project.

🚀 Features
🎤 Voice command input
🔊 Text-to-speech response
🌐 Flask web interface (browser-based)
⏰ Current time & date
📂 Open applications
🧠 ML-based intent recognition
💬 NLP command processing
🛠️ Tech Stack
Backend: Python
Frontend: Flask (HTML, basic UI)
Libraries:
speech_recognition
pyttsx3
scikit-learn
datetime
os
json
📁 Project Structure
VoiceAssistant/
│── data/
│   └── dataset.json
│
│── model/
│   └── model.pkl
│
│── templates/
│   └── index.html
│
│── static/
│   └── style.css
│
│── app.py          # Flask app
│── main.py         # Core assistant logic
│── train_model.py
│── utils.py
│── README.md
⚙️ Setup
git clone https://github.com/your-username/voice-assistant-ml.git
cd voice-assistant-ml
pip install speechrecognition pyttsx3 scikit-learn flask
python app.py
🌐 Running the Web App
Start server:
python app.py
Open browser:
http://127.0.0.1:5000
Click button → Speak → Get response 🎤
🧠 How It Works
User interacts via Flask web UI
Voice input is captured
Speech → text conversion
ML model predicts intent
Action is executed
Response returned as voice + text
📊 Dataset Sample
{
  "intent": "time",
  "patterns": ["what time is it", "tell me time"],
  "responses": ["The current time is"]
}
▶️ Demo
User: What is the time?
Assistant: The current time is 10:45 AM

User: Open Chrome
Assistant: Opening Chrome

User: Hello
Assistant: Hello! How can I help you?
<img width="998" height="694" alt="image" src="https://github.com/user-attachments/assets/56956c82-053a-460e-a7db-fabeb8b684ff" />
<img width="843" height="680" alt="image" src="https://github.com/user-attachments/assets/daf5ddc5-a555-47f7-ab47-004a743d5e0d" />

📈 Results
✔️ Browser-based interaction using Flask
✔️ Fast response (~1–2 sec)
✔️ Works offline
✔️ Clean UI + ML integration
⚠️ Limitations
Limited dataset
Basic UI (can be improved)
Noise sensitivity
🔮 Future Improvements
Better UI (React / advanced frontend)
Cloud deployment (AWS)
LLM integration
Multi-language support
📜 License

MIT License

🧑‍💻 Author

Arshad Kabir
📧 arshadkabir174@gmail.com
