import pynmea2

with open("1.log") as fd:
	lines = fd.readlines()
	for l in lines:
		p = l.split("GPRMC")
		#print("$GPRMC" + p[1])
		msg = pynmea2.parse("$GPRMC" + p[1])
		print(f"{p[0].split('$')[0].strip()},{msg.latitude},{msg.longitude}")
