import numpy as np
import pandas as pd
from ast import literal_eval

import helper
import extraction

cstring = helper.get_connstring()

def tranformData():
    rawmovies = extraction.getRawMovies()
    if not rawmovies:
        return
    
    df_movies = rawmovies[[
            'id', 'original_language', 'original_title', 'overview', 'adult',
            'backdrop_path', 'budget', 'homepage', 'imdb_id', 'popularity',
            'poster_path', 'release_date', 'revenue', 'runtime', 'status',
            'tagline', 'title', 'video', 'vote_average', 'vote_count',
            'belongs_to_collection.id'
        ]]
    df_movies = (
        df_movies
        .assign(
            release_date=lambda x: pd.to_datetime(x['release_date'].replace({0: np.NaN})).dt.normalize(), 
            )
        )
    
    
    df_genres = rawmovies[['id', 'genres']]
    df_genres = (
        df_genres.assign(genres = lambda x: x['genres'].apply(lambda x: literal_eval(x)))
        .explode('genres')
        .dropna()
        .assign(genres = lambda x: x['genres'].apply(lambda y: y['id']))
        .rename(columns={'id':'movieid', 'genres': 'genreid'})
        .drop_duplicates()
        )   
    
    
    df_companies = rawmovies[['id', 'production_companies']]
    df_companies = (
    df_companies.assign(production_companies = lambda x: x['production_companies'].apply(lambda x: literal_eval(str(x))))
        .explode('production_companies')
        .dropna()
        .assign(production_companies = lambda x: x['production_companies'].apply(lambda y: y['id']))
        .rename(columns={'id':'movieid', 'production_companies': 'productioncompanyid'})
        .drop_duplicates()
        )
    
    
    df_countries= rawmovies[['id', 'production_countries']]
    df_countries=(
    df_countries.assign(production_countries = lambda x: x['production_countries'].apply(lambda x: literal_eval(str(x))))
        .explode('production_countries')
        .dropna()
        .assign(production_countries = lambda x: x['production_countries'].apply(lambda y: y['name']))
        .rename(columns={'id':'movieid', 'production_countries':'productioncountry'})
        .drop_duplicates()
        )
    
    
    df_spoken = rawmovies[['id', 'spoken_languages']]
    df_spoken= (
    df_spoken.assign(spoken_languages = lambda x: x['spoken_languages'].apply(lambda x: literal_eval(str(x))))
        .explode('spoken_languages')
        .dropna()
        .assign(spoken_languages = lambda x: x['spoken_languages'].apply(lambda y: y['english_name']))
        .rename(columns={'id':'movieid', 'spoken_languages':'spokenlanguage'})
        .drop_duplicates()
        )
    
    return (df_movies, df_genres, df_companies, df_countries, df_spoken)