#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: controllers/index.py

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import site_helper as sher
from modules.main.news import News 
class Index():
    def GET(self):
        new = News()
        news = new.getNews()

        return sher.main_render.index(news)
        
