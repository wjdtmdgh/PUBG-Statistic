import pandas as pd
from .constant import *

def load_dataset(match_type):
    df = pd.read_csv(FILE_PATH)
    print(f"{FILE_PATH} successfully loadded")

    all_col_names = df.columns.tolist()
    col_names = list(filter(lambda x: x.startswith(column_prefix[match_type]), all_col_names))

    return df.loc[:, df.columns.isin(col_names)]
