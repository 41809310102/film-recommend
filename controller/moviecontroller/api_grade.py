import json
from flask import Blueprint, request

from dao.Gradeuser import Gradeuser
from utils import create_sql, mybaits
from utils.page import create_page

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


@api_url_grade.route('grade/list', methods=['POST', 'GET'])
def get_allgrade():
    print(len(request.args))
    if len(request.args) > 2:
        name = request.args['moviename']
        actor = request.args['userid']
        sql = create_sql.create_select(['*'], ['mpviename', 'userid'], 'gradeuser',
                                       ['"%{}%"'.format(name), '"%{}%"'.format(actor)])
    else:
        sql = create_sql.create_select(['*'], ['mpviename', 'userid'], 'gradeuser',
                                       ['"%{}%"'.format(""), '"%{}%"'.format("")])
    type = Gradeuser()
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
