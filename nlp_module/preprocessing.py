import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def preprocess(text):
    tokens = word_tokenize(text)
    words = [w for w in tokens if w.lower() not in stopwords.words('english')]
    return words