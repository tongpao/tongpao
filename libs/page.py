#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: libs/page.py

def page(page_size, pages, current_page, rows_count, getRowsFunc, condition, orderBy, fields = "*"):
    """
        适合单表分页
        @param page_size 每页显示行数
        @param pages 展示分页数
        @param current_page 当前页
            获得方法:
                if 'page' not in request_data:
                    self.current_page = 1
                else:
                    self.current_page = int(request_data['page'])
        @param rows_count 总的满足条件的函数
        @param getRowsFunc 获得展示数据行函数
            说明:
                getRowsFunc(condition, orderBy = orderBy, start = start, limit = limit, fields = '*')
                    自己在函数中选择表
        @param condition 获得数据条件
        @param orderBy 获得数据排序列

        @return 
            data = {
                        'rows':rows, #当前页展示符合条件condition的行数 
                        'start_page':start_page,#显示的起始页 
                        'end_page':end_page,#显示结束页
                        'next_page':next_page,#下一页
                        'last_page':last_page,#上一页
                        'page_count':page_count,#总的页数，做尾页
            }

    """
    if current_page <= 0: current_page = 1
    #page_count 总的分页数
    if rows_count < page_size:
        page_count = 1
    elif (rows_count % page_size != 0):
        page_count = rows_count / page_size + 1
    else:
        page_count = rows_count / page_size

    #起始位置
    start = (current_page - 1) * page_size
    #显示行数
    limit = page_size
    #获取数据行
    rows = getRowsFunc(condition,orderBy = orderBy, start = start, limit = limit, fields = fields)

    #开始页
    start_page = current_page - (current_page % pages)
    if start_page <= 0: start_page = 1

    #结束页
    end_page = start_page + pages
    if end_page > page_count: end_page = page_count 

    #下一页
    next_page = current_page + 1
    if next_page > page_count: next_page = page_count

    #上一页
    last_page = current_page - 1
    if last_page <= 0: last_page = 1

    data = {
                'rows':rows, 
                'start_page':start_page, 
                'end_page':end_page,
                'next_page':next_page,
                'last_page':last_page,
                'page_count':page_count
    }

    return data 


        

