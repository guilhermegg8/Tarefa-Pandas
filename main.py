import pandas as pd 
import ast


movies = pd.read_csv('tmdb_5000_credits.csv')

print(movies.head())

print(movies[['title', 'cast']])

def exibir_atores_filmes(movies, num_filmes=20):
    for i in range(num_filmes):
        title = movies['title'][i]
        cast = ast.literal_eval(movies['cast'][i])
        print(f"{title} | {cast[0]['name']}")

exibir_atores_filmes(movies)