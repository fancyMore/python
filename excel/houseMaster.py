# -*- coding: UTF-8 -*-
# -*Application Start*-

# 导入模块

import os
import xlrd
import xlwt
from xlutils.copy import copy

# 获取并处理数据源
srcXlsPath = 'D:/excelDemo/source/source.xls'
srcBook = xlrd.open_workbook(srcXlsPath)
srcSheet = srcBook.sheet_by_index(0)
srcRows = srcSheet.nrows

# 结果数据
destXlsPath = 'D:/excelDemo/result/result.xls'
destBook = xlrd.open_workbook(destXlsPath,formatting_info=True)


# 分类存储相同数据
class_list = {}
for i in range(1,srcRows):
    row_data = srcSheet.row_values(i)
    myKey = row_data[2]
    class_list[myKey] = []

for d in class_list:
    for i in range(1,srcRows):
        row_data = srcSheet.row_values(i)
        myKey = row_data[2]
        if d == myKey:
            class_list[d].append(row_data)

# 填充数据
for d in class_list:
    singleList = class_list[d]
    sLen = int(len(singleList))
    amount = int((sLen + 3 - 1)/3)
    for i in range(0,amount):
        tmpBook = copy(destBook)
        tmpSheet = tmpBook.get_sheet(0)
        for k in range(i*3, (i+1)*3):

            if k < sLen:
                row_data = singleList[k]
                rest = (k+1) % 3
                if rest == 1:
                    #表1数据
                    #指界人
                    tmpSheet.write(5,29,row_data[22]) #row, column, value
                    #地块编码
                    tmpSheet.write(2,1,row_data[5])
                    #地块名称
                    tmpSheet.write(4,1,row_data[6])
                    #合同面积
                    tmpSheet.write(4,3,row_data[14])
                    #东至
                    tmpSheet.write(6,1,row_data[17])
                    #西至
                    tmpSheet.write(8,1,row_data[19])
                    #南至
                    tmpSheet.write(6,3,row_data[18])
                    #北至
                    tmpSheet.write(8,3,row_data[20])
                    #土地用途
                    tmpSheet.write(10,1,' ☑种植业 ☐林业'.decode('utf-8'))
                     #土地利用类型
                    tmpSheet.write(13,1,' ☑水田 ☐旱地'.decode('utf-8'))
                elif rest == 2:
                    #表2数据
                    tmpSheet.write(21,29,row_data[22])#row, column, value
                    #地块编码
                    tmpSheet.write(18,1,row_data[5])
                    #地块名称
                    tmpSheet.write(20,1,row_data[6])
                    #合同面积
                    tmpSheet.write(20,3,row_data[14])
                     #东至
                    tmpSheet.write(22,1,row_data[17])
                    #西至
                    tmpSheet.write(24,1,row_data[19])
                    #南至
                    tmpSheet.write(22,3,row_data[18])
                    #北至
                    tmpSheet.write(24,3,row_data[20])
                    #土地用途
                    tmpSheet.write(26,1,' ☑种植业 ☐林业'.decode('utf-8'))
                    #土地利用类型
                    tmpSheet.write(29,1,' ☑水田 ☐旱地'.decode('utf-8'))
                elif rest == 0:
                    #表3数据
                    tmpSheet.write(37,29,row_data[22]) #row, column, value
                    #地块编码
                    tmpSheet.write(34,1,row_data[5])
                    #地块名称
                    tmpSheet.write(36,1,row_data[6])
                     #合同面积
                    tmpSheet.write(36,3,row_data[14])
                     #东至
                    tmpSheet.write(38,1,row_data[17])
                    #西至
                    tmpSheet.write(40,1,row_data[19])
                    #南至
                    tmpSheet.write(38,3,row_data[18])
                    #北至
                    tmpSheet.write(40,3,row_data[20])
                    #土地用途
                    tmpSheet.write(42,1,' ☑种植业 ☐林业'.decode('utf-8'))
                     #土地利用类型
                    tmpSheet.write(45,1,' ☑水田 ☐旱地'.decode('utf-8'))
        print('D:/excelDemo/dest/'+ str(d) + '_' + str(i) + '.xls')
        tmpBook.save('D:/excelDemo/dest/'+ str(d) + '_' + str(i) + '.xls')



# -*Application End*-
