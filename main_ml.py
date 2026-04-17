from ml_module.predict import predict
from speech.text_to_speech import speak
from speech.speech_to_text import listen
import datetime

while True:
    text = listen()

    intent, confidence = predict(text)

    print("Intent:", intent, "Confidence:", confidence)

    if confidence < 0.5:
        speak("I am not sure, can you rephrase?")
        continue

    if intent == "time":
        speak(str(datetime.datetime.now()))

    elif intent == "greeting":
        speak("Hello! How can I help you?")

    elif intent == "name":
        speak("I am your intelligent assistant")

    else:
        speak("I am still learning, try something else")