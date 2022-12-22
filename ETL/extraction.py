import numpy as np
import pandas as pd
import json
import requests
from datetime import datetime, timedelta

import dataloader
import helper
import pyodbc

fetchdate = datetime.strftime(datetime.today() - timedelta(days=1), '%m_%d_%Y')
cstring = helper.get_connstring()
apikey = helper.get_apikey()

def getMovieIds():
    return pd.read_json(f'http://files.tmdb.org/p/exports/movie_ids_{fetchdate}.json.gz', lines=True)
    
def getPersonIds():
    return pd.read_json(f'http://files.tmdb.org/p/exports/person_ids_{fetchdate}.json.gz', lines=True)
    
def getCompanyIds():
    return pd.read_json(f'http://files.tmdb.org/p/exports/production_company_ids_{fetchdate}.json.gz', lines=True)
    
def getKeywordIds():
    return pd.read_json(f'http://files.tmdb.org/p/exports/keyword_ids_{fetchdate}.json.gz', lines=True)
    
def getCollectionIds():
    return pd.read_json(f'http://files.tmdb.org/p/exports/collection_ids_{fetchdate}.json.gz', lines=True)
    
def getTVSeriesIds():
    return pd.read_json(f'http://files.tmdb.org/p/exports/tv_series_ids_{fetchdate}.json.gz', lines=True)
    
def getTVNetworkIds():
    return pd.read_json(f'http://files.tmdb.org/p/exports/tv_network_ids_{fetchdate}.json.gz', lines=True)


def getGenres():
    dataurl = f'https://api.themoviedb.org/3/genre/movie/list?api_key={apikey}'
    data = json.loads(requests.get(dataurl).text)
    genres = pd.DataFrame.from_dict(data['genres'])
    return genres


def getMoviesRaw():
    with pyodbc.connect(cstring) as conn:
        # query = "select id from movieids"
        query = "select id from movieids where id not in (select id from moviesraw)"
        ids = pd.read_sql(query, conn)
        
        
    for chunk in np.array_split(ids['id'], len(ids)//500 + 1):
        session = requests.Session()
        df_movies = None 
        dfs=[]
        for i in chunk:
            dataurl = f'https://api.themoviedb.org/3/movie/{i}?api_key={apikey}'
            data = json.loads(session.get(dataurl, stream=False).text)
            df = pd.json_normalize(data)
            dfs.append(df)
        
        df_movies = pd.concat(dfs)
        df_movies = df_movies[['adult', 'backdrop_path', 'budget', 'genres', 'homepage', 'id',
                                'imdb_id', 'original_language', 'original_title', 'overview',
                                'popularity', 'poster_path', 'production_companies',
                                'production_countries', 'release_date', 'revenue', 'runtime',
                                'spoken_languages', 'status', 'tagline', 'title', 'video',
                                'vote_average', 'vote_count', 'belongs_to_collection.id']]

        df_movies.dropna(subset=['id'], axis=0, inplace=True)
        df_movies['id'] = pd.to_numeric(df_movies.id, errors='coerce').astype('int')
        df_movies['genres'] = df_movies['genres'].astype('str')
        df_movies['production_companies'] = df_movies['production_companies'].astype('str')
        df_movies['production_countries'] = df_movies['production_countries'].astype('str')
        df_movies['spoken_languages'] = df_movies['spoken_languages'].astype('str')
        
        df_movies['vote_average'] = pd.to_numeric(df_movies.vote_average, errors='coerce')
        df_movies['popularity'] = pd.to_numeric(df_movies.popularity, errors='coerce')
        df_movies['adult'] = df_movies['adult'].astype('bool')
        df_movies['video'] = df_movies['video'].astype('bool')
        
        dataloader.inc_load_with_index(df=df_movies, tbl="MoviesRaw", fastexecute=False)
        session.close()



def extractAlltoDB():
    print("Getting MovieIds")
    with pyodbc.connect(cstring) as conn:
        query = "select id from movieids"
        dbmovieids = pd.read_sql(query, conn)
        movieids = getMovieIds()
        movieids = movieids.query("id not in @dbmovieids['id']")
    if movieids.shape[0] >0:
        print(f"Dumping {movieids.shape[0]} records into MovieIds table")
        dataloader.inc_load_with_index(df=movieids, tbl="MovieIds",)
    else:
        print("No additional movie ids found")
    
    
    print("Getting Genres")
    with pyodbc.connect(cstring) as conn:
        query = "select id from Genres"
        dbgenres = pd.read_sql(query, conn)
        genres = getGenres()
        genres = genres.query("id not in @dbgenres['id']")       
    if genres.shape[0] > 0:
        print(f"Dumping {genres.shape[0]} records into Genres table")
        dataloader.inc_load_with_index(df=genres, tbl="Genres",)
    else:
        print("No addition genres found")
        
    
    print("Getting PersonIds")
    with pyodbc.connect(cstring) as conn:
        query = "select id from Persons"
        dbpersonids = pd.read_sql(query, conn)
        personids = getPersonIds()
        personids = personids.query("id not in @dbpersonids['id']")
    if personids.shape[0]>0:
        print(f"Dumping {personids.shape[0]} records into Persons table")
        dataloader.inc_load_with_index(df=personids, tbl="Persons",)
    else:
        print("No additional person ids found")
    
    print("Getting CompanyIds")
    with pyodbc.connect(cstring) as conn:
        query = "select id from Companies"
        dbcompanyids = pd.read_sql(query, conn)
        companyids = getCompanyIds()
        companyids = companyids.query("id not in @dbcompanyids['id']")
    if companyids.shape[0]>0:
        print(f"Dumping {companyids.shape[0]} records into Companies table")
        dataloader.inc_load_with_index(df=companyids, tbl="Companies",)
    else:
        print("No additional company ids found")
    
    print("Getting CollectionIds")
    with pyodbc.connect(cstring) as conn:
        query = "select id from Collections"
        dbcollectionids = pd.read_sql(query, conn)
        collectionids = getCollectionIds()
        collectionids = collectionids.query("id not in @dbcollectionids['id']")
    if collectionids.shape[0]>0:
        print(f"Dumping {collectionids.shape[0]} records into Collections table")
        dataloader.inc_load_with_index(df=collectionids, tbl="Collections",)
    else:
        print("No additional collection ids found")
    


