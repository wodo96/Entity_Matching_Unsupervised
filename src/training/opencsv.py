import argparse
import csv
parser = argparse.ArgumentParser()
parser.add_argument('-dataset', required=True)

opt = parser.parse_args()
dataset = opt.dataset

def readcsv(filename):
    with open(filename,newline= "\n", encoding="ISO-8859-1") as f:
        reader = csv.reader(f)
        return list(reader)

def makefiletxt(filecsv):
	templst=[]
	temp= ""
	for i in range(len(filecsv)):
		templst.insert(i,filecsv[i][1:])
	for t in templst:
		for n in t:
			temp += (str(n) + " ")
		temp += "\n"
	temp = temp.replace(" ,","")
	return temp

source_1 = makefiletxt(readcsv("../../data/%s/tableA.csv" % (dataset))[1:])
source_2 = makefiletxt(readcsv("../../data/%s/tableB.csv" % (dataset))[1:])

with open("../../data/%s/source_1.txt" % (dataset), "w+", encoding="utf-8") as f:
	f.write(source_1)
with open("../../data/%s/source_2.txt" % (dataset), "w+", encoding="utf-8") as f:
	f.write(source_2)