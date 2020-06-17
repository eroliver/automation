from pathlib import Path
import os
import sys
import win64com.shell.shell as shell

# C:\Users\eoliver\Downloads
#users = []
#for user in users:
 #   append()

# files = ['C:\Users\eoliver\Downloads']

downloads = Path('C:/Users/eoliver/Downloads')
os.remove(downloads)
