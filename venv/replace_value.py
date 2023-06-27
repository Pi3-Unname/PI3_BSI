from typing import Set
import pandas as pd

def replace_values(df: pd.DataFrame, values: Set):
  for key, value in values.items():
    df['APR Risk of Mortality'].loc[df['APR Risk of Mortality'] == key] = value
