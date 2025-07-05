from pathlib import PosixPath
from zipfile import ZipFile

import pandas as pd

def get_zip_content_summary(zip_file_path: PosixPath) -> pd.DataFrame:
  zip_file_names = []
  zip_file_sizes = []
  zip_file_compress_sizes = []

  with ZipFile(zip_file_path) as zip_file:
    for zip_info in zip_file.infolist():
      zip_file_names.append(zip_info.filename)
      zip_file_sizes.append(zip_info.file_size)
      zip_file_compress_sizes.append(zip_info.compress_size)

  dataframe = pd.DataFrame({
      'file_name': zip_file_names,
      'file_size': zip_file_sizes,
      'file_compress_size': zip_file_compress_sizes
  })

  dataframe['file_size_mb'] = dataframe['file_size'].apply(lambda x: f'{x * 1e-6} MB')
  dataframe['file_comress_size_mb'] = dataframe['file_compress_size'].apply(lambda x: f'{x * 1e-6} MB')

  return dataframe