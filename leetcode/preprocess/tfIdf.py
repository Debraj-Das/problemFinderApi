import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

df = pd.read_csv('problem.csv')
names = df['Name'].values
urls = df['URL'].values
texts = df['Text'].values
n = len(names)

data = []
for i in range(n):
    name = 4*(names[i] + " ")
    text = str(texts[i])
    data.append(name + text.lower())


vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(data)

joblib.dump(tfidf_matrix, 'matrix.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')
