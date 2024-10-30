import pandas as pd

df = pd.read_csv('problem.csv')

df['Name'] = df['Name'].apply(lambda x: x.strip().replace(
    '\n', ' ').replace('-', ' ').replace('$', ' '))
df['URL'] = df['URL'].apply(lambda x: x.strip())
df['Text'] = df['Text'].apply(
    lambda x: str(x).strip().replace('-', ' ').replace('$', ' '))

df.to_csv('problem.csv', index=False)
