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
import time
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
        return sher.admin_render.admin_news() 

class addNews():

    def GET(self):
         
        return sher.admin_render.addnews() 
        
    def POST(self):
        request_data=web.input()
        print request_data
        del request_data['filedown']
        createdata=int(time.time())
        print request_data
        request_data['created']=createdata
        news=M_News()
        news.create_news(request_data)
        
        return sher.admin_render.addnews() 
class delNews():


    def GET(self):
        news=M_News()
        newslist=news.getNews(condition={},fields="*")
        return sher.admin_render.delnews(newslist)
    
    
    def POST(self):
        request_data=web.input()
        print request_data
        news=M_News()
        delnews=news.delete_news(request_data)
        raise web.seeother('delnews',False)
class searchNews():
    pass






