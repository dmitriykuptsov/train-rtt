from sys import argv
import numpy

coords = {}
print(f"Parsing the file {argv[1]}")
with open(argv[1]) as fd:
	lines = fd.readlines()
	for l in lines:
		s = l.split()
		if len(s) != 4:
			continue
		if not coords.get(s[1]):
			coords[s[1]] = {}
		if not coords[s[1]].get(s[2]):
			coords[s[1]][s[2]] = []

		coords[s[1]][s[2]].append(float(s[3]))


for key1 in list(coords.keys()):
	for key2 in list(coords[key1].keys()):
		#print(coords[key1][key2])
		std = numpy.std(coords[key1][key2])
		m   = numpy.mean(coords[key1][key2])
		l   = len(coords[key1][key2])
		print(f"{key1},{key2},{m},{std},{l}")
