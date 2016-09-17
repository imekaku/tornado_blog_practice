#!/usr/bin/env python
#coding:utf-8

import tornado.web

class TempHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        user = self.get_secure_cookie("user")
        return user

    def get(self):
        if not self.current_user:
            self.redirect("/login")
            return
        self.render("temp.html", page_title = "temp")