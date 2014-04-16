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

    def getUsers(self, condition, fields = '*'):
        rows = self.db.getList('b_user', condition, fields = fields)

        return rows





