#!/usr/bin/env python3
from pprint import pprint
import urllib.request
from bs4 import BeautifulSoup
import csv
import sys

PRINT_FLAG = False

if len(sys.argv) > 1 and sys.argv[1] == '1':
	PRINT_FLAG = True
	print("Printing enabled")  


rows = []
row = ['Name', 'Phone', 'Email', 'Attributes', 'Address', 'Comments', 'URL']

with open('test.csv', 'a', newline='') as fp:
	a = csv.writer(fp, delimiter=',')
	a.writerow(row)

rows.append(row)
# 7,360
# 49,933
# r = urllib.request.urlopen("http://www.infogo.gov.on.ca/infogo/employee.do?actionType=browse&id=7360&infoType=telephone&locale=en").read()
for i in range(7360, 49933):
	url = "http://www.infogo.gov.on.ca/infogo/employee.do?actionType=browse&id=" + str(i) + "&infoType=telephone&locale=en"
	#if PRINT_FLAG == 1:
	#	print(i) 
	# print(url)

	response = urllib.request.urlopen(url)
	soup = BeautifulSoup(response.read().decode('UTF-8', 'ignore').encode('ascii', 'ignore'), "html.parser")


	# print(type(r))
	# soup = BeautifulSoup(r, "html.parser")
	# print(type(soup))
	# print (soup.prettify()[0:1000])
	# print(soup.select("b"))
	if len(soup.select("b")) > 0 :
		# print("Type: " + str(type(soup.select("b"))) + " of size: " + str(len(soup.select("b"))))
		comments = ""

		name = (soup.select("b")[0]).contents[0].encode('utf-8', 'ignore').decode('ascii', 'ignore')

		phone = ""
		phoneSelector = soup.select(".bodycontext")
		if len(phoneSelector) > 0 and len(phoneSelector[0].contents) > 0:
			phone = (phoneSelector[0]).contents[0].encode('utf-8', 'ignore').decode('ascii', 'ignore')
		else: 
			comments = comments + "No phone"

		email = ""
		emailSelector = soup.select(".bodycontext")
		if len(emailSelector) > 2 and len(emailSelector[2].contents) > 0 :
			email  = (emailSelector[2]).contents[0].encode('utf-8', 'ignore').decode('ascii', 'ignore')
		else: 
			comments = comments + ", No email"

		attributes = (soup.select(".bodycontext")[4]).contents[0].encode('utf-8', 'ignore').decode('ascii', 'ignore')

		address = ""
		address1Selector = soup.select(".bodycontext")
		if len(address1Selector) > 5 : 
			address  = address + ((address1Selector[5]).contents[0]).encode('utf-8', 'ignore').decode('ascii', 'ignore')
		
		address2Selector = soup.select(".bodycontext")
		if len(address2Selector) > 6 : 
			address  = address + ", " + ((address2Selector[6]).contents[0]).encode('utf-8', 'ignore').decode('ascii', 'ignore')
		# print(len(soup.select(".bodycontext")))
		address3Selector = soup.select(".bodycontext")
		if len(address3Selector) > 7 : 
			address = address  + ", " + ((address3Selector[7]).contents[0]).encode('utf-8', 'ignore').decode('ascii', 'ignore')
		address4Selector = soup.select(".bodycontext")
		if len(address4Selector) > 8 : 
			address = address + ", " + ((address4Selector[8]).contents[0]).encode('utf-8', 'ignore').decode('ascii', 'ignore')

		# address_3 = ((soup.select(".bodycontext")[7]).contents[0]).encode('utf-8', 'ignore').decode('ascii', 'ignore')


		# address_4 = ((soup.select(".bodycontext")[8]).contents[0]).encode('utf-8', 'ignore').decode('ascii', 'ignore')


		# address = address_1 + ", " + address_2 + ", " + "address_3" + ", " + "address_4"
		row = [name, phone, email, attributes, address, comments, url]
		if PRINT_FLAG == 1: 
			print(row)
		# rows.append(row)
		with open('test.csv', 'a', newline='') as fp:
			a = csv.writer(fp, delimiter=',')
			a.writerow(row)

# print(rows)

# with open('test.csv', 'w', newline='') as fp:
#     a = csv.writer(fp, delimiter=',')
    
#     a.writerows(rows)

