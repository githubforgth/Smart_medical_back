#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/5/10 下午5:16
# @Author : Gao_Taiheng
# @File : api.py
import api.config
import mysql.connector
from flask import request, jsonify
# from sql_operation import Sql_Operation
import api.sql_operation
import datetime

sql = api.sql_operation.Sql_Operation()

db = api.config.db_config


def connect_db(**db_config):
    # 连接 MySQL 数据库
    cnx = mysql.connector.connect(**db_config)
    # 创建一个游标
    cursor = cnx.cursor()
    return cnx, cursor


# TODO: 数据加密
def login():
    account_id = request.args.get('account_id')
    password = request.args.get('password')
    print(account_id, password)
    response = sql.search(table='doctor_table', keyword=["account_id", "password"], value=[account_id, password],
                          model=True)
    print(response)
    return jsonify(response)


# 查询医生信息
def get_doctor_info_1():
    cnx, cursor = connect_db(**db)
    keyword = request.args.get("open_id")
    print(f"open_id:{keyword}")
    cursor.execute(f'SELECT * FROM doctor_table  where _openid = "{keyword}" ')
    result = cursor.fetchall()[0]
    headers = [i[0] for i in cursor.description]
    res = dict(zip(headers, result))
    print(res)
    return jsonify(res)


# 查询病历
def medical_info():
    keyword = request.args.get("id")
    # sql = Sql_Operation()
    response = sql.search("medical_records", ['id'], [keyword])
    print(response)
    response = response[0]
    res = {"id": response[0],
           "name": response[1],
           "gender": response[2],
           "age": response[3],
           "contact_info": response[4],
           "condition_description": response[5],
           "medical_history": response[6],
           "allergy_history": response[7],
           "situation":response[8],

           }
    print(res)
    return jsonify(res)


def person_settings():
    title = request.args.get("barTitle")
    column = request.args.get("keyword")
    open_id = request.args.get("open_id")
    print("Setting: ", column, open_id, title)
    # print(column)
    # sql = Sql_Operation()
    stats = sql.update(table_name='doctor_table', change_table={f'{title}': f'{column}'},
                       condition={"_openid": open_id})
    print("stats: ", stats)
    if stats:
        return "success"
    else:
        return "sorry"


def show_media_recorder():
    # sql = Sql_Operation()
    res = sql.search_all('medical_records')
    response = []
    print(res)
    for media in range(min(5, len(res))):
        temp_media = res[media]
        response.append({"id": temp_media[0],
                         "name": temp_media[1],
                         "gender": temp_media[2],
                         "age": temp_media[3],
                         "contact_info": temp_media[4],
                         "condition_description": temp_media[5],
                         "medical_history": temp_media[6],
                         "station": temp_media[8],
                         "medical": temp_media[9]
                         })
    print(response)
    return jsonify(response)


# 查找病人
def search_painter():
    keyword = request.args.get("keyword")
    print(keyword)
    try:
        # sql = Sql_Operation()
        res = sql.search("medical_records", ["name"], [keyword])
        response = []
        print(res)
        for n in res:
            response.append(n)
        if len(response) != 0:
            return jsonify(response)
        else:
            return jsonify({res: "抱歉 未找到"})
    except:
        return jsonify(['Not found'])


def get_todo():
    today_date = datetime.date.today()
    cnx = mysql.connector.connect(**api.config.db_config)
    # 创建一个游标
    cursor = cnx.cursor()
    keyword = request.args.get('id')
    print(keyword)
    sql = f'SELECT * FROM todolist where id = "{keyword}"  '
    cursor.execute(sql)
    results = cursor.fetchall()[0]
    print(results)
    res = \
        {
            "id": results[0],
            "time": str(results[1]),
            "todo_item": results[2]
        }

    cnx.close()
    return jsonify(res)


def send_message():
    # 获取数据
    message = request.args.get("massage")
    # sql_operation()
    return jsonify(message)


def register_search():
    value = request.args.get("account_id")
    response = sql.search(table='doctor_table', keyword=["account_id"], value=[value])
    print(response)
    if len(response) == 0:
        return "1"
    else:
        return "0"


def register():
    data = request.args.get("data")
    # print("data", data)
    # print(type(data))
    data = data[1:-1].split(",")
    print(data)
    sql.ADD('doctor_table', tuple(data))
    return jsonify(True)


def submit_medical():
    condition = request.args.get('condition')
    medical = request.args.get('medical')
    patient_id = request.args.get('id')
    state = sql.update("medical_records", {"situation": condition, "medical": medical}, {"id": patient_id})
    if state:
        return jsonify({"state": True})
    else:
        return jsonify({"state": False})


'''
+----------------------------------------+
message_id   id_1   id_2   message   time
mysql> CREATE TABLE messages (
    ->   message_id INT AUTO_INCREMENT PRIMARY KEY,
    ->   id_1 INT NOT NULL,
    ->   id_2 INT NOT NULL,
    ->   message VARCHAR(255) NOT NULL,
    ->   time DATETIME NOT NULL,
    ->   state BOOLEAN NOT NULL DEFAULT FALSE);
+----------------------------------------+
'''


# TODO: 1.读取数据
def show_massage():
    doctor_id = request.args.get("doctor_id")
    cnx = mysql.connector.connect(**api.config.db_config)
    cursor = cnx.cursor()
    sql = f"SELECT id_2, MAX(time) AS latest_time, message FROM messages WHERE id_1 = {doctor_id} GROUP BY id_2;"
    cursor.execute(sql)
    res = cursor.fetchall()
    print(res)
    return jsonify(res)


def chat_massage():
    cnx = mysql.connector.connect(**api.config.db_config)
    cursor = cnx.cursor()
    id_1 = request.args.get("id")
    id_2 = request.args.get("id_2")
    sql_l = f" SELECT * FROM messages WHERE id_1 = '{id_1}' AND id_2 = '{id_2}' ORDER BY time DESC "
    cursor.execute(sql_l)
    res = cursor.fetchall()
    cnx.close()
    cursor.close()
    return jsonify(res)


def chat_submit():
    cnx = mysql.connector.connect(**api.config.db_config)
    cursor = cnx.cursor()
    id_1 = request.args.get("id_1")
    id_2 = request.args.get("id_2")
    massage = request.args.get("massage")
    now = datetime.datetime.now()
    columns = sql.get_head("messages")
    print(columns, id_1, id_2, massage, now)
    sql_l = f"INSERT INTO messages ({', '.join(columns)}) VALUES ({id_1}, {id_2}, '{massage}', '{now}', '{0}')"
    print(sql_l)
    cursor.execute(sql_l)
    cnx.commit()
    cnx.close()
    cursor.close()
    if cursor.rowcount == 0:
        return jsonify({"state": False})
    else:
        return jsonify({"state": True})


def show_media_recorder_all():
    # sql = Sql_Operation()
    res = sql.search_all('medical_records')
    response = []
    print(res)
    for media in range(len(res)):
        temp_media = res[media]
        response.append({"id": temp_media[0],
                         "name": temp_media[1],
                         "gender": temp_media[2],
                         "age": temp_media[3],
                         "contact_info": temp_media[4],
                         "condition_description": temp_media[5],
                         "medical_history": temp_media[6],
                         "station": temp_media[8],
                         "medical": temp_media[9]
                         })
    return jsonify(response)
