# 用户列表
import json
from flask import Blueprint, request
from flask import render_template

from dao.Film import Film
from dao.Gradeuser import Gradeuser
from utils import create_sql, mybaits
from utils.page import create_page

api_url_movie = Blueprint('movic', __name__)


@api_url_movie.route('/movieadmin', methods=['POST', 'GET'])
def get_pagelist():
    return render_template("fileadmin.html")


@api_url_movie.route('/list', methods=['POST', 'GET'])
def get_list():
    arr_select = []
    print(len(request.args))
    if len(request.args) > 2:
        name = request.args['name']
        actor = request.args['actor']
        typeid = request.args['typeid']
        typename = get_type(typeid)
        sql = create_sql.create_select(['*'], ['name', 'actor', 'typename'], 'film',
                                       ['"%{}%"'.format(name), '"%{}%"'.format(actor), '"%{}%"'.format(typename)])
    else:
        sql = create_sql.create_select(['*'], ['name', 'actor'], 'film', ['"%{}%"'.format(""), '"%{}%"'.format("")])
    film = Film()
    res = mybaits.select(sql, film.get_classinfo())
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




@api_url_movie.route("/film/delfilm", methods=['POST', 'GET'])
def del_movie():
    id = request.args['id']
    sql = create_sql.create_del(['id'], 'film', id)
    mybaits.deledb(sql)
    return "删除成功!"


# 用户电影页面
@api_url_movie.route('/movieuser', methods=['POST', 'GET'])
def get_pagemovie_list():
    return render_template("filetouser.html")


@api_url_movie.route('/film/search', methods=['POST', 'GET'])
def get_pagemovie():
    film = Film()
    sql = create_sql.create_select(["*"], ['typename'], 'film', ['"%{}%"'.format("")])
    res = mybaits.select(sql, film.get_classinfo())
    res_type = []
    for k in res:
        # k['desc_url'] = '"{}"'.format(k['desc_url'])
        k['typename'] = k['typename'][0:2]
        if len(k['name']) > 7:
            k['name'] = k['name'][0:7] + '...'
        if len(k['importrole']) == 2:
            k['importrole'] = "暂无主演数据"
        if len(k['importrole']) > 11:
            k['importrole'] = k['importrole'][0:11] + "..."
        res_type.append(k)
    res_data = {
        'code': 1,
        'data': res_type,
    }
    return json.dumps(res_data).encode('utf-8')


@api_url_movie.route('/film/getinfo', methods=['POST', 'GET'])
def get_movieby_id():
    ids = request.args['id']
    sql = create_sql.create_selectbyid(['desc_url', 'name'], ['id'], 'film', ['"{}"'.format(str(ids))])
    res = mybaits.select(sql, ['desc_url', 'name'])
    res_data = {
        'code': 1,
        'data': res,
    }
    return json.dumps(res_data).encode('utf-8')


@api_url_movie.route('type/getAllType', methods=['POST', 'GET'])
def get_all_type():
    sql = create_sql.create_select(['*'], ['id', 'typename'], 'type', ['"%{}%"'.format(""), '"%{}%"'.format("")])
    print(sql)
    res = mybaits.select(sql, ['typeid', 'typename'])
    return json.dumps(res).encode('utf-8')


def get_type(id):
    sql = create_sql.create_selectbyid(['id', 'typename'], ['id'], 'type', ['{}'.format(str(id))])
    res = mybaits.select(sql, ['typeid', 'typename'])
    return res[0]['typename']


# 用户评分接口
@api_url_movie.route('film/givegrade', methods=['POST', 'GET'])
def get_add():
    userid = request.args['id']
    grade = request.args['grade']
    moviename = request.args['moviename']
    gradeuser = Gradeuser()
    gradeuser.set_grade("{}".format(float(grade)))
    gradeuser.set_userid("{}".format(userid))
    gradeuser.set_movie_name("'{}'".format(moviename))
    res = ['userid', 'movie_name', 'grade']
    sql = create_sql.create_insert(res, [gradeuser.userid, gradeuser.movie_name, gradeuser.grade],
                                   'gradeuser')
    mybaits.add(sql)
    res = {
        'code': 1
    }
    return json.dumps(res).encode('utf-8')
