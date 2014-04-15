#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: httpi.py
import httplib2,urllib,sys
import HTMLParser

def sendRequest(url, method="GET", body=None, headers={}):
    #print "request: %s" % url
#    baseHttp = httplib2.Http('.cache',timeout=60)
    baseHttp = httplib2.Http(timeout=60)
    if body is not None:
        body=urllib.urlencode(body)
    headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.110 Safari/537.36'
    headers['Content-type'] = 'application/x-www-form-urlencoded'
    response = content = None
    for tryCount in range(5):
        try:
            response, content = baseHttp.request(url, method, body=body, headers=headers)
            break
        except KeyboardInterrupt:
            print "用户终止"
            sys.exit()
        except:
            print "请求url:%s失败,请求方式:%s,正在重试第%s次" % (url.encode('utf-8'), method, tryCount)
            continue
    return response, content

def download(url, savePath, headers={}):
    #print "download: %s" % url
    baseHttp = httplib2.Http(timeout=60)
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1'
#headers['Host'] = 'asp.cntv.lxdns.com'
    response = content = ''
    dlSuccess = False
    for tryCount in range(5):
        try:
            response, content = baseHttp.request(url, headers=headers)
            dlSuccess = True
            break
        except KeyboardInterrupt:
            print "用户终止"
            sys.exit()
        except:
            print "下载url:%s失败,正在重试第%s次" % (url.encode('utf-8'), tryCount)
            continue

    if not dlSuccess:
        print "下载失败，终止重试"
        return False
    try:
        f = open(savePath,"wb")
        f.write(content)
        f.close()
        return True
    except:
        print "保存文件失败"
        return False

#urldecode
def unquoteString(string, coding):
    try:
        string = urllib.unquote(string).decode(coding).encode('utf-8')
        return string
    except:
        pass

    codingList = ['utf-8', 'gb2312', 'gbk', 'gb18030', 'big5']
    codingList.remove(coding)
    for coding in codingList:
        try:
            string = urllib.unquote(string).decode(coding).encode('utf-8')
            return string
        except:
            pass
    return ''

def convertCoding(string, original_coding, target_coding = 'utf-8'):
    try:
        string = string.decode(original_coding, 'ignore').encode(target_coding)
        return string
    except Exception, ex:
        print "转换编码%s->%s失败: %s" % (coding, target_coding, ex)
    return ''
    '''
    codingList = ['utf-8', 'gb2312', 'gbk', 'gb18030', 'big5']
    codingList.remove(coding)
    for coding in codingList:
        try:
            string = string.decode(coding).encode('utf-8')
            return string
        except:
            pass
    return ''
    '''

def parseUrl(url):
    try:
        proto, rest = urllib.splittype(url)
        host, rest = urllib.splithost(rest)
        host, port = urllib.splitport(host)
        return proto, host, port, rest
    except:
        pass
    return None, None, None, None

def html_entity_decode(string):
    parser = HTMLParser.HTMLParser()
    string = parser.unescape(string)
    parser.close()
    return string
