#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: modules/news.py
import config
from libs.db import db
from utils import utils
class News():
    def __init__(self):
        self.config = config.getConfig()
        self.db = db(w_db = self.config.site_db_w) 

    def getCount(self, condition = {}):
        return self.db.getCount('b_news', condition)

    def getNewsById(self, condition, fields = '*'):
        row = self.db.getBy('b_news', condition, fields)

        return row 

    def getNews(self, condition, orderBy = None, start = None, limit = None, fields = '*'):
        rows = self.db.getList('b_news',condition, orderBy, start, limit, fields)

        return rows
