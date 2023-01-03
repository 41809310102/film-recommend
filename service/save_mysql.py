import xlrd

from utils import mybaits
from utils.create_sql import create_db, create_insert


# 电影数据导入数据库
def save_film():
    path = '../filexlsx/douban_2021.xlsx'
    # 常用功能
    # 打开实验数据表格
    book = xlrd.open_workbook(path)
    # 选择页数为第1页
    sheet1 = book.sheets()[0]
    # 数据总行数
    nrows = sheet1.nrows
    print('数据总行数：', nrows)
    # 数据总列数
    ncols = sheet1.ncols
    print('表格总列数：', ncols)
    # 获取表中第三行的数据
    for k in range(1, nrows):
        x = sheet1.row_values(k)
        file = {
            'id': x[0],
            'name': "'{}'".format(change_data(x[1])),
            'local': "'{}'".format(x[2]),
            'actor': "'{}'".format(x[4]),
            'typename': "'{}'".format(x[12] + "," + x[13] + "," + x[14]),
            'uptime': "'{}'".format(change_time(x[17])),
            'showtime': "'{}'".format(x[18]),
            'numpeople': "'{}'".format(x[21]),
            'douban': "'{}'".format(x[22]),
            'importrole': "'{}'".format(x[28] + "," + x[30] + "," + x[32]),
            'desc_url':"'{}'".format(x[38]),
            'pic_url': "'{}'".format(x[39]),
        }
        res = ['name', 'actor', 'uptime', 'douban', 'typeid', 'typename', 'local', 'showtime', 'pic_url', 'desc_url',
               'importrole', 'state']
        sql = create_insert(res,
                            [file['name'], file['actor'], file['uptime'], file['douban'], "1", file['typename'],
                             file['local'], file['showtime'], file['pic_url'], file['desc_url'], file['importrole'],
                             "''"], 'film')
        try:
            mybaits.add(sql)
        except:
            print("数据有问题，跳过")


def change_data(data):
    len_data = len(data)
    return data[:len_data - 5]


def change_time(data):
    return data[0:10]


if __name__ == '__main__':
    # # create_db('film',)
    # create_class('Film')
    save_film()
