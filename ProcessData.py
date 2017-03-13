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
		for j in range(0, len(data_names)):
			data[data_names[j]].append(split_data[j]);	
	return data;

def makeGraph(keck_names, keck_velfiles):
	fig = plt.figure()
	plt.title("Velocity vs Observation Number");
	plt.xlabel("Observation number");

	plt.ylabel("Velocity of Celestial Body");	
	for name in keck_names:
		vels = keck_velfiles[name]['vel'][:20];
		plt.plot(vels, 'o');
	plt.show();
	fig.savefig("media/fig1.png");
def getPlanetDataNames():
	return ["rowid","pl_hostname","pl_letter","pl_discmethod","pl_pnum","pl_orbper","pl_orbpererr1","pl_orbpererr2","pl_orbperlim","pl_orbsmax","pl_orbsmaxerr1","pl_orbsmaxerr2","pl_orbsmaxlim","pl_orbeccen","pl_orbeccenerr1","pl_orbeccenerr2","pl_orbeccenlim","pl_orbincl","pl_orbinclerr1","pl_orbinclerr2","pl_orbincllim","pl_bmassj","pl_bmassjerr1","pl_bmassjerr2","pl_bmassjlim","pl_bmassprov","pl_radj","pl_radjerr1","pl_radjerr2","pl_radjlim","pl_dens","pl_denserr1","pl_denserr2","pl_denslim","pl_ttvflag","pl_kepflag","pl_k2flag","pl_nnotes","ra_str","ra","dec_str","dec","st_dist","st_disterr1","st_disterr2","st_distlim","st_optmag","st_optmagerr","st_optmaglim","st_optmagblend","st_optband","gaia_gmag","gaia_gmagerr","gaia_gmaglim","st_teff","st_tefferr1","st_tefferr2","st_tefflim","st_teffblend","st_mass","st_masserr1","st_masserr2","st_masslim","st_massblend","st_rad","st_raderr1","st_raderr2","st_radlim","st_radblend","rowupdate","pl_name","pl_tranflag","pl_rvflag","pl_imgflag","pl_astflag","pl_omflag","pl_cbflag","pl_orbtper","pl_orbtpererr1","pl_orbtpererr2","pl_orbtperlim","pl_orblper","pl_orblpererr1","pl_orblpererr2","pl_orblperlim","pl_rvamp","pl_rvamperr1","pl_rvamperr2","pl_rvamplim","pl_eqt","pl_eqterr1","pl_eqterr2","pl_eqtlim","pl_insol","pl_insolerr1","pl_insolerr2","pl_insollim","pl_massj","pl_massjerr1","pl_massjerr2","pl_massjlim","pl_msinij","pl_msinijerr1","pl_msinijerr2","pl_msinijlim","pl_masse","pl_masseerr1","pl_masseerr2","pl_masselim","pl_msinie","pl_msinieerr1","pl_msinieerr2","pl_msinielim","pl_bmasse","pl_bmasseerr1","pl_bmasseerr2","pl_bmasselim","pl_rade","pl_radeerr1","pl_radeerr2","pl_radelim","pl_rads","pl_radserr1","pl_radserr2","pl_radslim","pl_trandep","pl_trandeperr1","pl_trandeperr2","pl_trandeplim","pl_trandur","pl_trandurerr1","pl_trandurerr2","pl_trandurlim","pl_tranmid","pl_tranmiderr1","pl_tranmiderr2","pl_tranmidlim","pl_tsystemref","pl_imppar","pl_impparerr1","pl_impparerr2","pl_impparlim","pl_occdep","pl_occdeperr1","pl_occdeperr2","pl_occdeplim","pl_ratdor","pl_ratdorerr1","pl_ratdorerr2","pl_ratdorlim","pl_ratror","pl_ratrorerr1","pl_ratrorerr2","pl_ratrorlim","pl_def_reflink","pl_disc","pl_disc_reflink","pl_locale","pl_facility","pl_telescope","pl_instrument","pl_status","pl_mnum","pl_st_npar","pl_st_nref","pl_pelink","pl_edelink","pl_publ_date","hd_name","hip_name","st_rah","st_glon","st_glat","st_elon","st_elat","st_plx","st_plxerr1","st_plxerr2","st_plxlim","st_plxblend","gaia_plx","gaia_plxerr1","gaia_plxerr2","gaia_plxlim","gaia_dist","gaia_disterr1","gaia_disterr2","gaia_distlim","st_pmra","st_pmraerr","st_pmralim","st_pmdec","st_pmdecerr","st_pmdeclim","st_pm","st_pmerr","st_pmlim","st_pmblend","gaia_pmra","gaia_pmraerr","gaia_pmralim","gaia_pmdec","gaia_pmdecerr","gaia_pmdeclim","gaia_pm","gaia_pmerr","gaia_pmlim","st_radv","st_radverr1","st_radverr2","st_radvlim","st_radvblend","st_sp","st_spstr","st_sperr","st_splim","st_spblend","st_logg","st_loggerr1","st_loggerr2","st_logglim","st_loggblend","st_lum","st_lumerr1","st_lumerr2","st_lumlim","st_lumblend","st_dens","st_denserr1","st_denserr2","st_denslim","st_metfe","st_metfeerr1","st_metfeerr2","st_metfelim","st_metfeblend","st_metratio","st_age","st_ageerr1","st_ageerr2","st_agelim","st_vsini","st_vsinierr1","st_vsinierr2","st_vsinilim","st_vsiniblend","st_acts","st_actserr","st_actslim","st_actsblend","st_actr","st_actrerr","st_actrlim","st_actrblend","st_actlx","st_actlxerr","st_actlxlim","st_actlxblend","swasp_id","st_nts","st_nplc","st_nglc","st_nrvc","st_naxa","st_nimg","st_nspec","st_uj","st_ujerr","st_ujlim","st_ujblend","st_vj","st_vjerr","st_vjlim","st_vjblend","st_bj","st_bjerr","st_bjlim","st_bjblend","st_rc","st_rcerr","st_rclim","st_rcblend","st_ic","st_icerr","st_iclim","st_icblend","st_j","st_jerr","st_jlim","st_jblend","st_h","st_herr","st_hlim","st_hblend","st_k","st_kerr","st_klim","st_kblend","st_wise1","st_wise1err","st_wise1lim","st_wise1blend","st_wise2","st_wise2err","st_wise2lim","st_wise2blend","st_wise3","st_wise3err","st_wise3lim","st_wise3blend","st_wise4","st_wise4err","st_wise4lim","st_wise4blend","st_irac1","st_irac1err","st_irac1lim","st_irac1blend","st_irac2","st_irac2err","st_irac2lim","st_irac2blend","st_irac3","st_irac3err","st_irac3lim","st_irac3blend","st_irac4","st_irac4err","st_irac4lim","st_irac4blend","st_mips1","st_mips1err","st_mips1lim","st_mips1blend","st_mips2","st_mips2err","st_mips2lim","st_mips2blend","st_mips3","st_mips3err","st_mips3lim","st_mips3blend","st_iras1","st_iras1err","st_iras1lim","st_iras1blend","st_iras2","st_iras2err","st_iras2lim","st_iras2blend","st_iras3","st_iras3err","st_iras3lim","st_iras3blend","st_iras4","st_iras4err","st_iras4lim","st_iras4blend","st_photn","st_umbj","st_umbjerr","st_umbjlim","st_umbjblend","st_bmvj","st_bmvjerr","st_bmvjlim","st_bmvjblend","st_vjmi"];


def findnth(haystack, needle, n):
    parts= haystack.split(needle, n+1)
    if len(parts)<=n+1:
        return -1
    return len(haystack)-len(parts[-1])-len(needle)


def processPlanetsFile():
	data = {};
	filename = "data/planets.csv";
	raw_data = [];
	data_names = getPlanetDataNames();
	for name in data_names:
		data[name] = [];
	with open(filename) as f:
		raw_data = f.readlines();
	for i in range(0, len(raw_data)):
		if raw_data[i].startswith("#"):
			continue;
		raw_data[i] = raw_data[i].strip();
		lastIndex = 0;
		for j in range(0, len(data_names)):
			currIndex = findnth(raw_data[i], ",", j);
			if currIndex == -1:
				print raw_data[i];
				print "StartsWith: {}".format(raw_data[i].startswith("#"));
				print "oops";
				asdfs
			if currIndex - lastIndex == 1:
				data[data_names[j]] = "NONE";
			else:
				if j == 0:
					data[data_names[j]] = raw_data[i][lastIndex:currIndex];
				else:
					data[data_names[j]] = raw_data[i][lastIndex+1:currIndex];
			lastIndex = currIndex;
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
	planet_data = processPlanetsFile();	
	print planet_data['rowid'];
	print planet_data['pl_hostname'];
#3458 xi Aql b Radial Velocity
startProcessing();

