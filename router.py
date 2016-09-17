#!/usr/bin/env python
#coding:utf-8

# filename: ./router.py
# description: This is file is for router file

import sys

from handler.index import IndexHandler
from handler.login import LoginHandler
from handler.register import RegisterHandler
from handler.temp import TempHandler

# avoid chinese annotate bringing about bad tings
reload(sys)
sys.setdefaultencoding('utf-8')

urls = [
(r"/", IndexHandler),
(r"/login", LoginHandler),
(r"/register", RegisterHandler),
(r"/temp", TempHandler)
]