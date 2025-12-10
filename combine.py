fd_gps = open("1_parsed.log")
fd_rtt = open("2_parsed.log")

lines1 = fd_gps.readlines()
lines2 = fd_rtt.readlines()

for l2 in lines2:
	p2 = l2.split(",")
	min1 = 10000000000000
	out1 = None
	out2 = None
	for l1 in lines1:
		p1 = l1.split(",")
		if abs(float(p1[0]) - float(p2[0])) < min1 and abs(float(p1[0]) - float(p2[0])) < 5:
			out2 = l2
			out1 = l1
	if out2 and out1:
		print(out1.strip() + "," + out2.split(",")[1].strip())
