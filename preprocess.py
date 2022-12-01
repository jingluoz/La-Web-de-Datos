import pandas as pd
import ast

archivo = 'movies_metadata.csv'
df = pd.read_csv(archivo)

deleted_columns = ['genres', 'production_companies', 'production_countries' ,'adult', 'belongs_to_collection', 'homepage', 'imdb_id', 'overview','poster_path', 'spoken_languages', 'tagline', 'video', 'runtime','original_title', 'status']

df = df.drop(deleted_columns, axis=1)

df = df[pd.to_numeric(df['id'], errors='coerce').notnull()]
df = df[pd.to_numeric(df['popularity'], errors='coerce').notnull()]

def json_to_string(column, row, index):
    if (pd.isnull(row[column])):
        df.at[index, column] = []
    else:
        y = ast.literal_eval(row[column])
        aux = []
        for j in y:
            aux.append(j['name'])
        df.at[index, column] = aux

for i, r in df.iterrows():
    df.at[i, 'title'] = r['title'].lower().replace(' ', '_')
    if(int(r['vote_average'])!=0):
        df.at[i, "budget_over_rating"] = int(r['budget'])/int(r['vote_average'])
    df.at[i, "budget_over_rating"] = 0

df.to_csv("post.csv",index=False)