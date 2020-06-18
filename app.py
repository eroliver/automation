from pathlib import Path
import os
import tkinter as tk
import send2trash as send2trash
#import win64com.shell.shell as shell

# C:\Users\eoliver\Downloads
#users = []
#for user in users:
 #   append()

# files = ['C:\Users\eoliver\Downloads']
# os.system('"runas /user:USERNAME "C:/Python27/python.exe shell.py""')
downloads = Path('C:/Users/eoliver/Downloads/BackupJobSummaryReport_2020-06-17-08-00-08.pdf')
# os.remove(downloads)
#os.remove(downloads)
downloads_modified = os.path.getmtime(downloads)
print(downloads_modified)