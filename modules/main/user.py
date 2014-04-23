#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: user.py

import config
from libs.db import db
class User():
    def __init__(self):
        self.config = config.getConfig()
        self.db = db(w_db = self.config.site_db_w) 

    def create_user(self, data):
        insert_id = self.db.create('b_user', data)

        return insert_id

    def update_user(self, condition, data):
        self.db.updateBy('b_user', condition, data)

    def delete_user(self, condition):
        self.db.deleteBy('b_user', condition)

    def getUserBy(self, condition, fields = '*'):
        row = self.db.getBy('b_user', condition, fields = fields)

        return row

    def getCount(self, condition):
        return self.db.getCount('b_user', condition)

    def getUsers(self, condition, orderBy = None, start = None, limit = None, fields = '*'):
        sql = """select %s from b_user as a inner join b_permissons as b using(u_id) inner join b_perm_level as c \
                 on b.level_id = c.id where is_active = %d order by %s limit %d, %d\
              """ % (fields, condition['is_active'], orderBy, start, limit) 
        print 'sql:', sql
        rows = self.db.sql(sql).fetchall()

        return rows





