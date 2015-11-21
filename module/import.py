# -*- coding: UTF-8 -*-
# -*Application Start*-
#引用新功能
from __future__ import division

from __future__ import unicode_literals

import os
import math
#动态导入模块
try:
    import json
except ImportError:
    import simplejson



osFunc = dir(os)
mathFunc = dir(math)

print os.path.isdir(r'D:\python\excel')
print os.path.isfile(r'D:\python\excel\demo.py')

print json.dumps({'python':2.7})

print (10/3)

print isinstance('am I an unicode', unicode)

# -*Application End*-