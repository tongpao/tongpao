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
    '/?(?:index(?:\.html)?)?', 'controllers.main.index.Index',    #controllers/main/index.py
    '/register(?:\.html)?', 'controllers.main.register.Register',    #controllers/main/register.py
    '/login(?:\.html)?', 'controllers.main.login.Login',           #controllers/main/login.py
    '/logout(?:\.html)?', 'controllers.main.login.Logout',         #controllers/main/login.py
    '/about_us(?:\.html)?', 'controllers.main.aboutus.Aboutus',#controllers/main/aboutus.py
    '/contact_us(?:\.html)?', 'controllers.main.contact_us.ContactUs', #controllers/main/contact_us.py
    '/message(?:\.html)?', 'controllers.main.message.Message', #controllers/main/message.py
    '/message/list(?:\.html)?', 'controllers.main.message_list.MsgList', #controllers/main/message_list.py
    '/message/view/(\d+)', 'controllers.main.message_view.MsgView', #controllers/main/message_view.py
    '/contact_list(?:\.html)?', 'controllers.main.contact_us.ContactList',#controllers/main/contact_list.py
    '/show_works(?:\.html)?', 'controllers.main.show_works.ShowWorks', #controllers/main/show_works.py
    '/news/list(?:\.html)?','controllers.main.news_list.NewsList',#controllers/main/news_list.py
    '/news/view/(\d+)','controllers.main.news_view.NewsView',#controllers/main/news_view.py
    '/admin/users(?:\.html)?', 'controllers.admin.admin_user.AdminUser', #controllers/admin/admin_user.py
)

app = web.application(urls, globals())

#加载render, globals可以放置对象,方法可以在base模板，子模板中用
render = web.template.render
main_render = render(loc='templates/main', base='base', globals={})
admin_render = render(loc='templates/admin', base='base', globals={})

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
