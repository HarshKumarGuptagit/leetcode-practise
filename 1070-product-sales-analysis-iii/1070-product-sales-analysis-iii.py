import pandas as pd

def sales_analysis(sales: pd.DataFrame) -> pd.DataFrame:
    sales['product_year_rank'] = sales.groupby('product_id')['year'].rank(method = 'dense',ascending=True)
    # return sales[sales.product_year_rank == 1].groupby(['product_id','year']).agg(
    #     quantity = ('quantity','sum'),
    #     price = ('price','sum'),
    # ).reset_index().rename(columns={'year':'first_year'})
    return sales[sales.product_year_rank == 1][['product_id','year','quantity','price']].rename(columns={'year':'first_year'})