import xlwt
import random

from xlwt.compat import xrange

if __name__ == '__main__':
    # 注意这里的excel文件的后缀是xls 如果是xlsx打开会无效
    wtPath = '/Users/yvetteyoung/Desktop/test.xls'
    wtBook = xlwt.Workbook()

    # 新增一个sheet
    sheet = wtBook.add_sheet('test',cell_overwrite_ok=True)

    # 写入数据头
    headList = ['数据1','数据2','数据3']
    rowIndex = 0
    col = 0

    # 循环写入
    for head in headList:
        sheet.write(rowIndex, col, head)
        col = col + 1


    # 写入10行随机数
    for index in xrange(1, 11):
        for col in xrange(1, 3):
            data = random.randint(0, 99)
            sheet.write(index, 0, index) # 写序号
            sheet.write(index, col, data) # 写数据
        print("写第[%d]行数据"%index)

    # 保存
    wtBook.save(wtPath)