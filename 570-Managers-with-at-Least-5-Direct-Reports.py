import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    r=employee['managerId'].value_counts()
    v=r[r>=5].index
    res=employee[employee['id'].isin(v)][['name']]
    return res
    