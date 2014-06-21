#coding=utf8

__author__ = 'way'
__email__ = 'weizhe86@gmail.com'



import os,sys
from gi.repository import Gtk
import urllib
import webkit
import time
from django.core.management import execute_from_command_line
from threading import Thread

global port
port="6717"

class djangoservice(Thread):
    def __init__(self,argv):
        Thread.__init__(self)
        self.argv=argv
    def run(self):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
        execute_from_command_line(self.argv)

def close(widget):
    print('event:',widget)
    gtk.main_quit()

'''service=djangoservice(['','runserver',port],)
service.setDaemon(True)
service.start()'''

url='http://127.0.0.1:%s/'%port
win = Gtk.Window()
win.set_size_request(300,600)
win.connect("delete-event", Gtk.main_quit)
sw = Gtk.ScrolledWindow()
win.add(sw)

view = webkit.WebView()
sw.add(view)
'''while True:
    try:
        urllib.urlopen(url)
        break
    except Exception as err:
        print err
        time.sleep(0.1)'''
view.open(url)

win.show_all()
Gtk.main()