#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: admin/addteamwork.py

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import site_helper as sher
from modules.main.teamworks import M_Team_Works
import web
from utils import utils
class AddTeamWork():
    def GET(self):
        return sher.admin_render.addteamwork()
        
    def POST(self):
        data = web.input()
        del data['sub']
        mtw = M_Team_Works()
        mtw.create_works(data)

        raise web.seeother('/admin/teamworklist',False)


