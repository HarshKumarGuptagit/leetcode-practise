import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    result = pd.merge(employee,employee,left_on='managerId',right_on='id',how='left',suffixes=('','_manager'))
    return result[(result.salary>result.salary_manager)][['name']].rename(columns={'name':'Employee'})