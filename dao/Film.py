class Film(object):
    def __init__(self):
        self.id = None
        self.name = None
        self.actor = None
        self.uptime = None
        self.douban = None
        self.typeid = None
        self.typename = None
        self.local = None
        self.showtime = None
        self.picurl = None
        self.desc_url = None
        self.importrole = None
        self.state = None

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_actor(self):
        return self.actor

    def get_uptime(self):
        return self.uptime

    def get_douban(self):
        return self.douban

    def get_typeid(self):
        return self.typeid

    def get_typename(self):
        return self.typename

    def get_local(self):
        return self.local

    def get_showtime(self):
        return self.showtime

    def get_picurl(self):
        return self.picurl

    def get_desc_url(self):
        return self.desc_url

    def get_importrole(self):
        return self.importrole

    def get_state(self):
        return self.state

    def set_id(self, value):
        self.id = value

    def set_name(self, value):
        self.name = value

    def set_actor(self, value):
        self.actor = value

    def set_uptime(self, value):
        self.uptime = value

    def set_douban(self, value):
        self.douban = value

    def set_typeid(self, value):
        self.typeid = value

    def set_typename(self, value):
        self.typename = value

    def set_local(self, value):
        self.local = value

    def set_showtime(self, value):
        self.showtime = value

    def set_picurl(self, value):
        self.picurl = value

    def set_desc_url(self, value):
        self.desc_url = value

    def set_importrole(self, value):
        self.importrole = value

    def set_state(self, value):
        self.state = value

    def get_classinfo(self):
        res = ['id', 'name', 'actor', 'uptime', 'douban', 'typeid', 'typename', 'local', 'showtime', 'pic_url', 'desc_url', 'importrole', 'state']
        return res