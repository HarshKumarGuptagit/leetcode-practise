import pandas as pd

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    stadium['people_1'] = stadium.sort_values('id',ascending=True)['people'].shift(-1)
    stadium['people_2'] = stadium.sort_values('id',ascending=True)['people'].shift(-2)
    stadium['people_1_back'] = stadium.sort_values('id',ascending=True)['people'].shift(1)
    stadium['people_2_back'] = stadium.sort_values('id',ascending=True)['people'].shift(2)

    return stadium[
        ((stadium['people']>=100) & (stadium['people_1']>=100) & (stadium['people_2']>=100)) |
        ((stadium['people']>=100) & (stadium['people_1_back']>=100) & (stadium['people_2_back']>=100))|
        ((stadium['people']>=100) & (stadium['people_1_back']>=100) & (stadium['people_1']>=100))
        ].sort_values('visit_date').drop(columns= ['people_1','people_2','people_1_back','people_2_back'])