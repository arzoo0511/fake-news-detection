import pandas as pd
import re

def clean_text(text):
    text = re.sub(r'\W', ' ', text)       # Remove special characters
    text = re.sub(r'\s+', ' ', text)      # Remove extra spaces
    return text.lower()

def load_and_preprocess(path):
    data = pd.read_csv(path)
    data['text'] = data['text'].apply(clean_text)
    return data

