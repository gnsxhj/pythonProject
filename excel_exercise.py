#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding=utf-8

# ## 格式化excel文件
# import xlwings as xw
#
# #获取样例表格的列宽数据
# def get_sample_format(col): #因为无需读取整个excel所有列的列宽，所以这里传入一个读取的列宽范围参数
#     wb = xw.Book(".\materials\sample.xlsx")  #建立于sample.xlsx文件的连接
#     sheet = wb.sheets["Sheet1"]  #打开sample.xlsx文件的sheet1
#     format = []
#     for i in range(col):
#         format.append(sheet[0, i].column_width)
#     print('列宽:'+str(format))  #'行高：'+sheet.range('A1').column_width+
#     wb.close()
#     return format
# #美化表格
# def beautiful_sheet(table_name,raw,col,format):
#     #设置颜色
#     wb2 = xw.Book(table_name)  # 建立excel表连接
#     sheets_name = [st.name for st in wb2.sheets]
#     for st in sheets_name:
#         sheet2 = wb2.sheets[st]
#         # sheet2[0,0] =
#         sheet2.range('a1').value = ['序号','工号','姓名','科室','股','联系方式','身份证号','工种','编制','入职时间','合同到期时间','离职时间','合同公司'] #更改标题行
#         sheet2[0:raw,0:col+1].api.Borders(12).LineStyle = 0 #设置单元格横边框为细框线
#         sheet2[0:raw, 0:col+1].api.Borders(11).LineStyle = 0 #设置单元格竖边框为细框线
#         sheet2[0:raw,0:col].api.Font.Name = '微软雅黑'# 设置字体格式为微软雅黑
#         sheet2[0:raw, 0:col].api.HorizontalAlignment = -4108  #设置字体居中
#         #sheet2[:,4].api.NumberFormat = "0%"    #“霸榜率”这一列单元格设置为百分比格式显示
#         for i in range(raw): ##行遍历
#             if i == 0:
#                 sheet2[i, 0:col].color = [217, 217, 217] #设置标题背景颜色格式
#             elif i % 2 == 0:
#                 sheet2[i, 0:col].color = [183, 222, 232]    #设置偶数行背景颜色格式为浅蓝色
#         for i, item in enumerate(format): #列遍历,根据sample.xlsx中的列宽进行调整
#             sheet2[0, i].column_width = item
#     wb2.save()#保存excel
#     wb2.close()#关闭excel
#     return None
#
# if __name__ == '__main__':
#     table_name = ".\materials\data.xlsx"#需要修改的excel名字
#     raw = 151 #需要修改格式的行数
#     col = 8  ##需要修改格式的列数
#     format = get_sample_format(col)
#     beautiful_sheet(table_name,raw,col,format)

import os
import openpyxl

path = r'./materials'
os.chdir(path)

wb = openpyxl.load_workbook('sample.xlsx')
print(wb.sheetnames)

sheet = wb['Sheet1'] # 获取指定的sheet表
print(sheet)