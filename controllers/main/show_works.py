#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: show_works.py

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import web
import site_helper as sher
from modules.main.teamworks import M_Team_Works 
from utils import utils
from libs.page import page
class ShowWorks():
    def __init__(self):
        self.works = M_Team_Works()
    
    def GET(self):
        page_size = 4 
        pages = 4 
        request_data = web.input()
        if 'page' not in request_data:
            current_page = 1
        else:
            current_page = int(request_data['page'])
        condition = {}
        rows_count = self.works.getCount(condition)
        getRowsFunc = self.works.getWorks
        orderBy = 'id desc'
        fields = '*'
        #引用分页
        data = page(page_size, pages, current_page, rows_count, getRowsFunc, condition, orderBy, fields)
        functions = {'tsp2date':utils.convTsp2Date,}
        data['functions'] = functions
#        print data

        
        return sher.main_render.show_works(data)

