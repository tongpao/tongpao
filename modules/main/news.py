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
    def getNews(self):
        content = 'hello, world!'

        return content 
