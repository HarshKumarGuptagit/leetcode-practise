import pandas as pd
import datetime as dt

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather['prev_temp'] = weather.sort_values('recordDate',ascending=True)[['temperature']].shift(1)
    weather['prev_act_recordDate'] = weather.sort_values('recordDate',ascending=True)[['recordDate']].shift(1)
    weather['prev_exp_recordDate'] = weather['recordDate'] - timedelta(days=1)

    # final_df = pd.merge(weather,

    return weather[(weather.prev_act_recordDate==weather.prev_exp_recordDate) & (weather.temperature >weather.prev_temp)][['id']]