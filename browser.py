#!/usr/bin/env python
#coding=utf8

__author__ = 'way'
__email__ = 'weizhe86@gmail.com'

import os,sys
import gtk
import urllib
import webkit
import time
from django.core.management import execute_from_command_line
from multiprocessing import Process

gtk.threads_init()


global port
port="6717"

def djangoserver(argv):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
    execute_from_command_line(argv)

def close(widget):
    print 'event:',widget
    server.terminate()
    gtk.main_quit()

server=Process(target=djangoserver,args=(['browser.py','runserver',port],))
server.start()

url='http://127.0.0.1:%s/'%port
win = gtk.Window(gtk.WINDOW_TOPLEVEL)
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
