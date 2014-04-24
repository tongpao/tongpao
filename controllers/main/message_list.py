# /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: message_list.py
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import web
import site_helper as sher
from modules.main.message import M_Message
from utils import utils
from libs.page import page

class MsgList():
#    def GET(self):
#        msg = M_Message()
#        rows = msg.getMsgs({} ,fields = '*')       
#        print rows
#        data = {
#                    'rows':rows, 
#                }
#
#        return data 
#
#        return sher.main_render.message_list(data)
    def __init__(self):
        self.msg = M_Message()

    def GET(self):
        page_size = 3 
        pages = 3 
        request_data = web.input()
        if 'page' not in request_data:
            current_page = 1
        else:
            current_page = int(request_data['page'])
        condition = {}
        rows_count = self.msg.getCount(condition)
        getRowsFunc = self.msg.getMsgs
        orderBy = 'id desc'
        fields = '*'

        #引用分页
        data = page(page_size, pages, current_page, rows_count, getRowsFunc, condition, orderBy, fields)
        functions = {'tsp2date':utils.convTsp2Date,}
        data['functions'] = functions
        print data

        return sher.main_render.message_list(data)

