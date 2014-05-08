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
from libs.page import page

class NewsView():
    def __init__(self):
        self.news = M_News()

    def GET(self, news_id):

        row = self.news.getNewsById({'id':news_id}, fields = '*')
        if not row:
            return '404page'

        row['created'] = utils.convTsp2Date(row['created'])

        return sher.main_render.news_view(row) 



