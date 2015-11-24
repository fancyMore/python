# -*- coding: UTF-8 -*-
# -*Application Start*-
import os
import sys

desc_dir=sys.argv[1]

try:
    #home = os.path.expanduser("~") #把path中包含的"~"和"~user"转换成用户目录
    #print home
    if not os.path.exists(desc_dir):
        os.makedirs(desc_dir)
except Exception as e:
    print e
# -*Application End*-
'''
@usage
python file_batch_name.py D:\batch\fancy
'''
