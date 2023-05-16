#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/5/9 下午3:27
# @Author : Gao_Taiheng
# @File : sql_operation.py
import mysql.connector

import api.config


class Sql_Operation:
    # MySQL 连接配置
    def __init__(self):
        self.db_config = {
            'user': 'root',
            'password': '123456',
            'host': 'localhost',
            'database': 'doctor',
            'raise_on_warnings': True
        }

    def update(self, table_name, change_table: dict, condition: dict):
        if not table_name or not change_table or not isinstance(change_table, dict):
            raise ValueError('Please provide a valid table name and change table')

        if condition and not isinstance(condition, dict):
            raise ValueError('Please provide a valid condition')

        cnx = mysql.connector.connect(**self.db_config)
        cursor = cnx.cursor()
        try:
            sql = f' UPDATE {table_name} SET '
            change = []
            for column, value in change_table.items():
                change.append(f"{column} ='{value}'")
            sql += ",".join(change) + " "

            where_clauses = []
            for key, value in condition.items():
                where_clauses.append(f"{key} = '{value}'")
            if where_clauses:
                sql += "WHERE " + ' AND '.join(where_clauses)
                print(where_clauses, sql)
            cursor.execute(sql)
            cnx.commit()
            cursor.close()
            cnx.close()
            if cursor.rowcount == 0:
                return False
            else:
                return True

        except mysql.connector.Error as error:
            print(f"Failed to update table {table_name}: {error}")
            return False

        finally:
            cursor.close()
            cnx.close()

    # 查询
    def search(self, table, keyword: list, value: list, model=False):
        cnx = mysql.connector.connect(**self.db_config)
        # 创建一个游标
        cursor = cnx.cursor()
        if len(keyword) != len(value):
            return False
        # n = len(keyword)
        print(keyword, value)
        # limit = " AND ".join([f"{keyword[_]} = '{value[_]}'" for _ in range(n)])
        sql = f"SELECT * FROM {table} WHERE " + " AND ".join([f"{k} = %s" for k in keyword])
        print(sql, value)
        cursor.execute(sql, value)
        res = cursor.fetchall()
        cnx.close()
        cursor.close()
        if model:
            return dict(zip([i[0] for i in cursor.description], res[0]))
        else:
            return res

    # 查询所有元素
    def search_all(self, table):
        cnx = mysql.connector.connect(**self.db_config)
        # 创建一个游标
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM %s " % table)
        res = cursor.fetchall()
        cnx.close()
        cursor.close()
        return res

    def DELETE(self, table, keys: list, values: list):
        cnx = mysql.connector.connect(**self.db_config)
        cursor = cnx.cursor()
        n = len(keys)
        if n != values:
            cursor.close()
            cnx.close()
            return False
        if n != 0:
            limit = "WHERE" + " AND ".join([f"{keys[_]} = '{values[_]}'" for _ in range(n)])
        else:
            limit = ""
        sql = f"DELETE FROM {table} " + limit
        cursor.execute(sql)
        cnx.commit()
        print(cnx.rollback())
        cursor.close()
        cnx.close()
        return True

    def get_head(self, table):
        cnx = mysql.connector.connect(**self.db_config)
        cursor = cnx.cursor()
        # 获取表头信息
        cursor.execute(f"SELECT * FROM {table} LIMIT 0")
        columns = cursor.column_names[1:]
        print(columns)
        cnx.close()
        cursor.close()
        return columns

    def ADD(self, table, data):
        cnx = mysql.connector.connect(**self.db_config)
        cursor = cnx.cursor()

        columns = self.get_head(table)
        print(len(data), len(columns))
        # 构造SQL语句
        placeholders = ', '.join(['%s' for _ in columns])
        sql = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({placeholders})"
        print(sql)
        # 执行SQL语句
        cursor.execute(sql, data)
        cnx.commit()

        cursor.close()
        cnx.close()
        return True
