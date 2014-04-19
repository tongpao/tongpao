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

        user = User()
        row = user.getUserBy({'username':data['username'], 'email':data['email']})
        if row is None:
            print 'not regitser'
            user.create_user(data)
            return sher.main_render.login()
        else:
            raise web.seeother('register',False)


#
#        username= data['username']
#        email=data['email']
#        user = User()
#        validata_user={'username':username}
#        validata_email={'email':email} 
#        getusername=user.getUsers({'created':'0'},'username')
#        getemail=user.getUsers({'created':'0'},'email')
#        if validata_user in getusername:
#        elif validata_email in getmail:
#            raise web.seeother('/',False)
#
#        else:
#
#
##        raise web.seeother('/', False)
#
#
#
#        
#
