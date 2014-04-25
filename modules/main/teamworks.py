#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: modules/teamworks.py
import config
from libs.db import db
from utils import utils
class M_Team_Works():
    def __init__(self):
        self.config = config.getConfig()
        self.db = db(w_db = self.config.site_db_w) 

    def getCount(self, condition = {}):
        return self.db.getCount('b_team_works', condition)

    def getWorksById(self, condition, fields = '*'):
        row = self.db.getBy('b_team_works', condition, fields)

        return row 

    def getWorks(self, condition, orderBy = None, start = None, limit = None, fields = '*'):
        rows = self.db.getList('b_team_works',condition, orderBy, start, limit, fields)

        return rows
    
    def delete_works(self,condition):
        self.db.daleteBy('b_team_works',condition)

    def update_works(self,condition):
        self.db.updateBy('b_team_works',condition,data)

    def create_works(self,data):
        insert_id=self.db.create('b_team_works',data)

        return insert_id

