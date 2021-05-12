import argparse
import json
import os

parser = argparse.ArgumentParser()
parser.add_argument('-dataset', required=True)
parser.add_argument('-block', type=int)
opt = parser.parse_args()

dataset = opt.dataset
blocks = opt.block



path = "../../data_block/%s/%d" % (dataset, blocks)
train = "ltable_id,rtable_id,label\n"

block_file_path = os.path.join(path, "all_precision.json")

precisions_all=[]
if os.path.exists(block_file_path):
	with open(block_file_path, "r+", encoding="utf-8") as f:
		precisions_all = json.loads(f.read())

experimental= ""
for precision in precisions_all:
	experimental=str(precision)
	experimental = experimental.replace("[","")
	experimental = experimental.replace("]","")
	experimental = experimental.replace(" ","")
	experimental = experimental.split(",")
	train += (experimental[0] + "," + experimental[1] + ",1\n")

print (train)

with open("../../data_block/%s/%d/train.txt" % (dataset, blocks), "w+", encoding="utf-8") as f:
	f.write(train)