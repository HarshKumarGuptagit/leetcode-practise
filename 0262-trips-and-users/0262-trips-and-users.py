import pandas as pd
import numpy as np 
def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    legit_users = users[users.banned == "No"].users_id.unique()
    trips = trips[(trips.client_id.isin(legit_users)) & (trips.driver_id.isin(legit_users)) & 
    (trips.request_at.between("2013-01-01","2013-10-03"))
    ]
    
    summary_table = trips.assign(
        cancel_transactions = np.where(
            trips['status'].str.contains('cancelled'), 1, 0
        )
    ).groupby('request_at').agg(
        day_cancellations = ('cancel_transactions','sum'),
        day_total_transactions = ('id','count')
    ).reset_index()
    
    summary_table["Cancellation Rate"] = (summary_table.day_cancellations/summary_table.day_total_transactions).round(2)
    
    return summary_table[['request_at','Cancellation Rate']].rename(columns = {'request_at':'Day'})