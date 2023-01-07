import json
from flask import Blueprint, request, render_template

from dao.Gradeuser import Gradeuser
from utils import create_sql, mybaits
from utils.page import create_page
import datetime

api_url_grade = Blueprint('usergrade', __name__)


@api_url_grade.route('grade/givegrade', methods=['POST', 'GET'])
def get_add():
    userid = request.args['userid']
    grade = request.args['grade']
    moviename = request.args['moviename']
    gradeuser = Gradeuser()
    gradeuser.set_grade("{}".format(float(grade)))
    gradeuser.set_userid("{}".format(userid))
    gradeuser.set_movie_name("'{}'".format(moviename))
    sql = create_sql.create_insert(gradeuser.get_classinfo(), [gradeuser.userid, gradeuser.movie_name, gradeuser.grade],
                                   'gradeuser')
    mybaits.add(sql)
    return "评分成功"


@api_url_grade.route('/page', methods=['POST', 'GET'])
def get_admin_grade():
    return render_template("gradeadmin.html")


# 请求格式
#
# http://127.0.0.1:5001/grade/list?page=""&&limit=""
@api_url_grade.route('/list', methods=['POST', 'GET'])
def get_admin_data():
    print(len(request.args))
    if len(request.args) > 2:
        movie_name = request.args['name']
        sql = create_sql.create_select(['*'], ['movie_name'], 'gradeuser',
                                       ['"%{}%"'.format(movie_name)])
    else:
        sql = create_sql.create_select(['*'], ['movie_name'], 'gradeuser',
                                       ['"%{}%"'.format("")])
    film = Gradeuser()
    res = mybaits.select(sql, film.get_classinfo())
    page = request.args['page']
    limit = request.args['limit']
    print(len(res))
    res_user_name = get_id_getname()
    res = create_page(int(page), int(limit), res)
    for k in res:
        k['username'] = res_user_name[k['userid']]
    res_data = {
        "code": 0,
        "msg": "",
        "count": len(res),
        "data": res
    }
    return json.dumps(res_data).encode('utf-8')


# 获取用户姓名
def get_id_getname():
    sql = create_sql.create_select(['id', 'username'], ['username'], 'user', ['"%{}%"'.format("")])
    res = mybaits.select(sql, ['id', 'username'])
    res_data = {}
    for k in res:
        res_data[k['id']] = k['username']
    return res_data


# 删除评分信息
@api_url_grade.route("/grade/delgrade", methods=['POST', 'GET'])
def del_movie():
    id = request.args['id']
    sql = create_sql.create_del(['id'], 'gradeuser', id)
    mybaits.deledb(sql)
    return "删除成功!"


# 获取用户信息
@api_url_grade.route('grade/getAlluser', methods=['POST', 'GET'])
def get_all_user():
    sql = create_sql.create_select(['*'], ['id', 'username'], 'user', ['"%{}%"'.format(""), '"%{}%"'.format("")])
    print(sql)
    res = mybaits.select(sql, ['id', 'username'])
    return json.dumps(res).encode('utf-8')


@api_url_grade.route('grade/add_grade', methods=['POST', 'GET'])
def add_type():
    data = request.form
    print(data)
    type = Gradeuser()
    type.set_movie_name("'{}'".format(data['movie_name']))
    type.set_grade("'{}'".format(data['grade']))
    res = ['movie_name', 'grade', 'createtime']
    if data['id'] == '':
        sql = create_sql.create_insert(res,
                                       [type.movie_name, type.grade, "'{}'".format(datetime.datetime.now().strftime('%Y-%m-%d'))], 'gradeuser')
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
        sql = create_sql.create_update('gradeuser', res,
                                       [type.movie_name, type.grade,"'{}'".format(datetime.datetime.now().strftime('%Y-%m-%d')), type], ['id'],
                                       "{}".format(str(data['id'])))
        mybaits.update(sql)
        res_data = {
            'code': 1,
            'msg': "修改成功"
         }

    return json.dumps(res_data).encode('utf-8')
    # 删除数据


if __name__ == '__main__':
    get_id_getname()
