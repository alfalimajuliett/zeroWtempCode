#!/usr/bin/env python

import os
import subprocess
import glob
import time
from gpiozero import CPUTemperature
from crontab import CronTab

empty_cron    = CronTab()
my_user_cron  = CronTab(user=True)
users_cron    = CronTab(user='username')

system_cron = CronTab(tabfile='/etc/crontab', user=False)
job = system_cron[0]
job.user != None
system_cron.new(command='new_command', user='root')

job  = cron.new(command='/usr/bin/echo')#changes_in_repo
job.hour.every(2)

###python git code example####
def changes_in_repo():
    return subprocess.call("git diff --exit-code --quiet".split()) != 0

os.chdir(REPO_DIR)

if not os.path.isdir(REPO_DIR + os.sep + ".git"):
  subprocess.call("git init".split())
  with open(".gitignore", "w") as f:
    f.write("*\n")
  subprocess.call("git add -f .gitignore pending.data completed.data".split())
  subprocess.call(["git", "commit", "-mInitial log"])

if changes_in_repo():
  subprocess.call("git commit -a".split() + ["-m" + c['args']])

  # Only push every 2 minutes:
  stdout, _ = subprocess.Popen("git log origin/master.. --oneline --before=2minutes".split(), stdout=subprocess.PIPE).communicate()
  if stdout and False:
      subprocess.call(["git", "push"])
###python git code example###

cpu = CPUTemperature()
current_time = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())

def make_csv_line():
    return ",".join([current_time, str(cpu.temperature), str(read_temp())])+"\n"

def append_csv():
	with open("temp.csv", 'a') as f:
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

def changes_in_repo():
    return subprocess.call("git diff --exit-code --quiet".split()) != 0

    os.chdir(REPO_DIR)

    if not os.path.isdir(REPO_DIR + os.sep + ".git"):
        subprocess.call("git init".split())
        with open(".gitignore", "w") as f:
            f.write("*\n")
        subprocess.call("git add -f .gitignore pending.data completed.data".split())
        subprocess.call(["git", "commit", "-mInitial log"])

    if changes_in_repo():
        subprocess.call("git commit -a".split() + ["-m" + c['args']])

        # Only push every 2 minutes:
        stdout, _ = subprocess.Popen("git log origin/master.. --oneline --before=2minutes".split(), stdout=subprocess.PIPE).communicate()
        if stdout and False:
            subprocess.call(["git", "push"])

if __name__ == '__main__':
    append_csv()
