import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    all_products= len(product.product_key.unique())
    setup = customer.groupby('customer_id').agg(
        no_of_products = ('product_key','nunique')
    ).reset_index()

    return setup[(setup.no_of_products == all_products)][['customer_id']]