import pandas as pd
import datetime as dt
def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    master_table = pd.merge(movie_rating, movies, on='movie_id', how='left').merge(users,on='user_id',how='left')
    master_table['created_at'] = pd.to_datetime(master_table['created_at'])

    user_rating = master_table.groupby(['user_id','name']).movie_id.count().reset_index(name="movie_counts").sort_values(['movie_counts','name'],ascending=[False,True])[['name']].head(1).rename(columns={'name':'results'})
    
    movie_rating = master_table[(master_table.created_at.dt.strftime("%Y-%m") == "2020-02")].groupby(['movie_id','title']).rating.mean().reset_index(name="avg_rating").sort_values(['avg_rating','title'],ascending=[False,True])[['title']].head(1).rename(columns={'title':'results'})
    
    final_result = pd.DataFrame([],columns=['results'])
    final_results = pd.concat([user_rating,movie_rating],ignore_index=True) 
    return final_results