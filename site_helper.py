#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: site_helper.py

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
"""这是网站的入口文件，用于调动controllers, modules, templates下的内容来服务"""
import web
import config
web.config.debug = config.getConfig().debug
#全局网站映射, 每一个url的partner, webpy会自动加上^$,所以对于剩余uri，强制使用(.*)铺获
#每一个类，在webpy的application中都是递归的导入相应的类，如:
#a.b.c.d.E  E是文件中的类，则:
#类似 from a.b.c.d import E
urls = (
    '/?', 'controllers.main.index.Index',    #controllers/main/index.py 
    '/register', 'controllers.main.register.Register',    #controllers/main/register.py 
    '/message', 'controllers.main.message.Message',     #controllers/main/message.py
    '/about_us', 'controllers.main.aboutus.Aboutus',#controllers/main/aboutus.py
)

#加载render, globals可以放置对象,方法可以在base模板，子模板中用
render = web.template.render
main_render = render(loc='templates/main', base='base', globals={}) 

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
