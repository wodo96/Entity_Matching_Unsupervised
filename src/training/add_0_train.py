import os
import csv
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-dataset', required= True)
parser.add_argument('-block', required= False, default=20)
opt = parser.parse_args()
dataset = opt.dataset
block = opt.block

data_path = "../../data/%s" %(dataset)
data_block_path = "../../data_block/%s/%s" %(dataset,block)

train_file_path = os.path.join(data_block_path, "train_with_only_one.csv")
tableA_path = os.path.join(data_path, "tableA.csv")
tableB_path = os.path.join(data_path, "tableB.csv")

def readcsv(filename):
    with open(filename,newline= "\n", encoding="ISO-8859-1") as f:
        reader = csv.reader(f)
        return list(reader)

def makefilecsv (train, tA, tB):
	ran_number =[]
	lenTa = len(tA)
	lenTb = len(tB)
	for i in range(int((len (train))/2)):
		ran_number.insert(i,[str(random.randrange(0,lenTa)),str(random.randrange(0,lenTb)),'0'])
	for j in range(len(ran_number)):
		
		if not(train.count([str(ran_number[j][0]),str(ran_number[j][1]),'1'])>0):
			train.append(ran_number[j])
	
	train_def = ""
	for touple in train:
		train_def += ((str(touple[0])) + "," + (str(touple[1])) + "," + (str(touple[2]))+ "\n")
	return train_def



new_train = makefilecsv (readcsv(train_file_path),readcsv(tableA_path),readcsv(tableB_path))

print ("done")
with open((data_block_path + "/train.csv" ),"w+", encoding="utf-8") as f:
    f.write(new_train)
