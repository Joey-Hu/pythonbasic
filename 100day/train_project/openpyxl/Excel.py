#!/usr/bin/env python
# encoding: utf-8

# @author: huhao
# @Software : PyCharm
# @file: homework.py
# @time: 2019/6/14 14:27
# @Ducument：https://www.python.org/doc/
# @desc:

from openpyxl import load_workbook
from openpyxl import Workbook

wb = load_workbook('./employees.xlsx')

'''
# 以只读模式打开excel表
# wb = load_workbook('./employees.xlsx', read_only= True)

# 获取sheet页表名称列表
sheets_list = wb.sheetnames
print(sheets_list)
'''

# 读取sheet页表
# 根据名称读取
sheet = wb['employees']

print(sheet.title)

# 新建 sheet 页
wb.create_sheet('test', )
print(wb.sheetnames)

# 修改 sheet 页名称
sheet_test = wb['test']
sheet_test.title = 'test2'
print(wb.sheetnames)

# 删除 sheet 页：要先获取到 sheet 页才能删除，不能直接用 sheet 页的名称删除
sheet_rm = wb['test2']
wb.remove(sheet_rm)
print(wb.sheetnames)

# 获取指定行/列和切片操作
# print(sheet[2:3])
# print(sheet['B:C'])


for row in range(1, 101):
    for col in range(65, 71):  # A-F
        cell_index = chr(col) + str(row)
        # chr(c): Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.
        print(sheet[cell_index].value, end='\t')
    print()

# 错误log
# Error:'tuple' object has no attribute 'value'
# sheet[cell_index].value 中的cell_index必须是string类型

# 读取单元格
print(sheet.cell(2, 3).value)  # 读取第二行第三列单元格数据

# 修改单元格的值
sheet.cell(2, 3).value = 'huhao'
print(sheet.cell(2, 3).value)

# 公式：单元格求和，求平均值。。。

# 单元格合并与分裂

# 单元格样式

# 保存 Workbook
wb.save('./employees.xlsx')
