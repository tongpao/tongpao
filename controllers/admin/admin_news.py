#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: news_view.py
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import web
import site_helper as sher
from modules.main.news import M_News 
from utils import utils

class News():
    def __init__(self):
        self.news = M_News()

    def GET(self):

#           row = self.news.getNewsById({'id':news_id}, fields = '*')
#           if not row:
#               return '404page'
#   
#           row['created'] = utils.convTsp2Date(row['created'])
#   
        return sher.main_render.admin_news() 



