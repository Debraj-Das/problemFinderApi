import joblib
from sklearn.metrics.pairwise import cosine_similarity
from pathlib import Path
import os
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
matrix_path = os.path.join(BASE_DIR, 'atcoder/preprocess/matrix.pkl')
vectorizer_path = os.path.join(BASE_DIR, 'atcoder/preprocess/vectorizer.pkl')
data = os.path.join(BASE_DIR, 'atcoder/preprocess/problem.csv')

df = pd.read_csv(data)
QName = df['Name'].values
QLink = df['URL'].values


vectorizer = joblib.load(vectorizer_path)
tfidf_matrix = joblib.load(matrix_path)


def query(q):
    query_vector = vectorizer.transform([q.lower()])
    similarity_scores = cosine_similarity(tfidf_matrix, query_vector)
    sorted_indices = similarity_scores.argsort(axis=0)[::-1].squeeze()

    results = []

    for i in sorted_indices:
        if (similarity_scores[i] >= 0.01):
            results.append({
                "name": QName[i],
                "url": QLink[i],
                "score": round(float(similarity_scores[i][0]), 3),
            })

    return results
