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
train_file_path = os.path.join(data_block_path, "%s_output-unsupervised.csv" %(dataset))
test_file_path = os.path.join(data_path, "test.csv")

def readcsv(filename):
    with open(filename,newline= "\n", encoding="ISO-8859-1") as f:
        reader = csv.reader(f)
        return list(reader)

def makefilecsv (train, test):
	print("\nOld_touple:"+str(len(train)))
	print("Those touple will be eliminate:")
	for te in test:
		try:
			train.remove(te)
		except ValueError:
			exit
	print (">>>>><<<<<")
	print ("New_touple:"+str(len(train)))
	train_def = "\"ltable_id\",\"rtable_id\",label\n"
	for touple in train:
		train_def += ((str(touple[0])) + "," + (str(touple[1])) + "," + (str(touple[2]))+ "\n")
	return train_def

new_train = makefilecsv(readcsv(train_file_path), readcsv(test_file_path))

with open((data_block_path + "/train_with_only_one.csv" ),"w+", encoding="utf-8") as f:
    f.write(new_train)