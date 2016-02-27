#!/usr/bin/env python3
from pprint import pprint
import urllib.request
from bs4 import BeautifulSoup
import csv
import sys
import re

NAME_POSITION = None
PHONE_POSITION = {'x': 0, 'y': 0}
FAX_POSITION = {'x': 1, 'y': 0}
EMAIL_POSITION = {'x': 2, 'y': 0}
URL_POSITION = {'x': 0, 'y': 0}
ADDRESS_START_POSITION = {'x': 5, 'y': 0}

NAME_EXISTS = True
PHONE_EXISTS = True
FAX_EXISTS = True
EMAIL_EXISTS = True
URL_EXISTS = True
POSITION_EXISTS = True
ADDRESS_EXISTS = True

PRINT_FLAG = True

if len(sys.argv) > 1 and sys.argv[1] == '1':
	PRINT_FLAG = True
	print("Printing enabled")  


rows = []
row = ['Name', 'Phone', 'Fax',  'Email', 'Attributes', 'Address', 'Comments', 'URL']

with open('test.csv', 'a', newline='') as fp:
	a = csv.writer(fp, delimiter=',')
	a.writerow(row)
START = 7360
END = 49933
# END = 7361
rows.append(row)
# 7,360
# 49,933
# r = urllib.request.urlopen("http://www.infogo.gov.on.ca/infogo/employee.do?actionType=browse&id=7360&infoType=telephone&locale=en").read()
for i in range(START, END):
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

		bodyContextSelector = soup.select(".bodycontext")
#PHONE
		phone = ""

		if len(bodyContextSelector) > 0 and len(bodyContextSelector[0].contents) > 0 and  re.search('(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})',(bodyContextSelector[PHONE_POSITION['x']]).contents[PHONE_POSITION['y']].encode('utf-8', 'ignore').decode('ascii', 'ignore') , 0) is not None:
			phone = (bodyContextSelector[PHONE_POSITION['x']]).contents[PHONE_POSITION['y']].encode('utf-8', 'ignore').decode('ascii', 'ignore')
		else: 
			comments = comments + "No phone\t"
		fax = ""

		# print("FAX: " + (bodyContextSelector[1]).contents[0].encode('utf-8', 'ignore').decode('ascii', 'ignore'))
#FAX
		if len(bodyContextSelector) > 0 and len(bodyContextSelector[FAX_POSITION['x']].contents) > FAX_POSITION['y'] and  re.search('(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})',(bodyContextSelector[FAX_POSITION['x']]).contents[FAX_POSITION['y']].encode('utf-8', 'ignore').decode('ascii', 'ignore') , 0) is not None:
			fax = (bodyContextSelector[FAX_POSITION['x']]).contents[FAX_POSITION['y']].encode('utf-8', 'ignore').decode('ascii', 'ignore')
			print (fax)
		else:
			FAX_EXISTS = False
			comments = comments + "No fax\t"
			EMAIL_POSITION['x'] = FAX_POSITION['x'] + 1
			EMAIL_POSITION['y'] = FAX_POSITION['y']
			# ADDRESS_START_POSITION['y'] = ADDRESS_START_POSITION['y'] - 1
			print (fax)
		email = ""
#EMAIL		
		if len(bodyContextSelector) > 2 and len(bodyContextSelector[EMAIL_POSITION['x']].contents) > 0 and  re.search('[^@]+@[^@]+\.[^@]+',(bodyContextSelector[EMAIL_POSITION['x']]).contents[EMAIL_POSITION['y']].encode('utf-8', 'ignore').decode('ascii', 'ignore') , 0) is not None:
			email  = (bodyContextSelector[EMAIL_POSITION['x']]).contents[EMAIL_POSITION['y']].encode('utf-8', 'ignore').decode('ascii', 'ignore')
		elif FAX_EXISTS == True:
			EMAIL_POSITION['x'] = EMAIL_POSITION['x'] + 1
			email  = (bodyContextSelector[EMAIL_POSITION['x']]).contents[EMAIL_POSITION['y']].encode('utf-8', 'ignore').decode('ascii', 'ignore')
			ADDRESS_START_POSITION['y']  = ADDRESS_START_POSITION['y'] -1
		else : 
			comments = comments + ", No email"


		attributes = (soup.select(".bodycontext")[4]).contents[0].encode('utf-8', 'ignore').decode('ascii', 'ignore')
#ADDRESS
		address = ""
		address1Selector = soup.select(".bodycontext")
		if len(address1Selector) > ADDRESS_START_POSITION['x'] : 
			address  = address + ((address1Selector[ADDRESS_START_POSITION['x']]).contents[ADDRESS_START_POSITION['y']]).encode('utf-8', 'ignore').decode('ascii', 'ignore')
		
		address2Selector = soup.select(".bodycontext")
		if len(address2Selector) > ADDRESS_START_POSITION['x'] + 1: 
			address  = address + ", " + ((address2Selector[ADDRESS_START_POSITION['x'] + 1]).contents[0]).encode('utf-8', 'ignore').decode('ascii', 'ignore')
		# print(len(soup.select(".bodycontext")))
		address3Selector = soup.select(".bodycontext")
		if len(address3Selector) > ADDRESS_START_POSITION['x'] + 2 : 
			address = address  + ", " + ((address3Selector[ADDRESS_START_POSITION['x'] + 2]).contents[0]).encode('utf-8', 'ignore').decode('ascii', 'ignore')
		address4Selector = soup.select(".bodycontext")
		if len(address4Selector) > ADDRESS_START_POSITION['x'] + 3: 
			address = address + ", " + ((address4Selector[ADDRESS_START_POSITION['x'] + 3]).contents[0]).encode('utf-8', 'ignore').decode('ascii', 'ignore')

		# address_3 = ((soup.select(".bodycontext")[7]).contents[0]).encode('utf-8', 'ignore').decode('ascii', 'ignore')


		# address_4 = ((soup.select(".bodycontext")[8]).contents[0]).encode('utf-8', 'ignore').decode('ascii', 'ignore')


		# address = address_1 + ", " + address_2 + ", " + "address_3" + ", " + "address_4"
		row = [name, phone, fax, email, attributes, address, comments, url]
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

