import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    r = cinema[(cinema['id'] % 2 != 0) & (cinema['description'] != 'boring')]
    x = r.sort_values(by='rating', ascending=False)
    return x