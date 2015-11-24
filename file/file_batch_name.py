# -*- coding: UTF-8 -*-
# -*Application Start*-
import os															# Load the library module
import sys															# Load the library module

work_dir=sys.argv[1]											# Set the variable work_dir with the first argument passed
old_ext=sys.argv[2]											# Set the variable work_dir with the first argument passed
new_ext=sys.argv[3]											# Set the variable work_dir with the first argument passed

files = os.listdir(work_dir)									# Set the variable files, by listing everything in the directory
for filename in files:											# Loop through the files
  file_ext = os.path.splitext(filename)[1]				# Get the file extension
  if old_ext == file_ext:										# Start of the logic to check the file extensions, if old_ext = file_ext
    newfile = filename.replace(old_ext, new_ext)	    # Set newfile to be the filename, replaced with the new extension
    os.rename(													# Write the files
	    os.path.join(work_dir, filename),
		os.path.join(work_dir, newfile))
# -*Application End*-

'''
@usage
python file_batch_name.py D:\batch .txt .html
'''