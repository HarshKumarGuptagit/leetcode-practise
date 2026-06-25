import pandas as pd

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions['is_approved'] = np.where(
        transactions.state == 'approved',1,0
    )
    transactions['month'] = pd.to_datetime(transactions['trans_date']).dt.strftime('%Y-%m')
    return transactions.assign(
        approved_amount = (transactions.amount * transactions.is_approved).fillna(0)
    ).groupby(['month','country'],dropna=False).agg(
        trans_count = ('id','count'),
        approved_count = ('is_approved','sum'),
        trans_total_amount = ('amount','sum'),
        approved_total_amount = ('approved_amount','sum')
    ).reset_index()