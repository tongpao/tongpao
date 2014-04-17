#! /usr/bin/env python2.7
# -*- coding: utf8 -*-
# Filename: login.py

import sys
reload(sys)
sys.setdefaultencoding("utf8")

import site_helper as sher
from modules.main.user import User#,News
import web
from web import form
#from utils import utils

"""
用户登录类
"""
class Login():
    """
        定义并初始化login_form,表单中有Textbox,Password,Button三个控件
    """
    login_form = form.Form(
        form.Textbox('username', form.notnull),
        form.Password('password', form.notnull),
        form.Button('Login'),
    )

    def GET(self):
        """接受URL请求，返回给用户登录页面
            @return 返回渲染的模板页面
        """
        form = self.login_form()

        return sher.main_render.login(form)

    def POST(self):
        """接受处理用户提交的登录表单，返回结果
            @return 如果用户存在且帐号密码正确则跳转到主页，否则返回登录
        """
        if not self.login_form.validates():
            """表单的基本验证
            """

            return sher.main_render.login(self.login_form)

        #得到用户输入表单中的username,password
        username = self.login_form['username'].value
        password = self.login_form['password'].value
        #将他们放入到字典中
        validate_dict = {'username':username,'passwd':password}
        #得到model中user对象
        user = User()
        #从数据库中查出所有用户的帐号和密码，返回一个字典类型users
        users = user.getUsers({'created':'0'},'username,passwd')
        #判断用户输入是否存在并正确
        if validate_dict in users:

            raise web.seeother('/', False)

        return sher.main_render.login(self.login_form)
