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

if __name__ == '__main__':
    pass
