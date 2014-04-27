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
news = M_News()
class News():
    
    def GET(self):
        return sher.admin_render.admin_news()

class addNews():

    def GET(self):
         
        return sher.admin_render.addnews() 
        
    def POST(self):
        request_data=web.input()
        del request_data['filedown']
        createdata=int(time.time())
        request_data['created']=createdata
        request_data['is_display']='show'
        news.create_news(request_data)
        
        return sher.admin_render.addnews() 
class delNews():


    def GET(self):
      #  condition={"'is_display'":"show"}
        newslist=news.getNews({})
        print newslist
        return sher.admin_render.delnews(newslist)
    
    
    def POST(self):
        up_date={}
        request_data=web.input()
        up_date['is_display']='hidden'
        print up_date
        print request_data
       # request_data['id']=int(request_data['id'])
        print request_data
        print request_data
        delnews=news.update_news(request_data,up_date)
        print request_data
  #      delnews=news.delete_news(request_data)
        raise web.seeother('delnews',False)

class searchNews():
     
    def GET(self):
        search={}
        return sher.admin_render.searchnews(search)

    def POST(self):
        request_data=web.input()
        print request_data
  #      request_data["*"]=request_data.pop("search")
        print request_data
        search = news.search_news(request_data)
#        search=news.getNews(condition=request_data)
        print search
        print search
        return sher.admin_render.searchnews(search)





