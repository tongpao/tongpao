#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: contact_us.py

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import site_helper as sher
class ContactUs():
    def GET(self):

        return sher.main_render.contact_us()
        
