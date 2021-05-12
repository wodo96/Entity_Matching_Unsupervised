import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument('-dataset', required=True)
opt = parser.parse_args()
dataset = opt.dataset

def readcsv(filename):
    with open(filename, encoding="ISO-8859-1") as f:
        reader = csv.reader(f)
        return list(reader)

def functionSource(source):

    exp=""
    for s in source:
        s.remove(s[0])
        for i in range(len(s)):
            exp += (str(s[i]))+" "
            
        exp+="\n"
    return exp

source1=functionSource(readcsv("../../data/%s/tableA.csv" % dataset)[1:])
source2=functionSource(readcsv("../../data/%s/tableB.csv" % dataset)[1:])

with open("../../data/%s/source_1.txt" % (dataset), "w+", encoding="utf-8") as f:
    f.write(source1)

with open("../../data/%s/source_2.txt" % (dataset), "w+", encoding="utf-8") as f:
    f.write(source2)