#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: show_works.py

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import site_helper as sher
class ShowWorks():
    def GET(self):

        return sher.main_render.show_works()
        
