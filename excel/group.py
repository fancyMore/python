# -*- coding: UTF-8 -*-
# -*Application Start*-

# 导入模块
import os
import xlrd
import xlwt
from xlutils.copy import copy

# 发包方信息
codeXlsPath = 'D:/handle/source/code.xls'
codeBook = xlrd.open_workbook(codeXlsPath)
codeSheet = codeBook.sheet_by_index(0)
codeRows = codeSheet.nrows

# 获取并处理数据源
srcXlsPath = 'D:/handle/source/all.xls'
srcBook = xlrd.open_workbook(srcXlsPath)
srcSheet = srcBook.sheet_by_index(0)
srcRows = srcSheet.nrows

# 结果数据
destXlsPath = 'D:/handle/source/result_c.xls'
destBook = xlrd.open_workbook(destXlsPath,formatting_info=True)

#存储包信息
class_code = {}
for i in range(0,codeRows):
    row_data = codeSheet.row_values(i)
    myKey = row_data[0]
    class_code[myKey] = []
    class_code[myKey].append(row_data[2])
    class_code[myKey].append(row_data[3])

# 分类存储相同数据
class_list = {}
for i in range(3,srcRows):
    row_data = srcSheet.row_values(i)
    myKey = row_data[12]
    class_list[myKey] = []

for d in class_list:
    for i in range(1,srcRows):
        row_data = srcSheet.row_values(i)
        myKey = row_data[12]
        if d == myKey:
            class_list[d].append(row_data)

#填充数据
for d in class_list:
    tmpBook = copy(destBook)
    tmpSheet = tmpBook.get_sheet(0)
    for o in class_code:
        if o == d:
            msg = class_code[d][0]
    singleList = class_list[d]
    sLen = int(len(singleList)) #行数
    for i in range(0,sLen):
        for k in range(0,9):
                tmpSheet.write(3+i,k,singleList[i][k])
    tmpBook.save('D:/handle/dest/'+ msg +  '_农户摸底信息表'.decode('UTF-8') +'.xls')
#print len(class_list['51070420520101'])

# -*Application End*-
#singleList是[[],[],[]]