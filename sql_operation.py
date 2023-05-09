#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/5/9 下午3:27
# @Author : Gao_Taiheng
# @File : sql_operation.py
#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/5/7 下午8:26
# @Author : Gao_Taiheng
# @File : sql_operation.py
import mysql.connector


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
                sql += "WHERE "+' AND '.join(where_clauses)
                print(where_clauses, sql)
            cursor.execute(sql)

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


if __name__ == "__main__":
    pass
