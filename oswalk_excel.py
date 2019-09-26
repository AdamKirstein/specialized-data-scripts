import os
from os.path import join, getsize
import fnmatch as fn


# the files follow the format YYYY-MM-DD Report Name.xlsx, so self.name refers to Report Name.
# we append the date to the name later in the process.

def get_latest_report(self, report_dir):
    file_list = []
    for file in os.listdir(report_dir):
        if fn.fnmatch(file, "*{}*".format(self.name)):
            file_date = file.split(" ")[0]
            timestamp = os.path.getmtime(os.path.join(report_dir,file))
            file_list.append([file_date, timestamp, file])
        else:
            pass
    s = sorted(file_list, key= lambda x:[x[0], x[1]], reverse = True)
    last_mod = s[0]
    last_modified_file = os.path.join(report_dir, last_mod)
    print("LAST MODIFIED FILE: {}".format(last_mod))
    return last_modified_file 

# fails if report_dir is empty
# we need to move up one directory and search recursively through the files for all files that match the pattern
# we can use os.walk: https://docs.python.org/3/library/os.html#os.walk

# something like...

# for root, dirs, files in os.walk(directory above report dir):
#	for f in files:
        # if fn.fnmatch(file, "*{}*".format(self.name)):
            # file_date = file.split(" ")[0]
            # timestamp = os.path.getmtime(os.path.join(report_dir,file))
            # file_list.append([file_date, timestamp, file])
        # else:
            # pass

rootdir= r"C:\Users\Adam\Desktop\get_latest_dir"
filepath=[]
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        print(file.split(" ")[0])
        #print(os.path.join(subdir, file))
        #filepath.append(subdir + os.sep + file)
