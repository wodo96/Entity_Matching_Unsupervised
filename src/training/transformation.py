import os
import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument('-dataset', required= True)
parser.add_argument('-block', required= False, default=20)
parser.add_argument('-label', required=False, default=0) #1: you have also zero as label in train.csv; 0:you only have '1' in label
opt = parser.parse_args()

dataset = opt.dataset
block =opt.block
label = opt.label

data_path = "../../data/%s" %(dataset)
data_block_path = "../../data_block/%s/%s" %(dataset,block)


train_file_path = os.path.join(data_block_path, "dirty_train.csv")
ltable_file_path = os.path.join(data_path, "tableA.csv")
rtable_file_path = os.path.join(data_path, "tableB.csv")



def readcsv(filename):
    with open(filename,newline= "\n", encoding="ISO-8859-1") as f:
        reader = csv.reader(f)
        return list(reader)

def csvToList(file):
    temp = []
    for i in range (len (file)-1):
        temp.insert(i,file[i+1][:1])
    return temp

def makefilecsv_nolabel (ltable,rtable,train):
    l=csvToList(ltable)
    r=csvToList(rtable)
    train_temp=[]
    for i in range (len(train)-1):
        train_temp.insert(i,(train[i+1][0] ,train[i+1][1]))
    train_def = "\"ltable_id\",\"rtable_id\",label\n"
    for touple in train_temp:
        train_def += (str(l[int(touple[0])]) + "," + str(r[int(touple[1])]) + ",1\n")
    train_def = train_def.replace("['","")
    train_def = train_def.replace("']","")
    return train_def

def makefilecsv_label (ltable,rtable,train):
    l=csvToList(ltable)
    r=csvToList(rtable)
    train_temp=[]
    for i in range (len(train)-1):
        if ((train[i+1][2])=='1'):
            train_temp.insert(i,(train[i+1][0],train[i+1][1]))
    train_def = "\"ltable_id\",\"rtable_id\",label\n"
    for touple in train_temp:
        train_def += (str(l[int(touple[0])]) + "," + str(r[int(touple[1])]) +",1\n")
    train_def = train_def.replace("['","")
    train_def = train_def.replace("']","")
    return train_def




if (label==0):
    train = makefilecsv_nolabel(readcsv(ltable_file_path),readcsv(rtable_file_path),readcsv(train_file_path))
else:
    train = makefilecsv_label(readcsv(ltable_file_path),readcsv(rtable_file_path),readcsv(train_file_path))


with open((data_block_path + "/%s_output-unsupervised.csv" % (dataset)),"w+", encoding="utf-8") as f:
    f.write(train)