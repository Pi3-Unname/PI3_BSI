from typing import Set
import pandas as pd

def replace_values(df: pd.DataFrame,Key: str, values: Set):
  for keys, value in values.items():
    df[Key].loc[df[Key] == keys] = value
