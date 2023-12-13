import os
import shutil

base = os.getcwd()    
shutil.copy(base + '\\sqlite_original.db', base + '\\sqlite.db')