#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: news.py
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import web
import site_helper as sher
from modules.main.news import M_News 
from utils import utils
from libs.page import page

class NewsList():
    def __init__(self):
        self.news = M_News()
    
    def GET(self):
        page_size = 10 
        pages = 10
        request_data = web.input()
        if 'page' not in request_data:
            current_page = 1
        else:
            current_page = int(request_data['page'])
        condition = {'is_display':'show'}
        rows_count = self.news.getCount(condition)
        getRowsFunc = self.news.getNews
        orderBy = 'id desc'
        fields = 'id, title, created'

        #引用分页
        data = page(page_size, pages, current_page, rows_count, getRowsFunc, condition, orderBy, fields)
        functions = {'tsp2date':utils.convTsp2Date,}
        data['functions'] = functions

        return sher.main_render.news_list(data)

