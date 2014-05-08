#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: admin_user.py

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import site_helper as sher
import web
from libs.page import page
from modules.main.user import User
from utils import utils
class AdminUser():
    def __init__(self):
        self.user = User()
        pass

    def GET(self):
        request_data = web.input()
        if 'mod' in request_data:
            mod = request_data['mod']  
            if mod == 'list':
                return self.listUser(request_data)
            elif mod == 'view':
                return self.viewUser(request_data)

        return '404 page'

    def POST(self):
        request_data = web.input()
        if 'mod' in request_data:
            if mod == 'add':
                return self.addUser(request_data)
            elif mod == 'delete':
                return self.delUser(request_data)
            elif mod == 'update':
                return self.updateUser(request_data)

        return '404 page'

    def addUser(self):
        pass

    def updateUser(self):
        pass

    def delUser(self):
        """删除用户只是把用户重激活状态变成未激活状态"""
        pass

    def viewUser(self, request_data):
        u_id = None if 'u_id' not in request_data else int(request_data['u_id'])
        row = self.user.getUserBy({'u_id':u_id})
        
        return sher.admin_render.view_user(row)

    def listUser(self, request_data):
        """分页展示用户"""
        page_size = 2 
        pages = 3 
        current_page = 1 if 'page' not in request_data else int(request_data['page'])
        is_active = 1 if 'is_active' not in request_data else 0 
        condition = {'is_active':is_active}
        rows_count = self.user.getCount(condition)
        getRowsFunc = self.user.getUsers
        orderBy = 'u_id desc'
        fields = 'a.u_id, a.username, a.email, a.is_active, a.created, b.level_id, c.description'

        #引用分页
        data = page(page_size, pages, current_page, rows_count, getRowsFunc, condition, orderBy, fields)
        functions = {'tsp2date':utils.convTsp2Date,}
        data['functions'] = functions

        return sher.admin_render.list_user(data)


