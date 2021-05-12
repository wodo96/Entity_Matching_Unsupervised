import argparse
import csv
import os

parser = argparse.ArgumentParser()
parser.add_argument('-dataset', required=True)

opt = parser.parse_args()

dataset = opt.dataset


path = "../../data/%s" % (dataset)

def readcsv(filename):
    with open(filename, encoding="ISO-8859-1") as f:
        reader = csv.reader(f)
        return list(reader)

source1 = readcsv("../../data/%s/tableA.csv" % dataset)[1:]
source2 = readcsv("../../data/%s/tableB.csv" % dataset)[1:]

def functionSource(source, num):

    exp=""
    txt=""
    experimental= ""
    for source in source1:
        source.remove(source[0])
        experimental =str(source)
        experimental = experimental.replace("[","")
        experimental = experimental.replace("]","")
        experimental = experimental.replace("'","")
        exp += experimental+"\n"

        print(experimental)
    if(num == 1):
        with open("../../data/%s/source_1.txt" % (dataset), "w+", encoding="utf-8") as f:
            f.write(exp)
    else:
        with open("../../data/%s/source_2.txt" % (dataset), "w+", encoding="utf-8") as f:
            f.write(exp)


functionSource(source1,1)
functionSource(source2,2)