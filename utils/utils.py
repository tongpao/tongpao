#! /usr/bin/env python
#-*- coding:utf-8 -*-
#Filename: utils.py
def printRow(row, delimit = '\n'):
    content = delimit.join(['%s=%s' % (k, v) for k, v in row.items()])
    print content 
    return content

def printRows(rows, delimit = ';'):
    content = ''
    for row in rows:
        tmp = delimit.join(['%s=%s' % (k, v) for k, v in row.items()])
        print tmp 
        print
        content = '%s\n<br />%s' % (content, tmp)
    return content

def judgeIsNone(data, key_list):
    if data is None:
        return {'status':False, 'msg':'data is None'} 

    for key in key_list:
        if key in data.keys() and data[key] is not None:
            continue
        else:
            return {'status':False, 'msg':'key: %s is None' % key} 
    return {'status':True, 'msg':'ok'} 

def convTsp2Date(tsp):
    """转换时间戳为日期格式"""
    import time
    timeArray = time.localtime(tsp)
    return time.strftime("%Y-%m-%d %H:%M:%S", timeArray)

def convDate2Tsp(date):
    import time
    timeArray = time.strptime(date, "%Y-%m-%d %H:%M:%S")
    return int(time.mktime(timeArray))


    
if __name__ == '__main__':
    pass
