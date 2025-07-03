import os

from google.colab import drive

def mount_google_drive(file_path: str='/content/drive', remount: bool=False) -> None:
    if remount or os.environ.get('google_drive_mounted') is None:
        drive.mount(file_path)
        os.environ['google_drive_mounted'] = 'true'
