#!/usr/bin/env python
#coding:utf-8

# filename: ./application.py
# description: This file is for create a new application

import tornado.web

from setting import setting
from router import urls

class Application(tornado.web.Application):
    def __init__(self):
        handlers = urls
        tornado.web.Application.__init__(self, handlers, **setting)