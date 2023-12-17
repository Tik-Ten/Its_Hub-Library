from shutil import copy
from sys import argv
src = r"src/Its_Hub.py"
dst = argv[1] # Python libraries address
dst = rf"{dst}"
print("dst = " + dst)
print("Start copying...")
copy(src, dst)
print("Copy ended. Now, you can use Its_Hub library :)")