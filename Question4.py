import os.path
import glob
from glob import fnmatch
file_name=""
name=r"."
path=r".\demo.txt"
def directory_list(name):
    lst=glob.glob(f"{name}"+"\\*")
    for item in lst:
        if os.path.isdir(item):
            directory_list(item)    
        else:
            if fnmatch.fnmatch(os.path.basename(f"{item}"),"*.txt"):
                with open(item,"rt") as f1:
                    lines = f1.readlines()
                    with open(path, "at") as f2:
                        f2.writelines(lines)
directory_list(name)
