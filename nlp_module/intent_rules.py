def get_intent(text):
    if "time" in text:
        return "time"
    elif "hello" in text or "hi" in text:
        return "greeting"
    elif "name" in text:
        return "name"
    else:
        return "unknown"