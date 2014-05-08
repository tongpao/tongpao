#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: index.py

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import site_helper as sher
class Index():
    def GET(self):

        return sher.admin_render.index()
        
