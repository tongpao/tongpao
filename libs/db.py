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

    def sql(self,sql):
        #判断是查询语句，并且读服务器连接上,优先用读服务器
        if self.readable and sql.lstrip()[0:7].lower().startswith('select'):
            #print 'read1:, sql:',sql
            self.dbCursor_r.execute(sql)
            self.dbConn_r.commit()
            return self.dbCursor_r

        elif self.writeable:
            #print 'write:, sql:',sql
            self.dbCursor_w.execute(sql)
            if sql.lstrip()[0:7].lower().startswith('insert'):
                insert_id = self.dbConn_w.insert_id()
                self.dbConn_w.commit()
                return insert_id
            self.dbConn_w.commit()
            return self.dbCursor_w
        else:
            raise DBConfigError('sql read or write permission for current session is wrong.')

    def sqlExe(self,sql):
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
    
    def truncate(self,table_name):
        sql = "truncate table %s" % table_name
        self.sql(sql)

    def create(self, table, dataDict,autocommit = True):
        dataList = []
        for key,value in dataDict.items():
            if isinstance(value, basestring):
                value = MySQLdb.escape_string(value.encode('utf-8'))
            dataList.append("%s='%s'" % (key, value))
        data = ",".join(dataList)

        sql = "INSERT INTO %s SET %s" % (table, data)
        insert_id = self.sql(sql)
        return insert_id

    def getBy(self, table, conditionDict,fields = '*'):
        conditionList = []
        for key,value in conditionDict.items():
            if isinstance(value, basestring):
                value = MySQLdb.escape_string(value.encode('utf-8'))
            conditionList.append("%s='%s'" % (key, value))
        condition = " and ".join(conditionList)

        sql = "SELECT %s FROM %s WHERE %s" % (fields,table, condition)
        dbCursor = self.sql(sql)
        return dbCursor.fetchone()
    
    def getCount(self, table, conditionDict):
        conditionList = []
        for key,value in conditionDict.items():
            if isinstance(value, basestring):
                value = MySQLdb.escape_string(value.encode('utf-8'))
            conditionList.append("%s='%s'" % (key, value))
        condition = " and ".join(conditionList)

        if condition == '':
            condition = '1'
        sql = "SELECT count(*) as count FROM %s WHERE %s" % (table, condition)
        dbCursor = self.sql(sql)
        count = dbCursor.fetchone()
        return count['count']

    def getList(self, table, condition=None, orderBy=None, start=None, limit=None, fields = '*'):
        sql = "SELECT %s FROM %s" % (fields,table)
        if condition is not None:
            if type(condition) is types.DictType:
                conditionList = []
                for key,value in condition.items():
                    if isinstance(value, basestring):
                        value = MySQLdb.escape_string(value.encode('utf-8'))
                    conditionList.append("%s='%s'" % (key, value))
                condition = " and ".join(conditionList)
            sql = "%s WHERE %s" % (sql, condition)
        if orderBy is not None:
            sql = "%s ORDER BY %s" % (sql, orderBy)
        if start is not None and limit is not None:
            sql = "%s LIMIT %s,%s" % (sql, start, limit)
        dbCursor = self.sql(sql)
        return dbCursor.fetchall()

    def updateBy(self, table, conditionDict, dataDict):
        conditionList = []
        for key,value in conditionDict.items():
            if isinstance(value, basestring):
                value = MySQLdb.escape_string(value.encode('utf-8'))
            conditionList.append("%s='%s'" % (key, value))
        condition = " and ".join(conditionList)

        dataList = []
        for key,value in dataDict.items():
            if isinstance(value, basestring):
                value = MySQLdb.escape_string(value.encode('utf-8'))
            dataList.append("%s='%s'" % (key, value))
        data = ",".join(dataList)

        if condition != '':
            sql = "UPDATE %s SET %s WHERE %s" % (table, data, condition)
            self.sql(sql)

    def deleteBy(self, table, conditionDict):
        conditionList = []
        for key,value in conditionDict.items():
            if isinstance(value, basestring):
                value = MySQLdb.escape_string(value.encode('utf-8'))
            conditionList.append("%s='%s'" % (key, value))
        condition = " and ".join(conditionList)

        if condition != '':
            sql = "DELETE FROM %s WHERE %s" % (table, condition)
            self.sql(sql)

if __name__ == '__main__':
    w_db = {'host_w':'xigua.huafeiduo.com', 'user_w':'men10', 'passwd_w':'shang2050kai', 'database_w':'test'}
    r_db = {'host_r':'xigua.huafeiduo.com', 'user_r':'men10', 'passwd_r':'shang2050kai', 'database_r':'test'}
    testdb = db(w_db, r_db)
    #testdb = db(w_db = w_db)
    #testdb = db(r_db = r_db)
    write_sql = """insert into tst(name) values('test')"""
    testdb.sql(write_sql)
    write_sql = """update tst set name='test_for_update' where id=1"""
    testdb.sql(write_sql).fetchone()
    read_sql = """select * from tst"""
    print testdb.sql(read_sql).fetchall()
    testdb.truncate('tst')
    data = {'name':'42424'}
    print testdb.create('tst', data)
    print testdb.create('tst', data)
    print testdb.sql(read_sql).fetchall()
    print testdb.getBy('tst', {'id':1})
    testdb.updateBy('tst', {'id':1}, {'name':'tttuut'})
    print testdb.sql(read_sql).fetchall()
    print testdb.getList('tst')
    print testdb.getCount('tst', {})
    testdb.sqlExe(write_sql)
    print testdb.getList('tst')

