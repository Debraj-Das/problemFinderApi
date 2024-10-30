import joblib
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('problem.csv')
QName = df['Name'].values
QLink = df['URL'].values


vectorizer = joblib.load('vectorizer.pkl')
tfidf_matrix = joblib.load('matrix.pkl')

query = "tree and graph"

query_vector = vectorizer.transform([query.lower()])
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

print(results)
