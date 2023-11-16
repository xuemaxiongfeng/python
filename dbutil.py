# -*- coding:utf-8 -*-

import pymysql
from log import Logger

class DBUtil(object):
    #连接池
    conns_pool = {'host':'127.0.0.1', 'port':'3306', 'user':'news-user', 'pwd':'news-user123456789', 'db':'news', 'charset':'utf8mb4',
               "autocommit": True,
               "mincached": 10,         # 启动时开启的闲置连接数量(缺省值 0 开始时不创建连接)
               "maxconnections": 70,    # 连接池最大连接数量
               "maxcached": 10,         # 连接池中允许的闲置的最多连接数量
               "maxshared": 10,         # 共享连接数允许的最大数量(缺省值 0 代表所有连接都是专用的)如果达到了最大数量,被请求为共享的连接将会被共享使用
               "blocking": True,        # 设置在连接池达到最大数量时的行为(缺省值 0 或 False 代表返回一个错误<toMany......> 其他代表阻塞直到连接数减少,连接被分配)
               "maxusage": 0,           # 单个连接的最大允许复用次数(缺省值 0 或 False 代表不限制的复用).当达到最大数时,连接会自动重新连接(关闭和重新打开)
               "setsession": [],        # 一个可选的SQL命令列表用于准备每个会话，如["set datestyle to german", ...]，常用于做初始化命令
               "cursorclass": pymysql.cursors.DictCursor  # 返回类型，dict
               }

    #单独连接
    conn_local = {'host':'localhost', 'port':3306, 'user':'news-user', 'password':'news-user123456789', 'db':'news', 'charset':'utf8mb4'}


    conn = None
    @classmethod
    def __get_conn(cls):
        logger = Logger(file='database.log')
        try:
            cls.conn = pymysql.connect(host=cls.conn_local['host'], port=cls.conn_local['port'], user=cls.conn_local['user'], password=cls.conn_local['password'], database=cls.conn_local['db'], charset=cls.conn_local['charset'])
            return cls.conn
        except Exception as err:
            logger.error('Connect database failed:' + str.format(err))
            cls.conn = None
        finally:
            del logger

    @classmethod
    def __close_conn(cls):
        logger = Logger(file='database.log')
        try:
            if cls.conn is not None:
                cls.conn.close()
                cls.conn = None
        except Exception as err:
            logger.error('Close database failed:' + str.format(err))
        finally:
            del logger



    @classmethod
    def get_conn(cls):
        cls. __get_conn()



    @classmethod
    def uids_many(cls, sql, params):
        logger = Logger(file='database.log')
        cursor = None
        try:
            if not isinstance(params, list):
                logger.error('Op databse, the arg:params is not a list:' + str.format(params))
                return False
            cls.conn = cls.__get_conn()         #获取连接
            cursor = cls.conn.cursor()          #获取游标
            cursor.executemany(sql, params)     #操作sql
            cls.conn.commit()                   #提交
        except Exception as err:
            #logger.debug(err)
            logger.error('' + str.format(err))
            cls.conn.rollback()             #回滚
            return False
        else:
            return True
        finally:
            if cursor is not None:
                cursor.close()
            cls.__close_conn()
            del logger






