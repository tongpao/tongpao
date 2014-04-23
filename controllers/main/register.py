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
import time
class Register():
    def GET(self):
        error={'status':'init', 'msg':''}
        
        return sher.main_render.register(error)

    def POST(self):
        request_data = web.input()
        password=request_data['passwd']
        rpassword=request_data['rpasswd']
        if password != rpassword: 
            #如果passwd！=rpasswd
            error={'status':'failure','msg':"passwd is not equilt rpasswd"}
            return sher.main_render.register(error)

        user = User()
        row = user.getUserBy({'username':request_data['username'],'email':request_data['email']})
        if row:#如果用户名存在，提示更改用户名
            error={'status':'failure', 'msg':'user name existed'}
            return sher.main_render.register(error)

        createdata=int(time.time())#加入时间
        request_data['created']=createdata
        del request_data['rpasswd']#如果不存在当前用户，直接存储到数据库，回到login页面
        user.create_user(request_data)
        raise web.seeother('login',False)
        
        
        
