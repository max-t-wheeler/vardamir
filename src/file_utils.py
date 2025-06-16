from pathlib import PosixPath
from zipfile import ZipFile

def summarize_zip_contents(zip_file_path: PosixPath) -> None:
  with ZipFile(zip_file_path) as zip_file:
    for zip_info in zip_file.infolist():
      print(zip_info.filename)
      print(f'File Size: {zip_info.file_size * 1e-6} MB')
      print(f'Compressed File Size: {zip_info.compress_size * 1e-6} MB')

      print()
