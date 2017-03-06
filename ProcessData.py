import numpy as np
import matplotlib.pyplot as plt
import os
import sys
from os import listdir

def getKeckDataNames():
	return ["juldate", "vel", "uncert", "sval", "halpha", "mppx", "ex_time"];

def processKeckFile(name):	
	data = {};
	filename = "data/" + name + "_KECK.vels";
	raw_data = [];
	data_names = getKeckDataNames();
	data['juldate'] = []; #Julian Dates
	data['vel'] = []; #Velocities
	data['uncert'] = []; #Uncertainty of velocities
	data['sval'] = []; #S Values - See README.md
	data['halpha'] = []; #H Alpha values
	data['mppx'] = []; #Median photons per pixel
	data['ex_time'] = []; #Exposure time

	with open(filename) as f:
		raw_data = f.readlines();
	for i in range(0, len(raw_data)):
		raw_data[i] = raw_data[i].strip();
		split_data = raw_data[i].split();
		if not len(split_data) == len(data_names):
			print "We have a problem!";
			sys.exit("Oh no!");
		for i in range(0, len(data_names)):
			data[data_names[i]].append(split_data[i]);	
	return data;

def startProcessing():
	file_list = os.listdir("data/");
	keck_velfiles = {}; #Dictionary for all the velocities
	keck_names = [];
	for tmp_file in file_list:
		if not tmp_file == "planets.csv":
			tmp_file = tmp_file[:-10]; #Remove _KECK.vels from name
			keck_velfiles[tmp_file] = processKeckFile(tmp_file);
			keck_names.append(tmp_file);
	print keck_velfiles['HTR161-009'];		

	fig = plt.figure()
	plt.title("Velocity vs Observation Number for 10 bodies");
	plt.xlabel("Observation number");

	plt.ylabel("Velocity of Celestial Body");	
	for name in keck_names[50:60]:
		vels = keck_velfiles[name]['vel'][:20];
		plt.plot(vels, 'k');
	plt.show();
	fig.savefig("media/fig1.png");


startProcessing();

