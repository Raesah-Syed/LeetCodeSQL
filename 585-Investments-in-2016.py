import pandas as pd



def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    # 1. Have the same tiv_2015 value as one or more other policyholders
    cond1 = insurance['tiv_2015'].duplicated(keep=False)
    
    # 2. Are not located in the same city as any other policyholder (unique lat, lon pairs)
    cond2 = ~insurance.duplicated(subset=['lat', 'lon'], keep=False)
    
    # Filter rows meeting both conditions
    filtered = insurance[cond1 & cond2]
    
    # Sum tiv_2016 and round to 2 decimal places in a DataFrame
    total_tiv = filtered['tiv_2016'].sum()
    
    return pd.DataFrame({'tiv_2016': [round(total_tiv, 2)]})
    print (l)
    