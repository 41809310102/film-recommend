import json
from flask import Blueprint, request
from flask import render_template

from dao.Typefilm import Typefilm

from utils import create_sql, mybaits
from utils.page import create_page
import datetime

api_url_type = Blueprint('api', __name__)


@api_url_type.route('/get_typepage', methods=['POST', 'GET'])
def get_page():
    return render_template("typeadmin.html")


# 获取所有类型数据
@api_url_type.route('/list', methods=['POST', 'GET'])
def get_list():
    print(len(request.args))
    if len(request.args) > 2:
        name = request.args['typename']
        actor = request.args['typedesc']
        sql = create_sql.create_select(['*'], ['typename', 'typedesc'], 'type',
                                       ['"%{}%"'.format(name), '"%{}%"'.format(actor)])
    else:
        sql = create_sql.create_select(['*'], ['typename', 'typedesc'], 'type',
                                       ['"%{}%"'.format(""), '"%{}%"'.format("")])
    type = Typefilm()
    res = mybaits.select(sql, type.get_classinfo())
    page = request.args['page']
    limit = request.args['limit']
    print(len(res))
    res = create_page(int(page), int(limit), res)
    res_data = {
        "code": 0,
        "msg": "",
        "count": len(res),
        "data": res
    }
    return json.dumps(res_data).encode('utf-8')


# 新增类型
@api_url_type.route('type/add_type', methods=['POST', 'GET'])
def add_type():
    data = request.form
    print(data)
    type = Typefilm()
    type.set_typename("'{}'".format(data['typename']))
    type.set_typedesc("'{}'".format(data['typedesc']))
    type.set_updatetime("'{}'".format(datetime.datetime.now().strftime('%Y-%m-%d')))
    type.set_num(data['num'])
    res = ['typename', 'typedesc', 'updatetime', 'num', 'state']
    if data['id'] == '':
        type.set_state("'{}'".format("正常"))
        sql = create_sql.create_insert(res,
                                       [type.typename, type.typedesc, type.updatetime, type.num, type.state], 'type')
        res = mybaits.add(sql)
        if res > 0:
            res_data = {
                'code': 1,
                'msg': "添加成功"
            }
        else:
            res_data = {
                'code': 1,
                'msg': "添加成功"
            }
    else:
        type.set_state("'{}'".format(data['state']))
        sql = create_sql.create_update('type', res,
                                       [type.typename, type.typedesc, type.updatetime, type.num, type.state], ['id'],
                                       "{}".format(str(data['id'])))
        mybaits.update(sql)
        res_data = {
            'code': 1,
            'msg': "修改成功"
         }

    return json.dumps(res_data).encode('utf-8')
    # 删除数据


@api_url_type.route("/type/deltype", methods=['POST', 'GET'])
def del_movie():
    id = request.args['id']
    sql = create_sql.create_del(['id'], 'type', id)
    mybaits.deledb(sql)
    return "删除成功!"




# 查询当前数据是否存在
def get_infobyid(id):
    sql = create_sql.create_selectbyid(["id"], ["id"], 'type', ["'{}'".format(str(id))])
    res = mybaits.select(sql, ['id'])
    if len(res) > 0:
        return True
    else:
        return False


