# Question-6:
# #MaxFile class 
# from pkg.file import File 
# fs = File(".")
# fs.getMaxSizeFile(2) # gives two max file names 
# fs.getLatestFiles(datetime.date(2018,2,1))
# #Returns list of files after 1st Feb 2018 

import os
import datetime
from typing import List
class File:
    def __init__(self, directory: str):
        self.directory = directory
    def getMaxSizeFile(self, n: int) -> List[str]:
        files = []
        for file in os.listdir(self.directory):
            file_path = os.path.join(self.directory, file)
            if os.path.isfile(file_path):
                file_size = os.path.getsize(file_path)
                files.append((file, file_size))
        files.sort(key=lambda x: x[1], reverse=True)
        return [file[0] for file in files[:n]]

    def getLatestFiles(self, after_date: datetime.date) -> List[str]:
        latest_files = []
        for file in os.listdir(self.directory):
            file_path = os.path.join(self.directory, file)
            if os.path.isfile(file_path):
                file_mod_time = os.path.getmtime(file_path)
                file_mod_date = datetime.date.fromtimestamp(file_mod_time)
                if file_mod_date > after_date:
                    latest_files.append(file)
        return latest_files
fs = File(".")
print(fs.getMaxSizeFile(2))  # Get the two largest files in the current directory
print(fs.getLatestFiles(datetime.date(2018, 2, 1))) 


