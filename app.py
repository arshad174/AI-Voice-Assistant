from flask import Flask, render_template, request, jsonify
import pickle
import datetime
import re

app = Flask(__name__)

# Load model
model, vectorizer = pickle.load(open("ml_module/model.pkl", "rb"))

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    return text

def predict(text):
    text = clean_text(text)
    X = vectorizer.transform([text])
    intent = model.predict(X)[0]
    return intent

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]

    intent = predict(user_input)

    if intent == "time":
        response = str(datetime.datetime.now())
    elif intent == "greeting":
        response = "Hello! How can I help you?"
    elif intent == "name":
        response = "I am your ML Assistant"
    else:
        response = "I didn't understand"

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)