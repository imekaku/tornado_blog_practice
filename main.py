#!/usr/bin/env python
#coding:utf-8

# filename: ./main.py
# description: This is file for Start web server

import tornado.httpserver
import tornado.ioloop
import tornado.options
from tornado.options import define, options

from application import Application
from setting import LISTEN_PORT

#define("port", default=8000, help="run on the given port", type=int)

def main():
#    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(LISTEN_PORT)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()