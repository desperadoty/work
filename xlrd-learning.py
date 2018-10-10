import xlrd
from xlwt.compat import xrange

if __name__ == '__main__':
    # excel路径
    xlPath = '/Users/yvetteyoung/Desktop/test.xlsx'

    # 用于读取excel
    xlBook = xlrd.open_workbook(xlPath)

    # 获取excel工作簿数
    count = len(xlBook.sheets())
    print("工作簿数为：",count)

    # 获取表数据的行列数
    table = xlBook.sheets()[0]
    nrows = table.nrows
    ncols = table.ncols
    print("表数据行列为（%d,%d)"%(nrows,ncols))

    # 循环读取数据
    for i in xrange(0, nrows):
        rowValues = table.row_values(i) # 按行读取数据
        # 输出读取的数据
        for data in rowValues:
            print(data , "\t")
        print("\n")