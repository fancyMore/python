# -*- coding: UTF-8 -*-
# -*Application Start*-

import os, errno, shutil, time, re
tmp = os.popen('git diff bf7e430 273b240 --name-only').readlines()
length = len(tmp)
dest = 'E:/work/git_berbon/bb_static' #git diff 目录
backdir = 'F:/git_back'  #diff 文件备份目录
winrar = 'F:/git_rar'    #diff 文件压缩目录

def mkdir_p(path):
    dirpath = backdir + path
    if  not os.path.exists(dirpath):
        try:
            os.makedirs(backdir + path)
            return backdir + path
        except OSError as exc: # Python >2.5 (except OSError, exc: for Python <2.5)
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else: raise
    else :
      return dirpath
        
def get_file_base_name(fpath):
    return os.path.basename(fpath).replace("\n","")
    
def get_file_base_path(dpath):
    return os.path.dirname(dpath)

#不能处理同名文件  
def find_file(start, name):
    for relpath, dirs, files in os.walk(start):
        if name in files:
            full_path = os.path.join(start, relpath, name)
            return os.path.normpath(os.path.abspath(full_path))

#fixed

def find_file(start,name,filter):
    listpath = [start] 
    filename = name 
    result = []
    while True: 
        try: 
            path = listpath.pop() 
        except IndexError: 
            break 
        for i in os.listdir(path): 
            abspath = os.path.join(path,i) 
            if i[0] == '.': 
                continue 
            if i == filename:
                catch = re.search(filter.replace('/','').replace("\n",""), abspath.replace('\\',''))
                if catch:
                    return abspath
                else :
                    continue
            if os.path.isdir(abspath): 
                listpath.append(abspath) 

def copy_file(srcPath, destPath):
    if os.path.exists(srcPath) and not os.path.exists(destPath):
        print 'cp %s to %s' % (srcPath,destPath)
        shutil.copy(srcPath,destPath)
        
def win_rar(source, target):
    today = target + time.strftime('%Y%m%d')
    now = time.strftime('%H%M%S')
    target = today + os.sep + now + '.rar'
 
    if not os.path.exists(today):
        os.mkdir(today) # make directory
        print( 'Successfully created directory', today)
      
    rar_command = "winrar a {0} {1}".format(target, source)

    if os.system(rar_command) == 0:
        print("成功")
    else:
        print("失败")
        
def backup_file(filelist):
    for i in range(0, length):
        basename =  find_file(dest,get_file_base_name(filelist[i]),filelist[i])#E:\work\git_berbon\bb_vm\mall\extension\guaranteeFundManage.vm
        basepath = get_file_base_path(basename)#E:\work\git_berbon\bb_vm\mall\extension\
        filedir = basepath.replace(dest,'').replace('\\','/')
        destpath = mkdir_p(filedir) + "\\" + get_file_base_name(filelist[i])
        copy_file(basename, destpath)
    
    win_rar(backdir, winrar)

backup_file(tmp)
#print(tmp)
#find_file(dest,'diy.js','mall\js\shopFitting\diy.js')

# -*Application End*-