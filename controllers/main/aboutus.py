#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: controllers/aboutus.py

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import site_helper as sher
class Aboutus():
    def GET(self):
        return sher.main_render.about_us()

        
