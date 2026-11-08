import pandas as pd

def cumulative_salary(employee: pd.DataFrame) -> pd.DataFrame:
    max_month = employee.groupby('id')['month'].transform('max')
    rows = employee[employee['month'] < max_month]

    merged = rows.merge(employee, on='id', suffixes=('', '_2'))

    merged = merged[
        (merged['month_2'] >= merged['month'] - 2) &
        (merged['month_2'] <= merged['month'])
    ]

    result = (
        merged.groupby(['id', 'month'], as_index=False)['salary_2']
        .sum()
        .rename(columns={'salary_2': 'Salary'})
    )

    return result.sort_values(['id', 'month'], ascending=[True, False]).reset_index(drop=True)