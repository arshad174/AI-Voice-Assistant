import pickle

model, vectorizer = pickle.load(open("ml_module/model.pkl", "rb"))

def predict(text):
    X = vectorizer.transform([text])
    
    probs = model.predict_proba(X)
    confidence = max(probs[0])

    intent = model.predict(X)[0]

    return intent, confidence