#! /usr/bin/env python2.7
# -*- coding: utf8 -*-
# Filename: login.py

import sys
reload(sys)
sys.setdefaultencoding("utf8")

import site_helper as sher
from modules.main.user import User
import web

"""
用户登录类
"""
class Login():

    def GET(self):
        """接受URL请求，判断用户是否已登录，如果未登录返回给用户登录页面
            @return 返回渲染的模板页面
            否则直接跳转到主页
        """
        if web.ctx.session.isLogin != 1:
            result = {'status':'success'}

            return sher.main_render.login(result)

        raise web.seeother('/', False)

    def POST(self):
        #得到用户输入表单中的username,password
        inputDate = web.input()
        username = inputDate['username']
        password= inputDate['password']

        #得到model中user对象
        user = User()
        #从数据库中查出所有用户的帐号和密码，返回一个字典类型users
        users = user.getUsers({'username':username, 'passwd':password},'u_id')

        #判断用户输入是否存在并正确
        #若正确则为其创建session表示已登录
        if users:
            web.ctx.session.isLogin = 1
            result =  {'status':'success',}

            raise web.seeother('/', False)

        result =  {'status':'failure',}
        return sher.main_render.login(result)

class Logout():
    def GET(self):
        web.ctx.session.isLogin = 0
        web.ctx.session.kill()

        raise web.seeother('/', False)

