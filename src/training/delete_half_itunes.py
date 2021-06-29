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
test_file_path = os.path.join(data_path, "test.csv")
valid_file_path = os.path.join(data_path, "valid.csv")
tableB_file_path = os.path.join(data_path, "tableB.csv")

def readcsv(filename):
    with open(filename,newline= "\n", encoding="ISO-8859-1") as f:
        reader = csv.reader(f)
        return list(reader)

def makefiletxt(file):
	new_file= "ltable_id,rtable_id,label\n"
	for touple in file:
		new_file += ((str(touple[0])) + "," + (str(touple[1])) + "," + (str(touple[2]))+ "\n")
	return new_file

def makefilecsv (train,test,valid,tableb):
	ltb= len(tableb)/2
	tableb= tableb[:int(ltb)]

	value = tableb[len(tableb)-1][0]
	
	for t in train:
		if t[1]>value:
			train.remove(t)
	
	for te in test:
		if te[1]>value:
			test.remove(te)
	
	for v in valid:
		if v[1]>value:
			valid.remove(v)
	
	train_def = makefiletxt(train)
	test_def = makefiletxt(test)
	valid_def = makefiletxt(valid)
	
	tableb_def = ""

	for tb in tableb:
		tableb_def += ((str(tb[0])) + ",\"" + (str(tb[1])) + "\",\"" + (str(tb[2])) + "\",\"" + (str(tb[3])) + "\",\"" + (str(tb[4])) + "\",\"" + (str(tb[5])) + "\",\"" + (str(tb[6])) + "\",\"" + (str(tb[7])) + "\",\"" + (str(tb[8])) + "\"\n")
	
	return tableb_def,train_def,test_def,valid_def

new_tableb,new_train,new_test,new_valid = makefilecsv(readcsv(train_file_path),readcsv(test_file_path),readcsv(valid_file_path),readcsv(tableB_file_path))

with open((data_path + "/train.csv" ),"w+", encoding="utf-8") as f:
    f.write(new_train)

with open((data_path + "/test.csv" ),"w+", encoding="utf-8") as f:
    f.write(new_test)

with open((data_path + "/valid.csv" ),"w+", encoding="utf-8") as f:
    f.write(new_valid)

with open((data_path + "/tableB.csv" ),"w+", encoding="utf-8") as f:
    f.write(new_tableb)