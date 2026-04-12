import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv("cleaned_fake_news.csv")


df = df.dropna()

X_text = df["content"]  
vectorizer = TfidfVectorizer(
    max_features=5000,
    stop_words='english',
    ngram_range=(1,2)
)


X = vectorizer.fit_transform(X_text)


y = df["label"]

print("Shape des vecteurs :", X.shape)
