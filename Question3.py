import os.path
import glob
name=r"C:\Users\Shreya\check"
def directory_list(name):
    max_size=0
    file_name=""
    size=0
    lst=glob.glob(f"{name}"+"\\*")
    for item in lst:
        if os.path.isdir(item):
            direc_items=glob.glob(f"{item}"+"\\*")
            for it in direc_items:
                if os.path.isfile(it):
                        size=os.path.getsize(f"{it}")
                        if max_size<size:
                            max_size=size
                            file_name=file_name+os.path.basename(f"{it}")
                else:
                        directory_list(it)    
        else:
            size=os.path.getsize(f"{item}")
            if max_size<size:
                max_size=size
                file_name=file_name+os.path.basename(f"{item}")
    print(max_size)
    print(file_name)
directory_list(name)


        
    
    

