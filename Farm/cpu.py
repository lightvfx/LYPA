#!/usr/bin/env python
import os,sys
import todo
from threading import Timer

def main():
    # Init the database before doing anything else
    todo.initDB()
    for task in todo.Task.query().all():
        #print task.done
        if task.done == 0:
            task.done = 1
            todo.saveData()
            print "rendering: " + task.text
            print "finished"
            
        else :
            print "waiting ...... "
    t = Timer(5.0,main)
    t.start()
    
            

if __name__ == "__main__":
    t = Timer(5.0,main)
    t.start()
    
