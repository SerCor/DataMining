'''
    Crea k particiones
'''

import argparse
import pandas as pd
from typing import List, Tuple, Iterable
import numpy as np
from pprint import pprint


Partition = pd.DataFrame
ValidationFragment = Tuple[Partition, Partition]


def shuffle_df(df: pd.DataFrame) -> pd.DataFrame:
    return df.sample(frac=1)


def split_df(df: pd.DataFrame, k: int) -> List[Partition]:
    return np.array_split(df, k)


def split_dataset(df: pd.DataFrame, k: int, class_col: str) -> List[ValidationFragment]:
    classes = df[class_col].unique()
    df_per_class = {c: shuffle_df(df[df[class_col] == c]) for c in classes}
    splits_per_class = {c: split_df(df, k=k)
                        for c, df in df_per_class.items()}
    partitions_groups = list(zip(*splits_per_class.values()))
    partitions = list(map(pd.concat, partitions_groups))
    validation_steps = []

    for pindex, partition in enumerate(partitions):
        validation_steps.append(
            [pd.concat([*partitions[:pindex], *partitions[pindex+1:]]), partition])

    return validation_steps
