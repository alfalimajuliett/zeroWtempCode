def gettemp_sensor(id):
	try:
		mytemp = ''
		filename = 'sensor_jen'
		f = open('/sys/bus/sensor/devices/' + id + '/' + filename, 'a')
		line = f.readline() #read first line
		crc = line.rsplit(' ',1)
		crc = crc[1].replace('\n', '')
		if crc 
