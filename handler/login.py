#!/usr/bin/env python
#coding:utf-8

import tornado.web
import MySQLdb

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("login.html", page_title="Login Page")

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        
        if self.check(username, password):
            self.set_secure_cookie("user", username)
            self.render("welcome.html", username=username, page_title = "Welcome Page")
        else:
            self.render("bad.html", page_title="Bad Page")

    def check(self, username, password):
        conn = MySQLdb.connect(host='localhost', user='root', passwd='123456', db='tornado_blog_01')
        cur = conn.cursor()
        sql_select = "select password from user where username = '"+username+"'"
        cur.execute(sql_select)
        db_password = cur.fetchone()
        if not db_password:
            return False
        if db_password[0] != password:
            return False
        else:
            return True