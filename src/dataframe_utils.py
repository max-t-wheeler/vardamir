import pandas as pd

def convert_to_date(data: pd.DataFrame, column: str) -> pd.Series:
  data[column] = pd.to_datetime(data[column], errors='coerce').dt.date

def drop_empty_records(data: pd.DataFrame, subset: list=None) -> None:
  data.dropna(how='all', subset=subset, inplace=True)
  data.reset_index(drop=True, inplace=True)
