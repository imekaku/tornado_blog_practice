#!/usr/bin/env python
#coding:utf-8

# filename: ./setting.py
# description: This is file is for setting of other Python Code

import os

LISTEN_HOST = '0.0.0.0'
LISTEN_PORT = 80

setting = dict(
    template_path=os.path.join(os.path.dirname(__file__),"templates"),
    static_path=os.path.join(os.path.dirname(__file__),"statics"),
    cookie_secret="fdsjfdsbvuw&*2327g6&^&<>djk",
    )