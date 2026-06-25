import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    order_count = orders.groupby('customer_number').agg(
        no_of_orders = ('order_number','count')
    ).reset_index()
    return order_count.sort_values('no_of_orders',ascending=False)[['customer_number']].head(1)