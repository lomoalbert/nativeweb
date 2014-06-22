#!/usr/bin/env python
#coding=utf8

__author__ = 'way'
__email__ = 'weizhe86@gmail.com'

import os,sys
import gtk
import urllib
import webkit
import time
from multiprocessing import Process
from paste import httpserver
from backend.wsgi import application

gtk.threads_init()

global port
port="6717"


server=Process(target=httpserver.serve,args=(application, '127.0.0.1', port))
server.daemon=True
server.start()


def close(widget):
    print 'event:',widget
    gtk.main_quit()

url='http://127.0.0.1:%s/music/'%port
win = gtk.Window()
print win
win.set_default_size(300,600)
win.connect("destroy",close)
sw = gtk.ScrolledWindow()
view = webkit.WebView()
sw.add(view)
win.add(sw)
win.show_all()
while True:
    try:
        urllib.urlopen(url)
        break
    except Exception as err:
        print err
        time.sleep(0.1)
view.open(url)
gtk.main()
