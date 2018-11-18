import os
import glob
from time import localtime, strftime
from gpiozero import CPUTemperature

cpu = CPUTemperature()
current_time = strftime("%a, %d %b %Y %H:%M:%S", localtime())


def record_cpu_temp():
	with open("cpu_temp.csv", 'a') as f:
		f.write(str(current_time) +"\n")
		f.write(str(cpu.temperature) +"\n")
		
		
if __name__ == "__main__":
	record_cpu_temp()	
