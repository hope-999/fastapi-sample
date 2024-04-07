"""
实用工具

Mysql 数据库连接，执行sql语句

Redis 数据库连接，执行缓存增删改查
"""
from typing import Set

import pymysql
import redis
from dbutils.pooled_db import PooledDB
from redis.typing import EncodableT, KeysT, PatternT

from app import settings
from app.logger import logger


class MysqlDB(object):
    def __init__(self,
                 host=settings.XIAOE_TESTING_PLATFORM_MYSQL_HOST,
                 port=int(settings.XIAOE_TESTING_PLATFORM_MYSQL_PORT),
                 user=settings.XIAOE_TESTING_PLATFORM_MYSQL_USER,
                 password=settings.XIAOE_TESTING_PLATFORM_MYSQL_PASSWORD,
                 database=settings.XIAOE_TESTING_PLATFORM_MYSQL_DB
                 ):
        self.db_pool = None
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    async def connect_to_mysql(self):
        self.db_pool = PooledDB(
            creator=pymysql,
            maxshared=settings.MYSQL_MAX_SHARED,
            maxconnections=settings.MYSQL_MAX_CONNECTIONS,
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database,
            charset=settings.MYSQL_CHARSET
        )

    def mysql_get_sql_result(self, sql) -> list:
        """连接数据库并执行 SQL 查询"""
        cursor = None
        con = None

        try:
            # 从连接池中获取一个数据库连接对象
            con = self.db_pool.connection()
            # 创建游标对象
            cursor = con.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()  # 通过fetchall方法获得数据
            # return [list(i) for i in results]
            return results
        except Exception as e:
            logger.exception(f"错误： {str(e)}")
        finally:
            cursor.close()
            con.close()

    def insert_data(self, sql: str):
        """插入数据"""
        cursor = None
        con = None
        try:
            logger.debug(f'[数据库插入数据] sql={sql}')
            # 从连接池中获取一个数据库连接对象
            con = self.db_pool.connection()
            # 创建游标对象
            cursor = con.cursor()
            rows = cursor.execute(sql)
            # 提交事务
            con.commit()
            logger.info(f'[数据库插入数据] rows={rows}')
        except pymysql.err.IntegrityError as e:
            logger.info(f'插入数据重复: {e.__str__()}')
        except Exception as e:
            logger.exception(f'执行sql错误:{e.__str__()}')

        finally:
            cursor.close()
            con.close()

    async def close_mysql_connection(self):
        if self.db_pool:
            self.db_pool.close()


class RedisDB(object):
    pool = redis.ConnectionPool(
        host=settings.RDB_HOST,
        password=settings.RDB_PASSWORD,
        port=settings.RDB_PORT
    )

    def set(self, k, v, ex=60):
        try:
            r = redis.Redis(connection_pool=self.pool)
            r.set(k, v, ex=ex)
            logger.info(f'[Redis] 添加key成功: {k}={v}')
        except Exception as e:
            logger.exception(f'添加Redis key错误:{e.__str__()}')

    def get(self, k):
        try:
            r = redis.Redis(connection_pool=self.pool)
            result_b = r.get(k)
            result = result_b.decode('utf-8') if result_b else result_b
            logger.info(f'[Redis] 获取key成功: {k}={result}')
            return result
        except Exception as e:
            logger.exception(f'获取Redis key错误:{e.__str__()}')

    def list_push(self, k, values: list, ex=60):
        try:
            r = redis.Redis(connection_pool=self.pool)
            r.rpush(k, *values)
            # 设置过期时间
            r.expire(k, ex)
            logger.info(f'[Redis] 添加key成功: {k}={values}')
        except Exception as e:
            logger.exception(f'添加Redis key错误:{e.__str__()}')

    def list_range(self, k, start: int, end: int):
        try:
            r = redis.Redis(connection_pool=self.pool)
            result_b = r.lrange(k, start, end)
            results = [i.decode('utf-8') for i in result_b]
            logger.info(f'[Redis] 查询key成功: {k}={results}')
            return results
        except Exception as e:
            logger.exception(f'[Redis] 查询Redis key错误:{e.__str__()}')

    def set_add(self, k, values: Set, ex=60 * 10):
        """ 向集合中添加数据 """
        try:
            r = redis.Redis(connection_pool=self.pool)
            for v in values:
                r.sadd(k, v)
            r.expire(k, ex)
            logger.info(f'[Redis] 添加set key成功: {k}={values}')
        except Exception as e:
            logger.exception(f'[Redis] 添加Redis set key错误:{e.__str__()}')

    def set_members(self, k):
        """ 获取k的所有成员 """
        try:
            results = set()
            r = redis.Redis(connection_pool=self.pool)
            result_b = r.smembers(k)
            if result_b:
                results = set([i.decode('utf-8') for i in result_b])
            logger.debug(f'[Redis] 获取set key成功: {k}={results}')
            return results
        except Exception as e:
            logger.exception(f'[Redis] 添加Redis set key错误:{e.__str__()}')

    def set_sismember(self, k, v):
        """ 集合数据类型中，判断成员v是否在k中 """
        r = redis.Redis(connection_pool=self.pool)
        return r.sismember(k, v)

    def set_delete(self, k):
        """ 删除整个集合 """
        r = redis.Redis(connection_pool=self.pool)
        r.delete(k)

    def set_scard(self, k):
        """ 获取集合长度
        :param k:
        :return:
        """
        r = redis.Redis(connection_pool=self.pool)
        return r.scard(k)

    def set_sadd(self, k, values, ex: int = 60 * 60):
        """

        :param k:
        :param values:
        :param ex:
        """
        r = redis.Redis(connection_pool=self.pool)
        r.sadd(k, *values)
        r.expire(k, ex)

    def delete(self, k):
        r = redis.Redis(connection_pool=self.pool)
        r.delete(k)

    def keys(self, pattern: PatternT = "*", **kwargs):
        r = redis.Redis(connection_pool=self.pool)
        return r.keys(pattern, **kwargs)

    def mget(self, keys: KeysT, *args: EncodableT):
        r = redis.Redis(connection_pool=self.pool)
        return r.mget(keys, *args)
