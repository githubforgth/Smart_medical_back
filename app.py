#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/4/29 下午7:23
# @Author : Gao_Taiheng
# @File : app.py
from flask import Flask, jsonify, request
import mysql.connector
import traceback
import datetime
from sql_operation import Sql_Operation

app = Flask(__name__)

# MySQL 连接配置
db_config = {
    'user': 'root',
    'password': '123456',
    'host': 'localhost',
    'database': 'doctor',
    'raise_on_warnings': True
}


def connect_db(**db_config):
    # 连接 MySQL 数据库
    cnx = mysql.connector.connect(**db_config)
    # 创建一个游标
    cursor = cnx.cursor()
    return cnx, cursor


@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    print(message)
    return message


@app.route('/doctor_info')
def get_doctor_info():
    cnx = mysql.connector.connect(**db_config)
    # 创建一个游标
    cursor = cnx.cursor()
    cursor.execute('SELECT * FROM doctor_info where id = "1"  ')
    results = cursor.fetchall()
    for row in results:
        info_item = {
            'name': row[0],
            'age': row[1],
            'id': row[2],
            'gender': row[3],
            'motto': row[4],
            'headshot': row[5]
        }
    cnx.close()
    if cursor.rowcount == 0:
        print("SORRY")
    else:
        print("YES")
    return jsonify(info_item)


@app.route('/todolist')
def get_todo():
    today_date = datetime.date.today()
    cnx = mysql.connector.connect(**db_config)
    # 创建一个游标
    cursor = cnx.cursor()
    sql = 'SELECT * FROM todolist where date = "2023-05-04"'
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


def search(table, keyword, value):
    cnx = mysql.connector.connect(**db_config)
    # 创建一个游标
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM %s WHERE %s= %s" % (table, keyword, value))
    res = cursor.fetchall()
    cnx.close()
    return res


def search_all(table):
    cnx = mysql.connector.connect(**db_config)
    # 创建一个游标
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM %s " % table)
    res = cursor.fetchall()
    cnx.close()
    return res


@app.route("/search_painter")
def search_painter():
    keyword = request.args.get("keyword")
    print(keyword)
    try:
        res = search("patient_info", "patient_name", f"'{keyword}'")
        response = []
        for n in res:
            response.append(n[0])
        if len(response) != 0:
            return jsonify(response)
        else:
            return jsonify(["抱歉 未找到"])
    except:
        return jsonify(['Not found'])


@app.route("/medical_record")
def media_recorder():
    pass


@app.route("/show_medical")
def show_media_recorder():
    res = search_all('medical_records')
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
                         "medical_history": temp_media[6]
                         })
    return jsonify(response)


@app.route("/medical_info")
def medical_info():
    keyword = request.args.get("id")
    response = search("medical_records", 'id', keyword)
    print(response)
    response = response[0]
    res = {"id": response[0],
           "name": response[1],
           "gender": response[2],
           "age": response[3],
           "contact_info": response[4],
           "condition_description": response[5],
           "medical_history": response[6],
           "allergy_history": response[7]
           }
    print(res)
    return jsonify(res)


@app.route("/person_setting")
def person_settings():
    column = request.args.get("key_word")
    print(column)
    sql = Sql_Operation()
    stats = sql.update(table_name='doctor_info', change_table={'name': 'John'}, condition={"name": "John Doe"})
    if stats:
        return "success"
    else:
        return "sorry"


if __name__ == '__main__':
    app.run(debug=True)
