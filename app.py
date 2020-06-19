from pathlib import Path
import os
import time
import tkinter as tk
import send2trash as send2trash
#import win64com.shell.shell as shell

# C:\Users\eoliver\Downloads
#users = []
#for user in users:
 #   append()

# files = ['C:\Users\eoliver\Downloads']
# os.system('"runas /user:USERNAME "C:/Python27/python.exe shell.py""')
# downloads = Path('C:/Users/eoliver/Downloads/BackupJobSummaryReport_2020-06-17-08-00-08.pdf')
# os.remove(downloads)
#os.remove(downloads)
# downloads_modified = os.path.getmtime(downloads)
# print(downloads_modified)


def clear_old_downloads():
    base_path = 'C:/Users/eoliver/Downloads/'
    with os.scandir(base_path) as entries:
        for entry in entries:
            if entry.is_file() and os.path.getmtime(entry) < time.time() - 31536000:
                print(entry.name)
                os.remove(base_path+entry.name)


# add check for multiple drives and users
def clear_old_recycle_bin():
    base_path = 'C:/$Recycle.Bin/'
    with os.scandir(base_path) as entries:
        for entry in entries:
            if entry.is_file() and os.path.getmtime(entry) < time.time() - 15768000:
                print(entry.name)
                os.remove(base_path + entry.name)


def clear_old_recycle_bin_desktop():
    base_path = 'C:/Users/eoliver/Desktop/'
    with os.scandir(base_path) as entries:
        for entry in entries:
            if entry.is_file() and os.path.getmtime(entry) < time.time() - 100:
                print(entry.name)
                # os.remove(base_path + entry.name)


clear_old_recycle_bin_desktop()