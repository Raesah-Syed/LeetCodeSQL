import pandas as pd

def bank_account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    transactions['transacted_on']=pd.to_datetime(transactions['transacted_on'])
    g=transactions.merge(users, left_on='paid_by', right_on='user_id', how='right')
    g['amount']=-g['amount']
    t=transactions.merge(users, left_on='paid_to',right_on='user_id', how='right')
    m=pd.concat((t[['user_id','transacted_on','amount']],g[['user_id','transacted_on','amount']]))
    m.sort_values(by='transacted_on')
    m['amount'] = m['amount'].fillna(0)
    m['credit'] = m.groupby('user_id')['amount'].cumsum()
    s = m.groupby('user_id', as_index=False).last()
    res=s.merge(users, on='user_id')
    res['credit']=res['credit_x']+res['credit_y']
    res['credit_limit_breached']=numpy.where(res['credit']<0,'Yes','No')
    return (res[['user_id','user_name','credit','credit_limit_breached']])