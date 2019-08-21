#!/usr/bin/env python

import argparse
from argparse import RawTextHelpFormatter
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.patches as mpatches
import numpy as np

"""
Author: El King Morado
Date: July 18, 2019
Purpose: Creates graphs for the output of Emap (tool created by previous interns)
"""

#ARGUMENT PARSER

parser = argparse.ArgumentParser(description="Creates a bar and/or pie graph for the top X percent of the output of Emap", formatter_class=RawTextHelpFormatter)

#Required Arguments
parser.add_argument("infilename", metavar="inputFile", help="Input, output of Emap (which has a file extension of csv but actually is a tsv)")

#Optional Arguments
parser.add_argument("-a", "--annot", metavar="N", type=int, default=7, help="Only output the corresponding annotations:\n1 == Biological process only\n2 == Cellular component only\n3 == Molecular function only\n4 == Biological process and cellular component\n5 == Biological process and molecular function\n6 == Cellular component and molecular function\n7 == All annotations (Default)")

parser.add_argument("-g", "--graph", metavar="N", type=int, default=3, help="Only output the corresponding graph:\n1 == Bar graphs\n2 == Pie graphs\n3 == Bar and Pie graphs (Default)")

parser.add_argument("-t", "--top", metavar="NN", type=int, default=20, help="Top NN of the annotations will be displayed per domain (Default is 20)")

#parser.add_argument("-o", "--outdir", metavar="dir", default="emapvis", help="Output directory for the graphs")

parser.add_argument("-c", "--cmap", metavar="code", default="RdYlGn", help="Color map code for matplotlib for the prettyness of the graphs\nI suggest the following:\nRdYlBu\nSpectral\nviridis\nplasma\nRdYlGn (Default)")

parser.add_argument("-l", "--level", metavar="N", default=5, type=int, help="Gene onthology level")

parser.add_argument("-b", "--barall", metavar="N", default=0, type=int, help="Creates the bar  ")

args = vars(parser.parse_args())

#GET VALUE OF ARGUMENTS

infilename = args["infilename"]
graph = args["graph"]
top = args["top"]
annotChoice = args["annot"]
colsch = args["cmap"]
#outdir = args["outdir"]
level = args["level"]
barall = args["barall"]

#Checking for arguments
"""
print("Input file name: {0}.".format(infilename))
print("Graph outputs: {0}.".format(graph))
print("For top {0} annotations.".format(top))
print("Annotation outputs: {0}.".format(annot))
print("Cmap to use: {0}.".format(colsch))
print("Output directory: {0}.".format(outdir))
"""

#FUNCTIONS

def createBar(domain,annotData,numElem,cols):
	#ADD INFO FOR GRAPH ELEMENTS
	if domain == 1:
		title = "Biological Process"
	elif domain == 2:
		title = "Cellular Component"
	else:
		title = "Molecular Function"

	outfilename = title.replace(" ","_") + "_Bar.png"
	cmap = plt.get_cmap(cols)
	colors = cmap(np.arange(numElem)*12)

	#POPULATE DATA
	counts = []
	annots = []

	annotData = annotData[:numElem]
	print("=======")
	print(annotData)

	lenlimit = 65

	for elem in annotData:
		count = elem[0]
		annot = elem[1]
		counts.append(count)
		if len(annot) < lenlimit:
			annots.append(annot)
		else:
			newannot = annot[:lenlimit] + "\n-" + annot[lenlimit:]
			annots.append(newannot)

	y_pos = np.arange(len(annots))

	#GENERATE GRAPH AND GRAPH ELEMENTS

	fig = plt.figure(figsize=(20, 10))
	plt.bar(y_pos, counts, align="center", alpha=0.5, color=colors, edgecolor="black")
	plt.xticks(y_pos, annots, rotation=45, ha="right", va="top")
	plt.subplots_adjust(left=None, bottom=.35, right=None, top=None, wspace=None, hspace=None)
	plt.ylabel("Gene Count")
	plt.title(title)
	plt.savefig(outfilename, dpi=100)

def createPie(domain,annotData,numElem,cols):
	#ADD INFO FOR GRAPH ELEMENTS
	if domain == 1:
		title = "Biological Process"
	elif domain == 2:
		title = "Cellular Component"
	else:
		title = "Molecular Function"

	graphTitle = title + "\n(proportion based only on top 20 annotations)"
	outfilename = title.replace(" ","_") + "_Pie.png"
	cmap = plt.get_cmap(cols)
	colors = cmap(np.arange(numElem)*12)

	#POPULATE DATA
	counts = []
	annots = []

	annotData = annotData[:numElem]

	for elem in annotData:
		count = elem[0]
		annot = elem[1]
		counts.append(count)
		annots.append(annot)

	y_pos = np.arange(len(annots))

	#GENERATE GRAPH AND GRAPH ELEMENTS
	fig = plt.figure(figsize=(20, 12))

	plt.pie(counts, labels=annots, autopct='%1.1f%%', colors=colors, pctdistance=1.1, labeldistance=1.2)
	plt.axis("equal")
	plt.title(graphTitle, loc="left")
	plt.savefig(outfilename, dpi=100)

def createBarall(bps,ccs,mfs,numElem,cols):
	#ADD INFO FOR GRAPH ELEMENTS
	outfilename = "BarAll.png"
	title = "Top 20 Annotations for Each Domain"
	cmap = plt.get_cmap(cols)
	color1 = cmap(.1)
	color2 = cmap(.4)
	color3 = cmap(.9)
	colorGet = [color1, color2, color3]
	colors =[]
	bp = mpatches.Patch(color=color1, label='biological_process')
	cc = mpatches.Patch(color=color2, label='cellular_component')
	mf = mpatches.Patch(color=color3, label='molecular_function')

	for color in colorGet:
		i = 0
		while i < 20:
			colors.append(color)
			i += 1

	#POPULATE DATA
	counts = []
	annots = []

	bps = bps[:numElem]
	ccs = ccs[:numElem]
	mfs = mfs[:numElem]

	annotData = bps + ccs + mfs

	for elem in annotData:
		count = elem[0]
		annot = elem[1]
		counts.append(count)
		annots.append(annot)

	y_pos = np.arange(len(annots))

	#GENERATE GRAPH AND GRAPH ELEMENTS
	fig = plt.figure(figsize=(20, 10))
	plt.bar(y_pos, counts, align="center", alpha=0.5, color=colors, edgecolor="black")
	plt.xticks(y_pos, annots, rotation=45, ha="right", va="top")
	plt.subplots_adjust(left=None, bottom=.35, right=None, top=None, wspace=None, hspace=None    )
	plt.ylabel("Gene Count")
	plt.title(title)
	plt.legend(handles=[bp, cc, mf])
	plt.savefig(outfilename, dpi=100)

#GET ALL SIGNIFICANT DATA

infile = [((line.rstrip()).split("\t")) for line in open(infilename,"r").readlines()]

bps = []
ccs = []
mfs = []

for line in infile:
	level_ffile = int(line[0])
	annotation = line[2]
	parent = line[3]
	numGenes = len(line[5].split(","))
	if level == level_ffile:
		if parent == "biological_process":
			bps.append([numGenes,annotation])
		if parent == "cellular_component":
			ccs.append([numGenes,annotation])
		if parent == "molecular_function":
			mfs.append([numGenes,annotation])

bps = sorted(bps, reverse=True)
ccs = sorted(ccs, reverse=True)
mfs = sorted(mfs, reverse=True)

#What to process
bpp = 0
ccp = 0
mfp = 0

#Check what domains to process
if annotChoice == 1:
	bpp = 1
elif annotChoice == 2:
	ccp = 1
elif annotChoice == 3:
	mfp = 1
elif annotChoice == 4:
	bpp = 1
	ccp = 1
elif annotChoice == 5:
	bpp = 1
	mfp = 1
elif annotChoice == 6:
	ccp = 1
	mfp = 1
elif annotChoice == 7:
	bpp = 1
	ccp = 1
	mfp = 1

#Check what graphs to create
if graph == 1:
	if bpp == 1:
		createBar(1,bps,top,colsch)
	if ccp == 1:
		createBar(2,ccs,top,colsch)
	if mfp == 1:
		createBar(3,mfs,top,colsch)
elif graph == 2:
	if bpp == 1:
		createPie(1,bps,top,colsch)
	if ccp == 1:
		createPie(2,ccs,top,colsch)
	if mfp == 1:
		createPie(3,mfs,top,colsch)
elif graph == 3:
	if bpp == 1:
		createBar(1,bps,top,colsch)
		createPie(1,bps,top,colsch)
	if ccp == 1:
		createBar(2,ccs,top,colsch)
		createPie(2,ccs,top,colsch)
	if mfp == 1:
		createBar(3,mfs,top,colsch)
		createPie(3,mfs,top,colsch)

#Check if to create barall
if barall == 1:
	createBarall(bps,ccs,mfs,top,colsch)
else:
	pass
