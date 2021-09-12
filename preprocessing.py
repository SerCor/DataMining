'''
    Elimina el one hot encoding en las columnas
        - weekday_{day} | is_weekend
        - data_channel_is_{channel}
    Y las convierte en una respectiva columna
        - weekday {monday, tuesday, wednesday, thursday, friday, saturday, sunday, weekend} 
        - channel {lifestyle, entertainment, bus, socmed, tech, world, nA}
'''
import pandas as pd
from typing import List


def first_value_one(cols, s):
    for col in cols:
        if s[col] == 1.0:
            return col

    if 'data_channel_is_bus' in cols:  # Solo deberia faltar algun valor en los cols channel
        return pd.NA


def drop_cols(df: pd.DataFrame, cols: List[str]) -> pd.DataFrame:
    return df.drop(cols, axis=1)


def normalize(df: pd.DataFrame) -> pd.DataFrame:
    week_days_cols = [*[f'weekday_is_{d}' for d in ['monday', 'tuesday', 'wednesday', 'thursday',
                                                    'friday', 'saturday', 'sunday']], *['is_weekend']]
    channel_cols = [f'data_channel_is_{c}' for c in [
        'lifestyle', 'entertainment', 'bus', 'socmed', 'tech', 'world']]
    df['weekday'] = ''
    df['channel'] = ''

    for index, row in df.iterrows():
        day = first_value_one(week_days_cols, row).replace('weekday_is_', '')
        channel = first_value_one(
            channel_cols, row)

        # Puede ser que el registro no tenga un valor asignado (channel = NaN)
        if isinstance(channel, str):
            channel = channel.replace('data_channel_is_', '')

        df.loc[index, 'weekday'] = day
        df.loc[index, 'channel'] = channel

    return drop_cols(df, [*week_days_cols, *channel_cols])
