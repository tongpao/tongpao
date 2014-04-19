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
    '/login', 'controllers.main.login.Login',           #controllers/main/login.py
    '/logout', 'controllers.main.login.Logout',         #controllers/main/login.py
    '/message', 'controllers.main.message.Message',     #controllers/main/message.py
    '/about_us', 'controllers.main.aboutus.Aboutus',#controllers/main/aboutus.py
)

app = web.application(urls, globals())

#加载render, globals可以放置对象,方法可以在base模板，子模板中用
render = web.template.render
main_render = render(loc='templates/main', base='base', globals={})

#创建session对象，并进行初始化
session = web.session.Session(app, web.session.DiskStore('sessions/'), initializer = {'is_login':False , 'is_super':False})
#设置session过期时间
web.config.session_parameters['timeout'] = config.getConfig().session_timeout
#创建一个被web.loadhook加载的处理器(processor)
def session_hook():
    web.ctx.session = session
app.add_processor(web.loadhook(session_hook))

if __name__ == '__main__':
    app.run()
