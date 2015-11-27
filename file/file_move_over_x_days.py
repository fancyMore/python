# -*- coding: UTF-8 -*-
# -*Application Start*-
import shutil, sys, os, time
src = 'D:/overFiles/test'
dst = 'D:/overFiles/backup'
now = time.time()
time_line = now - 20*86400
for f in os.listdir(src):
    path = os.path.join(src,f)
    if os.stat(path).st_mtime < time_line:
        if os.path.isfile(path):
            shutil.move(path, dst)
# -*Application End*-

'''
@shutil 高级文件操作模块
'''
'''
@usage
备份过期20天的文件
'''