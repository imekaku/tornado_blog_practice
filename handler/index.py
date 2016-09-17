#!/usr/bin/env python
#coding:utf-8

# filename: ./handler/index.py
# description: This is file for IndexHandler

import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", page_title = "index")