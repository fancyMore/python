# -*- coding: UTF-8 -*-
# -*Application Start*-
import os
import xlrd
import xlwt
from xlutils.copy import copy
import string

sourceXls = 'D:/excelDemo/source/source.xls'
targetXls = 'D:/excelDemo/result/result.xls'

# filePath = input (u'请将xls文件路径粘贴进去，如果程序里已经指定了文件则按Enter键继续：')
# print (filePath)

# 打开Excel文件读取数据
sourceBook = xlrd.open_workbook(sourceXls)
targetBook = xlrd.open_workbook(targetXls, formatting_info=True)

try:
    # 通过索引顺序获取指定工作表
    sourceSheet = sourceBook.sheet_by_index(0)
    targetSheet = targetBook.sheet_by_index(0)
except:
    print ("no sheet in %s named Sheet1" % sourceSheet)

'''
#复制workbook
copyTargetBook = copy(targetBook)
copyTargetSheet = copyTargetBook.get_sheet(0)
#写入workbook
copyTargetSheet.write(1,5,'fancy');
#保存workbook
copyTargetBook.save('D:/excelDemo/dest/fancy.xls');
'''

# 获取行数
sourceRows = sourceSheet.nrows
# 获取列数
sourceCols = sourceSheet.ncols

print ("sourceRows %d, sourceCols %d" % (sourceRows, sourceCols))

# 获取第一行第一列数据
cell_value = sourceSheet.cell_value(1, 3)
print (cell_value)

row_list = []

myData = []

newWorkbook = xlwt.Workbook(encoding='ascii')
newWorksheet = newWorkbook.add_sheet('HZXM')

for k in range(1, sourceRows):
    # print (sourceSheet.col_values(4)[k])
    newWorksheet.write(k - 1, 0, label=sourceSheet.col_values(4)[k])

newWorkbook.save('D:/excelDemo/dest/fancy.xls');

'''
#获取各行数据
for i in range(1,sourceRows):
    row_data = sh.row_values(i)
'''
print('---------------------os')
cOs = dir(os)
print(cOs)
print('---------------------xlrd')
cXlrd = dir(xlrd)
print(cXlrd)
print('---------------------xlwt')
cXlwt = dir(xlwt)
print(cXlwt)
print('---------------------copy')
cCopy = dir(copy)
print(cCopy)
# -*Application End*-
