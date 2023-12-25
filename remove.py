from sys import argv
from os import remove
dst = argv[1] # Python libraries address
dst = rf"{dst}"
dst = dst + "/Its_Hub.py"
print("dst: " + dst)
remove(dst)
print("Remove completed.")