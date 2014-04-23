#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: message.py

import config
from libs.db import db
class Message():
    def __init__(self):
        self.config = config.getConfig()
        self.db = db(w_db = self.config.site_db_w) 

    def create_message(self, data):
        insert_id = self.db.create('b_message', data)

        return insert_id

    def update_message(self, condition, data):
        self.db.updateBy('b_message', condition, data)

    def delete_message(self, condition):
        self.db.deleteBy('b_message', condition)

    def getMsgBy(self, condition, fields = '*'):
        row = self.db.getBy('b_message', condition, fields = fields)

        return row

    def getMsgs(self, condition, fields = '*'):
        rows = self.db.getList('b_message', condition, fields = fields)

        return rows


