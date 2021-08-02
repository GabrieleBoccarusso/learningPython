'''
basic examples on how to navigate the current directory

Gabriele Boccarusso 2.8.2021 
'''
from datetime import datetime
import os

def display_cwd():
    cwd = os.getcwd()
    print(f"Current Working Directory: {cwd}")

def up_one_dir_level(): # takes us on an upper level of the directory
    os.chdir("../")


def format_datetime(timestamp):
    utc_timestamp = datetime.utcfromtimestamp(timestamp)
    formated_date = utc_timestamp.strftime("%d %b %Y %H %M %S")
    return formated_date

def display_dir_entries(dir):
    #scandir gives us more information than listdir
    with os.scandir(dir) as entries:
        for entry in entries:
            print(entry.name)
            info = entry.stat()
            print(f"\tCreation time: {format_datetime(info.st_ctime)}")
            print(f"\tLast access time: {format_datetime(info.st_atime)}")
            print(f"\tSize: {info.st_size} bytes")


def display_dirs(dir):
    with os.scandir(dir) as entries:
        for entry in entries:
            if entry.is_dir():
                print(f"Directory name: {entry.name}")

def display_files(dir):
    with os.scandir(dir) as entries:
        for entry in entries:
            if entry.is_file():
                print(f"File name: {entry.name}")

if __name__ == "__main__":
    # display_dir_entries('../')
    display_dirs("../")
    display_files("../GUI")