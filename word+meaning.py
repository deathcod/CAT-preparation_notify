
import os
import requests
import re
import csv
fp=open('data/words.txt','r')
f=open("data/word+meaning.csv", "a")
writer = csv.writer(f)
for i in fp:
	k=[]
	k.append(i.rstrip())
	result=requests.get('https://www.vocabulary.com/dictionary/'+i.rstrip()).text
	x=result[result.find('<p class="short">')+len('<p class="short">'):result.find('</p>')]
	if len(x)>1000:
		x=result[result.find('description" content="')+len('description" content="'):result.find('"/>',result.find('description" content='))]
	if len(x)>1000:
		result=requests.get('http://www.dictionary.com/browse/'+i.rstrip()).text
		x=result[result.find('description" content="')+len('description" content="'):result.find('" />',result.find('description" content="'))]
	if len(x)>1000:
		x='[]'
	x=x.replace('<i>','')
	x=x.replace('</i>','')
	k.append(x.encode('utf-8','replace'))
	writer.writerow(k)