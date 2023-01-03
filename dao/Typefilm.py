class Typefilm(object):
    def __init__(self):
        self.id = None
        self.typename = None
        self.typedesc = None
        self.updatetime = None
        self.num = None
        self.state = None

    def get_id(self):
        return self.id

    def get_typename(self):
        return self.typename

    def get_typedesc(self):
        return self.typedesc

    def get_updatetime(self):
        return self.updatetime

    def get_num(self):
        return self.num

    def get_state(self):
        return self.state

    def set_id(self, value):
        self.id = value

    def set_typename(self, value):
        self.typename = value

    def set_typedesc(self, value):
        self.typedesc = value

    def set_updatetime(self, value):
        self.updatetime = value

    def set_num(self, value):
        self.num = value

    def set_state(self, value):
        self.state = value

    def get_classinfo(self):
        res = ['id', 'typename', 'typedesc', 'updatetime', 'num', 'state']
        return res
