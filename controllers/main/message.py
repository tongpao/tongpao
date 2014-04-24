#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: message.py

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import site_helper as sher
from modules.main.message import Message as Msg
import web
from utils import utils
class Message():
    def GET(self):
        return sher.main_render.message()
    def POST(self):
        data = web.input()
        del data['sub']
        mes = Msg()
        mes.create_message(data)

        raise web.seeother('/message',False)


