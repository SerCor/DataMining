'''
    Escribe un dataframe en un archivo con formato arff
'''
import pandas as pd
from typing import List, Dict, Union
from io import TextIOWrapper

AttributeType = Union[List[str], str]
AttributesDescription = Dict[str, AttributeType]


def write_definition(fp: TextIOWrapper, attrs_description: AttributesDescription) -> None:
    for column, atype in attrs_description.items():
        if not isinstance(atype, str):
            atype = '{ ' + ','.join(map(str, atype)) + ' }'
        fp.write(f'@attribute {column} {atype}\n')


def write_data(fp: TextIOWrapper, df: pd.DataFrame) -> None:
    fp.write('@data\n')
    for index, row in df.iterrows():
        fp.write(','.join(map(str, row)) + '\n')


def get_attributes_types(df: pd.DataFrame) -> AttributesDescription:
    return {k: df[k].unique() if v == 'object' else 'numeric' for k, v in df.dtypes.items()}


def to_arff(path: str, df: pd.DataFrame, attrs_description: AttributesDescription, relation: str) -> None:
    with open(path, encoding='utf-8', mode='w') as fp:
        fp.write(f'@relation {relation}\n\n')
        write_definition(fp, attrs_description)
        write_data(fp, df)
