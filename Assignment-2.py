import urllib
import re
try:
	f=open("project2.txt","w")
	print "Enter the Site of which u want images as http://www.xyz.abc"
	z=raw_input()
	url=urllib.urlopen(z)
	html=url.read()
	b=re.compile("img.*src=\"([^ ]*)\"")
	x=re.findall(b,html)
	f.write("The following gives the links of all images in %s"%z)
	for i in x:
		if i.startswith("/"):
			print z+i
			f.write("\n")
			f.write(z+i)
		else:
			print z+i
			f.write("\n")
			f.write(z+i)
	f.close()
except:
	print "The website dosent exist/Please check the input"