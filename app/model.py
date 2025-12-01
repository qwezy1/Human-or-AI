import pandas as pd
import nltk
import os
import joblib
from nltk.tokenize import sent_tokenize, word_tokenize
import numpy as np

import nltk

nltk.download('punkt')
nltk.download('punkt_tab')



nltk.download('punkt')

# Загружаем модель безопасно относительно этого файла
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
model = joblib.load(model_path)

label_map = {1: "AI-generated", 0: "Human-written"}

def extract_stylo_features(text):
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    avg_sent_len = np.mean([len(word_tokenize(s)) for s in sentences]) if sentences else 0
    sent_len_var = np.var([len(word_tokenize(s)) for s in sentences]) if sentences else 0
    ttr = len(set(words)) / len(words) if words else 0
    markdown_bold = text.count("**")
    return pd.Series({
        "avg_sent_len": avg_sent_len,
        "sent_len_var": sent_len_var,
        "ttr": ttr,
        "markdown_bold": markdown_bold
    })

def predict_class(text: str):
    df_sample = pd.DataFrame([{
        "text": text,
        **extract_stylo_features(text)
    }])
    pred = model.predict(df_sample)[0]
    proba = model.predict_proba(df_sample)[0][1]
    confidence = proba if pred == 1 else 1 - proba
    return {
        "prediction": label_map[pred],
        "confidence": round(float(confidence), 3)
    }
