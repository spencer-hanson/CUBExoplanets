import numpy as np
import os
from os import listdir

def processKeckFile(name):	
	data = {};
	filename = "data/" + name + "_KECK.vels";
	data['juldate'] = []; #Julian Dates
	data['vel'] = []; #Velocities
	data['uncert'] = []; #Uncertainty of velocities
	data['sval'] = []; #S Values - See README.md
	data['halpha'] = []; #H Alpha values
	data['mppx'] = []; #Median photons per pixel
	data['ex_time'] = []; #Exposure time
	
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



startProcessing();

