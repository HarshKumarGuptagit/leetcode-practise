import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:

    # tiv_2015 appears more than once
    repeated_tiv = insurance.groupby("tiv_2015")["pid"].transform("count") > 1

    # location appears exactly once
    unique_location = insurance.groupby(["lat", "lon"])["pid"].transform("count") == 1

    ans = insurance.loc[
        repeated_tiv & unique_location,
        "tiv_2016"
    ].sum()

    return pd.DataFrame({"tiv_2016": [round(ans, 2)]})