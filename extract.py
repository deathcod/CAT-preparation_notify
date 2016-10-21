import os
import re
import csv
fp=open('data/code.txt','r')
k=re.findall(r'([\d]+[.] [a-zA-z0-9\n +\-.,!@#$%^&*();\\/|<>":?=\']*?)[*]',fp.read())
x=[]
for i in k:
	#if not re.search(r'(a[.])',i):
	w=[]
	z=re.findall(r'(\d+)[.] ([a-zA-z0-9\n +\-.,!@#$%^&*();\\/|<>":?=\']*?)a[.] (\w+)\nb[.] (\w+)\nc[.] (\w+)\nd[.] (\w+)\ne[.] (\w+)',i)[0][:]
	for i in z:
		w.append(i)
	x.append(w)
print (x)
7with open("data/code.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(x)