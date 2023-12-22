<<<<<<< HEAD
# -*- coding:utf-8 -*-
import os
from win32com.client import Dispatch, constants, gencache, DispatchEx


class PDFConverter:
    def __init__(self, pathname, export='.'):
        self._handle_postfix = ['doc', 'docx', 'ppt', 'pptx', 'xls', 'xlsx']
        self._filename_list = list()
        self._export_folder = os.path.join(os.path.abspath('.'), 'pdfconver')
        if not os.path.exists(self._export_folder):
            os.mkdir(self._export_folder)
        self._enumerate_filename(pathname)

    def _enumerate_filename(self, pathname):
        '''
        读取所有文件名
        '''
        full_pathname = os.path.abspath(pathname)
        if os.path.isfile(full_pathname):
            if self._is_legal_postfix(full_pathname):
                self._filename_list.append(full_pathname)
            else:
                raise TypeError(
                    '文件 {} 后缀名不合法！仅支持如下文件类型：{}。'.format(pathname, '、'.join(self._handle_postfix)))
        elif os.path.isdir(full_pathname):
            for relpath, _, files in os.walk(full_pathname):
                for name in files:
                    filename = os.path.join(full_pathname, relpath, name)
                    if self._is_legal_postfix(filename):
                        self._filename_list.append(os.path.join(filename))
        else:
            raise TypeError('文件/文件夹 {} 不存在或不合法！'.format(pathname))

    def _is_legal_postfix(self, filename):
        return filename.split('.')[-1].lower() in self._handle_postfix and not os.path.basename(filename).startswith(
            '~')

    def run_conver(self):
        '''
        进行批量处理，根据后缀名调用函数执行转换
        '''
        print('需要转换的文件数：', len(self._filename_list))
        for filename in self._filename_list:
            postfix = filename.split('.')[-1].lower()
            funcCall = getattr(self, postfix)
            print('原文件：', filename)
            funcCall(filename)
        print('转换完成！')

    def doc(self, filename):
        '''
        doc 和 docx 文件转换
        '''
        name = os.path.basename(filename).split('.')[0] + '.pdf'
        exportfile = os.path.join(self._export_folder, name)
        print('保存 PDF 文件：', exportfile)
        gencache.EnsureModule('{00020905-0000-0000-C000-000000000046}', 0, 8, 4)
        w = Dispatch("Word.Application")
        doc = w.Documents.Open(filename)
        doc.ExportAsFixedFormat(exportfile, constants.wdExportFormatPDF,
                                Item=constants.wdExportDocumentWithMarkup,
                                CreateBookmarks=constants.wdExportCreateHeadingBookmarks)

        w.Quit(constants.wdDoNotSaveChanges)

    def docx(self, filename):
        self.doc(filename)

    def xls(self, filename):
        '''
        xls 和 xlsx 文件转换
        '''
        name = os.path.basename(filename).split('.')[0] + '.pdf'
        exportfile = os.path.join(self._export_folder, name)
        xlApp = DispatchEx("Excel.Application")
        xlApp.Visible = False
        xlApp.DisplayAlerts = 0
        books = xlApp.Workbooks.Open(filename, False)
        books.ExportAsFixedFormat(0, exportfile)
        books.Close(False)
        print('保存 PDF 文件：', exportfile)
        xlApp.Quit()

    def xlsx(self, filename):
        self.xls(filename)

    def ppt(self, filename):
        '''
        ppt 和 pptx 文件转换
        '''
        name = os.path.basename(filename).split('.')[0] + '.pdf'
        exportfile = os.path.join(self._export_folder, name)
        gencache.EnsureModule('{00020905-0000-0000-C000-000000000046}', 0, 8, 4)
        p = Dispatch("PowerPoint.Application")
        ppt = p.Presentations.Open(filename, False, False, False)
        ppt.ExportAsFixedFormat(exportfile, 2, PrintRange=None)
        print('保存 PDF 文件：', exportfile)
        p.Quit()

    def pptx(self, filename):
        self.ppt(filename)


if __name__ == "__main__":
    # 支持文件夹批量导入
    folder = 'tmp'
    pathname = os.path.join(os.path.abspath('.'), folder)

    # 也支持单个文件的转换
    # pathname = 'test.doc'

    pdfConverter = PDFConverter(pathname)
    pdfConverter.run_conver()
=======
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
>>>>>>> origin/master
