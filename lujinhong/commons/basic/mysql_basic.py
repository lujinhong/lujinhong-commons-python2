# -*- coding: utf8 -*_

import MySQLdb

class MysqlBasic():

    def __init__(self):
        self.db = 'ljhtest'
        self.table='test'
        self.cursor = MySQLdb.connect(host='10.82.126.12',user='ljh', passwd='lujinhong',charset='utf8', use_unicode=False).cursor()

    def saveToDb(self):
        sql = "insert into aso.test values(1,'ljh')"
        print sql
        try:
            self.cursor.execute(sql)
            self.cursor.execute("commit")
        except BaseException, e:
            print e
        return 0

if __name__ == '__main__':
    mysqlBasic =  MysqlBasic()
    mysqlBasic.saveToDb()


