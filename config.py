#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: config.py
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
"""这是全局配置文件
    要求：使用变量名 = 值格式表示，每个变量名在其上说明其意义
"""
class Config():
    #网站版本
    version = 0.1

    #是否开启debug模式
    debug = True 

    #网站数据库配置,可以配置读写分离
    site_db_w = {'host_w':'localhost', 'user_w':'test', 'passwd_w':'123456', 'database_w':'tongpao_db', 'port_w':3306}

def getConfig():
    return Config()
