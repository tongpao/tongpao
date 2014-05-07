#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: db.py
import MySQLdb,types

class DBConfigError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class db:
    def __init__(self, w_db = None, r_db = None):
        self.writeable = False  # 读写权限
        self.readable  = False  # 只读权限
        if r_db is not None:
            self.readable = True
            if 'port_r' not in r_db:
                r_db['port_r'] = 3306
            self.dbConn_r = MySQLdb.connect(host=r_db['host_r'], port = r_db['port_r'], user=r_db['user_r'],\
                    passwd=r_db['passwd_r'], db=r_db['database_r'], charset='utf8')
            self.dbCursor_r = self.dbConn_r.cursor(cursorclass = MySQLdb.cursors.DictCursor)
        if w_db is not None:
            self.writeable = True 
            if 'port_w' not in w_db:
                w_db['port_w'] = 3306
            self.dbConn_w = MySQLdb.connect(host=w_db['host_w'], port = w_db['port_w'], user=w_db['user_w'],\
                    passwd=w_db['passwd_w'], db=w_db['database_w'], charset='utf8')
            self.dbCursor_w = self.dbConn_w.cursor(cursorclass = MySQLdb.cursors.DictCursor)

        if not self.writeable and not self.readable:
            raise DBConfigError('you must have a host.')

    def sql(self, sql):
        #判断是查询语句，并且读服务器连接上,优先用读服务器
        if self.readable and sql.lstrip()[0:7].lower().startswith('select'):
            print 'read: sql:',sql
            self.dbCursor_r.execute(sql)
            self.dbConn_r.commit()
            return self.dbCursor_r

        elif self.writeable:
            print 'write: sql:',sql
            self.dbCursor_w.execute(sql)
            if sql.lstrip()[0:7].lower().startswith('insert'):
                insert_id = self.dbConn_w.insert_id()
                self.dbConn_w.commit()
                return insert_id
            self.dbConn_w.commit()
            return self.dbCursor_w
        else:
            raise DBConfigError('sql read or write permission for current session is wrong.')

    def sqlExe(self, sql):
        #判断是查询语句，并且读服务器连接上,优先用读服务器
        if self.readable and sql.lstrip()[0:7].lower().startswith('select'):
            #print 'read1:, sql:',sql
            self.dbCursor_r.execute(sql)
            self.dbConn_r.commit()
        elif self.writeable:
            self.dbCursor_w.execute(sql)
            self.dbConn_w.commit()
            #print 'write:, sql:',sql
        else:
            raise DBConfigError('sql read or write permission for current session is wrong.')

        return True
    
    def truncate(self, table_name):
        sql = "truncate table %s" % table_name
        self.sql(sql)

    def create(self, table, dataDict, autocommit = True):
        dataList = []
        for key,value in dataDict.items():
            if isinstance(value, basestring):
                value = MySQLdb.escape_string(value.encode('utf-8'))
            dataList.append("%s='%s'" % (key, value))
        data = ",".join(dataList)

        sql = "INSERT INTO %s SET %s" % (table, data)
        insert_id = self.sql(sql)
        return insert_id

    def dealConditionDict(self, conditionDict):
        condition = '1'
        if conditionDict:
            conditionList = []
            for key, value in conditionDict.items():
                if isinstance(value, basestring):
                    value = MySQLdb.escape_string(value.encode('utf-8'))
                value = str(value)
                if '>' in value or '<' in value:  
                    operator = value[:1] if '=' not in value else value[:2]
                    value = value[1:] if '=' not in value else value[2:]
                    conditionList.append("%s %s '%s'" % (key, operator, value))
                else:
                    conditionList.append("%s='%s'" % (key, value))
            condition = " and ".join(conditionList)

        return condition

    def getBy(self, table, conditionDict = None, fields = '*'):
        condition = self.dealConditionDict(conditionDict)
        sql = "SELECT %s FROM %s WHERE %s" % (fields, table, condition)
        dbCursor = self.sql(sql)
        return dbCursor.fetchone()
    
    def getCount(self, table, conditionDict = None):
        condition = self.dealConditionDict(conditionDict)
        sql = "SELECT count(*) as count FROM %s WHERE %s" % (table, condition)
        dbCursor = self.sql(sql)
        count = dbCursor.fetchone()
        return count['count']

    def getList(self, table, conditionDict=None, orderBy=None, start=None, limit=None, fields = '*'):
        sql = "SELECT %s FROM %s" % (fields,table)
        condition = self.dealConditionDict(conditionDict)
        sql = "%s WHERE %s" % (sql, condition)
        if orderBy is not None:
            sql = "%s ORDER BY %s" % (sql, orderBy)
        if start is not None and limit is not None:
            sql = "%s LIMIT %s,%s" % (sql, start, limit)
        dbCursor = self.sql(sql)
        return dbCursor.fetchall()

    def updateBy(self, table, dataDict = None, conditionDict = None):
        condition = self.dealConditionDict(conditionDict)
        dataList = []
        for key,value in dataDict.items():
            if isinstance(value, basestring):
                value = MySQLdb.escape_string(value.encode('utf-8'))
            dataList.append("%s='%s'" % (key, value))
        data = ",".join(dataList)

        if condition != '':
            sql = "UPDATE %s SET %s WHERE %s" % (table, data, condition)
            self.sql(sql)

    def deleteBy(self, table, conditionDict = None):
        condition = self.dealConditionDict(conditionDict)
        sql = "DELETE FROM %s WHERE %s" % (table, condition)
        self.sql(sql)

if __name__ == "__main__":
    #create table user(id int primary key auto_increment, name char(32), age int) engine=innodb default charset=utf8;
    test_db_w = {'host_w':'localhost', 'user_w':'test', 'passwd_w':'123456', 'database_w':'test', 'port_w':3306}
    testdb = db(w_db=test_db_w)
    #def create(self, table, dataDict, autocommit = True):
    print 'test: def create(self, table, dataDict, autocommit = True):'
    testdb.create('user', {'name':'zhangsan','age':10})
    testdb.create('user', {'name':'lisi','age':11})
    testdb.create('user', {'name':'wangwu','age':12})
    testdb.create('user', {'name':'lili','age':14})
    testdb.create('user', {'name':'tt','age':17})
    print 
    
    #def getBy(self, table, conditionDict = None, fields = '*'):
    print "test: def getBy(self, table, conditionDict = None, fields = '*'):"
    row = testdb.getBy('user')
    print ';'.join(["%s=%s" % (k, v) for k, v in row.items()])

    row = testdb.getBy('user', {'name':'tt'})
    print ';'.join(["%s=%s" % (k, v) for k, v in row.items()])
    
    row = testdb.getBy('user', {'name':'lili', 'age':14})
    print ';'.join(["%s=%s" % (k, v) for k, v in row.items()])
    print 

    #def getCount(self, table, conditionDict = None):
    print 'test: def getCount(self, table, conditionDict = None):'
    count = testdb.getCount('user')
    print 'user: %d' % count

    count = testdb.getCount('user', {'name':'lisi'})
    print 'user: %d' % count
    print 

    #def getList(self, table, conditionDict=None, orderBy=None, start=None, limit=None, fields = '*'):
    print "test: def getList(self, table, conditionDict=None, orderBy=None, start=None, limit=None, fields = '*'):"
    rows = testdb.getList('user')
    print 'rows len: ', len(rows)

    rows = testdb.getList('user', {'name':'lisi'})
    print 'rows len: ', len(rows)

    rows = testdb.getList('user', {'age':'>=10', 'age':'<=13'})
    print 'rows len: ', len(rows)

    rows = testdb.getList('user', {'age':'>12', 'age':'<14'})
    print 'rows len: ', len(rows)
    print 

    #def updateBy(self, table, dataDict = None, conditionDict = None):
    print 'test: def updateBy(self, table, dataDict = None, conditionDict = None):'
    testdb.updateBy('user', {'name':'zs'}, {'name':'zhangsan'})
    print 

    #def deleteBy(self, table, conditionDict = None):
    print 'test: def deleteBy(self, table, conditionDict = None):'
    testdb.deleteBy('user', {'name':'lisi'})
    print 

    #def truncate(self, table_name):
    print 'test: def truncate(self, table_name):'
    testdb.truncate('user')
    print 

