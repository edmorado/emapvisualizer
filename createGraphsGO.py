#!/usr/bin/python

import argparse
import sys
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.patches as mpatches

if len(sys.argv) != 2:                                      
        print("Usage: python creatGraphsGO.py GO.csv")
        print("Example: python creatGraphsGO.py bp_output.csv")
else:
	infilename = sys.argv[1]
	infile = [((line.rstrip()).split("\t")) for line in open(infilename,"r").readlines()]

	thisLevel = []
	for line in infile:
		level = line[0]
		name = line[2]
		parent = line[3]
		numgenes = len(line[5].split(","))
		if level == "5":
			thisLevel.append([numgenes,name,parent])
	thisLevel = sorted(thisLevel, reverse=True)

	top20 = thisLevel[0:20]
	top60 = thisLevel[0:60]

	print("Top20 is:\n")
	print(top20)

	counts = []
	annots = []

########################## Top 20 Arranged
	"""
	for elem in top20:
		count = elem[0]
		annot = elem[1]
		counts.append(count)
		annots.append(annot)

	annots = set(annots)

	y_pos = np.arange(len(annots))
	"""

	cmap = plt.get_cmap("RdYlGn")
	colors = cmap(np.arange(20)*12)

########################### Bar Single
	"""	
	plt.bar(y_pos, counts, align='center', alpha=0.5, color=colors)
	plt.xticks(y_pos, annots, rotation=45, ha="right", va="top")
	plt.ylabel('Gene Count')
#	plt.title('Biological Process')
#	plt.title('Cellular Component')
#	plt.title('Molecular Function')
	plt.subplots_adjust(bottom=0.35) 
	plt.show()
	"""
############################ Pie
	"""
	plt.pie(counts, labels=annots, autopct='%1.1f%%', colors=colors, pctdistance=1.1, labeldistance=1.2)
	plt.axis('equal')
#	plt.title("Biological Process\n(proportion based only on top 20 annotations)", loc="left")
#	plt.title("Cellular Component\n(proportion based only on top 20 annotations)", loc="left")
#	plt.title("Molecular Function\n(proportion based only on top 20 annotations)", loc="right")
	plt.show()
	"""
	
############################# Bar 60 All

	"""
 	for elem in top60:
 		count = elem[0]
 		annot = elem[1]
 		counts.append(count)
 		annots.append(annot)
 
	annots = set(annots)

	colors2 = []
	for line in top60:
		if line[2] == "biological_process":
			colors2.append("yellowgreen")
			print("BP")
		elif line[2] == "cellular_component":
			colors2.append("lightcoral")
			print("CC")
		elif line[2] == "molecular_function":
			colors2.append("lightskyblue")
			print("MF")
		else:
			print(line)		
	"""
############################# Bar 60 Even
	colors3 = []
	colorforEven = ["yellowgreen", "lightcoral", "lightskyblue"]	

	for colore in colorforEven:
		i = 0
		while i < 20:
			colors3.append(colore)
			i += 1

	bpa = []
	cca = []
	mfa = []
		
	for element in thisLevel:
		if element[2] == 'biological_process':
			bpa.append(element)

	for element in thisLevel:
		if element[2] == 'cellular_component':
			cca.append(element)

	for element in thisLevel:
		if element[2] == 'molecular_function':
			mfa.append(element)

	bpa = sorted(bpa, reverse=True)
	cca = sorted(cca, reverse=True)
	mfa = sorted(mfa, reverse=True)

############################# Plot it
	allannot = bpa[:20] + cca[:20] + mfa[:20]

	print(bpa[:20])
	
	for elem in allannot:
		count = elem[0]
		annot = elem[1]
		counts.append(count)
		annots.append(annot)

	y_pos = np.arange(len(annots))
	
	plt.bar(y_pos, counts, align='center', alpha=0.5, color=colors3)	
	plt.xticks(y_pos, annots, rotation=45, ha="right", va="top", fontsize=8)
	plt.ylabel('Gene Count')
	plt.title('All Annotations')
	plt.subplots_adjust(bottom=0.35)

	bp = mpatches.Patch(color='yellowgreen', label='biological_process')
	cc = mpatches.Patch(color='lightcoral', label='cellular_component')
	mf = mpatches.Patch(color='lightskyblue', label='molecular_function')
	plt.legend(handles=[bp, cc, mf])
#	plt.show()
