import pandas as pd

def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    mo=movie_rating.groupby(["user_id"]).agg(tr=('rating','count')).reset_index()
    m=mo.merge(users, on="user_id")
    r=m.sort_values(by=["tr","name"], ascending=[False,True])
    
    movie_rating["created_at"]=pd.to_datetime(movie_rating["created_at"])
    x=movie_rating[movie_rating["created_at"].between('2020-02-01','2020-02-29')]
    xr=x.groupby(["movie_id"]).agg(ar=('rating','mean')).reset_index()
    mr=xr.merge(movies, on="movie_id").reset_index()
    sr=mr.sort_values(by=["ar","title"], ascending=[False,True])
    
    pdo=pd.concat([r["name"][:1], sr["title"][:1]], ignore_index=False)
    result = pd.DataFrame({"results": [r["name"].iloc[0], sr["title"].iloc[0]]})
    return result

    