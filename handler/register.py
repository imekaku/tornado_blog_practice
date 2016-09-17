#!/usr/bin/env python
#coding:utf-8

import tornado.web
import MySQLdb
class RegisterHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("register.html", page_title = "Register Page")

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        self.insertIntoDatabase(username, password)
        self.render("welcome.html", username=username, page_title = "Welcome Page")

    def insertIntoDatabase(self, username, password):
        conn = MySQLdb.connect(host='localhost', user='root', passwd='123456', db='tornado_blog_01')
        cur = conn.cursor()
        sql_insert = "insert into user(username, password) values(\""+username+"\",\""+password+"\")"
        cur.execute(sql_insert)
        conn.commit()
        conn.close()