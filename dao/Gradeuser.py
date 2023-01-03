class Gradeuser(object):
    def __init__(self):
        self.id = None
        self.userid = None
        self.movie_name = None
        self.grade = None

    def get_id(self):
        return self.id

    def get_userid(self):
        return self.userid

    def get_movie_name(self):
        return self.movie_name

    def get_grade(self):
        return self.grade

    def set_id(self, value):
        self.id = value

    def set_userid(self, value):
        self.userid = value

    def set_movie_name(self, value):
        self.movie_name = value

    def set_grade(self, value):
        self.grade = value

    def get_classinfo(self):
        res = ['id', 'userid', 'movie_name', 'grade']
        return res