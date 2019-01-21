#!/usr/bin/env python
#python will ignore this ^ but the shell will not
import os
import subprocess
import glob
import time
from gpiozero import CPUTemperature
from crontab import CronTab
from contextlib import contextmanager

CODE_REPO = os.path.dirname(os.path.abspath(__file__))
DATA_REPO = os.path.join(os.path.dirname(CODE_REPO),"QlabTempData")

def install():
    cron = CronTab()
    job = cron.new(command = os.path.abspath(__file__))#magic operator for getting the path of the current file
    job.hour.every(2)
    cron.write()

###python git code example####

def run_command(command):
    subprocess.call(command.split())

def git_commit(git_repo):
    run_command("GIT_DIR="+ git_repo +" git commit -am 'Update data'")

def git_pull(git_repo):
    run_command("GIT_DIR="+ git_repo +" git pull")

def git_push(git_repo):   
    run_command("GIT_DIR="+ git_repo +" git push")
 
def update_code():
    git_pull(CODE_REPO) # what happens if the code changes?

def update_data():
    append_csv()
    git_commit(DATA_REPO)
    git_push(DATA_REPO)

###python git code example###

cpu = CPUTemperature()
current_time = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())

def make_csv_line():
    return ",".join([current_time, str(cpu.temperature), str(read_temp())])+"\n"

def append_csv():
	with open(os.path.join(DATA_REPO,"temp.csv"), 'a') as f:
		f.write(make_csv_line())

# from https://pimylifeup.com/raspberry-pi-temperature-sensor/
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0] #getting first device that starts with 28
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES': # strip returns a copy of the string with both leading and trailing characters removed
        time.sleep(0.2) #code pauses for this amount of secs
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f
# Lines[1] means we're looking at the 2nd element in the array,
#in this case, the 2nd line. Once we have the line we simply
#get all the numbers that are after the t= this is done here
#lines[1][equals_pos+2:]. Equals_pos is the start position
#of the temperature (t), and we add 2 to the position, so
#we only get the actual temperature numbers.

def main():
    if os.environ["install_temp_cron"] == "True":
        install()
    update_data()
    update_code()
    notify_healthcheck()

if __name__ == '__main__':
    main()
