import os
import re
fp=open('data/code.txt','r')
k=re.findall(r'([\d]+[.] [a-zA-z0-9\n +\-.,!@#$%^&*();\\/|<>":?=\']*?)[*]',fp.read())
x=[]
for i in k:
	#if not re.search(r'(a[.])',i):
	z=re.findall(r'(\d+)[.] ([a-zA-z0-9\n +\-.,!@#$%^&*();\\/|<>":?=\']*?)a[.] (\w+)\nb[.] (\w+)\nc[.] (\w+)\nd[.] (\w+)\ne[.] (\w+)',i)
	#for j in z:
	for w in z[0][2:]:
		print w
