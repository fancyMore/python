# -*- coding: UTF-8 -*-
# -*Application Start*-
import os
import sys

directory = sys.argv[1]
dir_size = 0
for (path, dirs, files) in os.walk(directory):
    print dirs
    for file in files:
        print file
        filename = os.path.join(path, file)
        dir_size += os.path.getsize(filename)
print "Folder Size in Bytes = %0.2f Bytes" % (dir_size)
print "Folder Size in Kilobytes = %0.2f KB" % (dir_size / 1024.0)
print "Folder Size in Megabytes = %0.2f MB" % (dir_size / 1024 / 1024.0)
print "Folder Size in Gigabytes = %0.2f GB" % (dir_size / 1024 / 1024 / 1024.0)
# -*Application End*-

'''
@os.walk
@return 三元tupple(dirpath, dirnames, filenames)
@pram
dirpath是一个string，代表目录的路径,
dirnames是一个list，包含了dirpath下所有子目录的名字,
filenames是一个list，包含了非目录文件的名字.这些名字不包含路径信息,如果需要得到全路径,需要使用 os.path.join(dirpath, name).
'''
'''
@usage
python dir_size.py D:\batch\fancy
'''
