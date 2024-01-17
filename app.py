from pathlib import Path
from time import ctime
import os
import shutil
import sys

# type in the path of whatever folder you are trying to transfer files from
# this can be a folder from your computer, an external hard drive, whatever...
source = Path(r"C:\Users\brian\OneDrive\Pictures\Camera Roll")
# type in the path of whatever folder you want your folders/files to be sent to and organized
target = Path(r"D:\TransferTest")


def source_check(s):
    check = s.exists()
    if check is False:
        sys.exit(
            "Source folder NOT present/exists. Change source var to an existing folder path.")
    print("Source folder found!")


def create_folder():
    os.chdir(source)
    for folder in source.iterdir():
        if folder.is_dir() is True:
            time = ctime(folder.stat().st_ctime)
            day = time[8:10]
            month = time[4:7]
            year = time[20:]
            name = folder.stem
            new = f"{day}{month}{year}_{name}"
            print(folder)
            print(new)


def file_trans():
    print("Standby")


source_check(source)
create_folder()
