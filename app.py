#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/4/29 下午7:23
# @Author : Gao_Taiheng
# @File : app.py
from flask import Flask
from api import api

app = Flask(__name__)


@app.route("/login")
def login():
    response = api.login()
    return response


# 显示待办
@app.route('/todolist')
def get_todo():
    response = api.get_todo()
    return response


# 查询病人是否存在Counter()最大
@app.route("/search_painter")
def search_painter():
    response = api.search_painter()
    return response


@app.route("/medical_record")
def media_recorder():
    pass


# 首页显示病人卡片
@app.route("/show_medical")
def show_media_recorder():
    response = api.show_media_recorder()
    return response


@app.route("/show_medical_all")
def show_media_recorder_all():
    response = api.show_media_recorder_all()
    return response


# 返回病历
@app.route("/medical_info")
def medical_info():
    response = api.medical_info()
    return response


# 个人设置
@app.route("/person_setting", methods=["GET"])
def person_settings():
    response = api.person_settings()
    return response


@app.route("/test_2")
def test():
    t = api.get_doctor_info_1()
    return t


@app.route("/register/search")
def register_search():
    response = api.register_search()
    print("search_register", response)
    return response


@app.route("/register/submit")
def register():
    res = api.register()
    return res


@app.route("/submit_medical")
def submit_medical():
    response = api.submit_medical()
    return response


@app.route("/show_massage")
def show_massage():
    return api.show_massage()


@app.route("/massage_list")
def massage_list():
    return api.chat_massage()


@app.route("/chat_submit")
def chat_submit():
    return api.chat_submit()


if __name__ == '__main__':
    app.run(debug=True)
