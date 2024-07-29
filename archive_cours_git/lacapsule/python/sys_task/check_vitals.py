#!/usr/bin/python3

import datetime
import os
import psutil

path = "/home/jme/la_capsule/python_files/sys_task/"

def check_space(drive_path = path):    
    return psutil.disk_usage(drive_path).percent

def check_cpu():    
    # return psutil.cpu_percent()
    return os.cpu_count()

def check_ram():
    return psutil.virtual_memory().percent

message = ("Disk {} \n usage : {} \n cpu % : {} \n ram % : {} \n ------------------------- \n".format(path, check_space(path), check_cpu(), check_ram()))

with open(path + "logs/vitals.log", "a") as file:
    file.write(str(datetime.datetime.now() )+ "\n" + message)