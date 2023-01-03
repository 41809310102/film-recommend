import json
from flask import Blueprint, request, render_template

from dao.Film import Film
from utils import create_sql, mybaits, recommendations

api_url_tuijian = Blueprint('tuijian', __name__)


def get_all_user():
    sql = create_sql.create_select(['id'], ['username'], 'user', ['"%{}%"'.format("")])
    res = mybaits.select(sql, ['id'])
    nodes = {}
    for k in res:
        nodes[k['id']] = get_all_grade(k['id'])
    return nodes


def get_all_grade(ids):
    res = ['userid', 'movie_name', 'grade']
    sql = create_sql.create_selectbyid(res, ['userid'], 'gradeuser', "{}".format(str(ids)))
    res_data = mybaits.select(sql, res)
    nodes = {}
    for k in res_data:
        nodes[k['movie_name']] = k['grade']
    return nodes


def get_tuijian_movie(ids):
    res = recommendations.getRecommendations(get_all_user(), ids)
    tuijian = []  # 推荐电影信息
    for k in res:
        print(k[1])
        sql = create_sql.create_selectbyid(["*"], ['name'], 'film', ["'{}'".format(k[1])])
        film = Film()
        res = mybaits.select(sql, film.get_classinfo())
        for k in res:
            tuijian.append(k)
    return tuijian


@api_url_tuijian.route('/tuijian_page', methods=['POST', 'GET'])
def get_yuijian_page():
    return render_template("tuijian.html")


@api_url_tuijian.route('tj/getofuser_tj', methods=['POST', 'GET'])
def get_user_movie():
    ids = request.args['id']
    res = get_tuijian_movie(int(ids))
    res_code = {
        'code': 1,
        'msg': "推荐电影如下",
        'data': res
    }
    return json.dumps(res_code).encode('utf-8')


@api_url_tuijian.route('/tj/getinfo', methods=['POST', 'GET'])
def get_movieby_id():
    ids = request.args['id']
    sql = create_sql.create_selectbyid(['desc_url', 'name'], ['id'], 'film', ['"{}"'.format(str(ids))])
    res = mybaits.select(sql, ['desc_url', 'name'])
    res_data = {
        'code': 1,
        'data': res,
    }
    return json.dumps(res_data).encode('utf-8')


if __name__ == '__main__':
    get_tuijian_movie(2)
