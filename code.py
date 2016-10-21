#!/usr/bin/env python

from jinja2 import Environment,FileSystemLoader
import webbrowser
import csv
import sys
import threading
import re
import time
import os
import signal
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify as notify

class CountdownTask(threading.Thread):
    def __init__(self,target):
        self._target=target
        threading.Thread.__init__(self)
        self._stopevent = threading.Event( )
        self._running = True

    def terminate(self):
        self._stopevent.set( )

    def run(self):
        self._target()
file_address = '/home/deathnote/Desktop/d/python_project/cat/'
def brow():
    url='file://'+file_address+'html/code.html'
    webbrowser.open(url,new=1)
    pass

APPINDICATOR_ID = 'myappindicator'
answer,Flag,position,end,current_position=open(file_address+'data/answer.txt','r').read().split(',')
Flag=int(Flag)
position=int(position)
end=int(end)
current_position=int(current_position)
increment=10
super_Flag=0
def tests():
    global Flag,answer,increment,position
    if(Flag==1 ):
        print "ho yaah"
        templateLoader = FileSystemLoader( searchpath="/" )
        env = Environment(loader=templateLoader)
        js=env.get_template(file_address+'ori.js')
        t=env.get_template(file_address+'html/check.html')
        g=open(file_address+'database.csv','r')
        greader = csv.reader(g)
        greader=[i for i in greader][position:increment+position]
        ans=answer[position:increment+position]
        f=open(file_address+'html/code.html','w')
        k=open(file_address+'quiz-1.js','w')
        f.write(t.render(greader=greader,ans=ans,pos=position))
        k.write(js.render(ans=ans))
        t = CountdownTask(target=brow)
        t.start()
        t.terminate() # Signal termination
        #t.join()      # Wait for actual termination (if needed)
        position+=increment
        Flag=0

def notification():
    global Flag,current_position,position
    if(Flag==0 and not t1._stopevent.isSet( )):
        f=open(file_address+'word+meaning.csv', 'r')
        reader = [row for index,row in enumerate(csv.reader(f)) if(index>=current_position and index<position*5+increment+40)]
        for row in reader:
            if t1._stopevent.isSet( ):
                return
            if row[1].find('[')>0:
                current_position+=1
                continue
            notify.Notification.new(row[0],row[1]).show()
            current_position+=1
            time.sleep(10)
        Flag=1
    #notify.notification.new('Take Test','If not willing to give test press STOP NOTIFICATION MENU')
    tests()
    print "its done!!"
    
def databasewite():
    global answer,Flag,position,end,current_position
    while not t3._stopevent.isSet( ):
        time.sleep(1)
        f=open(file_address+'data/answer.txt','w')
        f.write(answer+","+str(Flag)+","+str(position)+","+str(end)+","+str(current_position))
        f.close()
        #if kill_bomb==1:
         #   break
        pass

t1 = CountdownTask(target=notification)
t1.setDaemon(True)
t3 = CountdownTask(target=databasewite)
t3.setDaemon(True)

def Start_notification(_):
    global t1,t2,t3
    t3.__init__(target=databasewite)
    t1.__init__(target=notification)
    t3.start()
    t1.start()
    pass

def Stop_notification(_):
    global t1,t2,t3
    #if(super_Flag==1):
    print "ya i am here"
    #kill_bomb=1
    if t1.isAlive():
        #t1.kill()
        t1.terminate()
        #t1.join()
    if t3.isAlive():
        #t1.kill()
        t3.terminate()
        #t2.join()
    #super_Flag=0
    print "pata nahi..!"
    pass

def build_menu():
    menu = gtk.Menu()
    item_start = gtk.MenuItem('Start Notification')
    item_start.connect('activate', Start_notification)
    menu.append(item_start)
    item_stop = gtk.MenuItem('Stop Notification')
    item_stop.connect('activate', Stop_notification)
    menu.append(item_stop)
    item_quit = gtk.MenuItem('Quit')
    item_quit.connect('activate', quit)
    menu.append(item_quit)
    menu.show_all()
    return menu

def quit(_):
    Stop_notification(_)
    notify.uninit()
    gtk.main_quit()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, file_address+'logo.png', appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    notify.init(APPINDICATOR_ID)
    gtk.main()
    pass