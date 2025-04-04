import os.path
import glob
from glob import fnmatch
file_name=""
name=r"C:\Users\Shreya\check"
path=r"C:\Users\Shreya\demo.txt"
def directory_list(name):
    lst=glob.glob(f"{name}"+"\\*")
    for item in lst:
        if os.path.isdir(item):
            directory_list(item)    
        else:
            if fnmatch.fnmatch(os.path.basename(f"{item}"),"*.txt"):
                with open(path,"wt") as f:
                    print(os.path.basename(f"{item}"))
                    f.writelines(os.path.basename(f"{item}"))
directory_list(name)
