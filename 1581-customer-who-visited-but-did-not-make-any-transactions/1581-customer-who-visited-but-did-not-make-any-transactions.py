import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    result = pd.merge(visits,transactions, on = "visit_id",how="left")
    return result[(result.amount.isna())].groupby('customer_id').agg(
        count_no_trans = ('visit_id','count')
    ).reset_index()
    