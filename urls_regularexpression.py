"""to perform the searching of the regular expression in the web document"""
import urllib2
import re
f = urllib2.urlopen('http://www.facebook.com').read()

#for a in f:
#prog = re.compile("<a")
lst = re.findall(r"(https?:(//)+[\w\d:#@%/;$()~_?\+-=\\\.&]*)",f)#regular expression
lst1 = lst
set1 = set(lst)#to remove the same urls
lst = list(set1)
lenth = len(lst)
for i in range(lenth):
	print " ".join(lst[i]) 
print len(lst)
	