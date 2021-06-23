import os
import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument('-dataset', required= True)
parser.add_argument('-block', required= False, default=20)
opt = parser.parse_args()
dataset = opt.dataset
block = opt.block


data_path = "../../data/%s" %(dataset)
data_block_path = "../../data_block/%s/%s" %(dataset,block)
train_file_path = os.path.join(data_path, "train.csv")
tableB_file_path = os.path.join(data_path, "tableB.csv")

def readcsv(filename):
    with open(filename,newline= "\n", encoding="ISO-8859-1") as f:
        reader = csv.reader(f)
        return list(reader)


def makefilecsv (train,tableb):
	ltb= len(tableb)/2
	tableb= tableb[:int(ltb)]

	value = tableb[len(tableb)-1][0]
	for t in train:
		if t[1]>value:
			train.remove(t)
	tableb_def = ""
	train_def = "\"ltable_id\",\"rtable_id\",label\n"
	for touple in train:
		train_def += ((str(touple[0])) + "," + (str(touple[1])) + "," + (str(touple[2]))+ "\n")
	for tb in tableb:
		tableb_def += ((str(tb[0])) + "," + (str(tb[1])) + "," + (str(tb[2])) + "," + (str(tb[3])) + "," + (str(tb[4])) + "," + (str(tb[5])) + "," + (str(tb[6])) + "," + (str(tb[7])) + "," + (str(tb[8])) + "\n")
	
	return tableb_def,train_def

new_tableb,new_train = makefilecsv(readcsv(train_file_path),readcsv(tableB_file_path))

with open((data_path + "/train.csv" ),"w+", encoding="utf-8") as f:
    f.write(new_train)

with open((data_path + "/tableB.csv" ),"w+", encoding="utf-8") as f:
    f.write(new_tableb)