#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: register.py

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import site_helper as sher
from modules.main.user import User 
import web
from utils import utils
class Register():
    def GET(self):
        return sher.main_render.register()

    def POST(self):
        data = web.input()
        del data['sub']
        del data['repasswd']
        user = User()
        user.create_user(data)
        raise web.seeother('/', False)



        

