from bs4 import BeautifulSoup
import re
import urllib.request
import sys
import csv
START = 7626
# START = 7360
START = 32060
END = 49933

START = 49932
END = 55000

START = 7358
END = 7360

UNIT_START = 2
UNIT_END = 7356

ADDRESS_SIZE_START = 0
ADDRESS_SIZE_END = 6

def my_print(text):
    sys.stdout.write(str(str(text)) + "\n")
    sys.stdout.flush()

# def isBlank(url):
# 	response = urllib.request.urlopen(url)
# 	input = str(response.read().decode('UTF-8', 'ignore'))
# 	result = re.search(r'.*Phone:&nbsp;\s*(.*)$', input, re.DOTALL)
# 	if result is not None: 
# 		return False
# 	else: 
# 		return True

# def findStart(START, END):
# 	MIDDLE = int((START - END/2))
# 	url = "http://www.infogo.gov.on.ca/infogo/employee.do?actionType=browse&id=" + START + "&infoType=telephone&locale=en"
# 	if not (isBlank(START)):
# 		print ("FOUND START: " + START)
# 		return START
# 	if not (isBlank(MIDDLE)): 
# 		findStart(START, MIDDLE)
# 	findStart(int(MIDDLE + 1), END)	

#check first result 
	# if isBlank()
	# findLimits(START, MIDDLE)
	# findLimits(MIDDLE, END)

#defaults
name = ""
phone = ""
fax = ""
email = "" 
website = ""
attributes = ""
address = ""
title = ""
ministry = ""
branch = ""

row = ["Name", "Phone", "Fax", "Email", "URL", "Title", "Ministry", "Branch", "Address", "URL", "No."]
with open('output.csv', 'a', newline='') as fp:
	a = csv.writer(fp, delimiter=',')
	a.writerow(row)


for i in range(START, END): 
	# my_print(str(i - START) + "\n")
	title = ministry = branch = name = phone = fax = email = url = website  =  address = attributes = "-"
	url = "http://www.infogo.gov.on.ca/infogo/employee.do?actionType=browse&id=" + str(i) + "&infoType=telephone&locale=en"
	response = urllib.request.urlopen(url)
	input = str(response.read().decode('UTF-8', 'ignore'))
	#PHONE
	result = re.search(r'.*Phone:&nbsp;\s*(.*)$', input, re.DOTALL)
	if result is not None: 
		soup = BeautifulSoup(result.group(1), "html.parser")
		# print(soup.select(".bodycontext")[0])
		if(len(soup.select(".bodycontext")[0].contents) is not 0): 
			phone = (soup.select(".bodycontext")[0]).contents[0].encode('utf-8', 'ignore').decode('ascii', 'ignore')
#NAME
		soup = BeautifulSoup(input, "html.parser")
		name = (soup.select("b")[0]).contents[0].encode('utf-8', 'ignore').decode('ascii', 'ignore')
		# my_print("NAME: " + name)
		# my_print("PHONE: " + phone)

		# result = re.search(r'.*Address:&nbsp;\s*(.*)$', input, re.DOTALL)
		# if result is not None: 
		# 	soup = BeautifulSoup(result.group(1), "html.parser")
		# 	name = (soup.select(".bodycontext")[0]).contents[0].encode('utf-8', 'ignore').decode('ascii', 'ignore')
		# 	my_print("Name: " + name)
#FAX
		result = re.search(r'.*Fax:&nbsp;\s*(.*)$', input, re.DOTALL)
		if result is not None: 
			soup = BeautifulSoup(result.group(1), "html.parser")
			fax = (soup.select(".bodycontext")[0]).contents[0].encode('utf-8', 'ignore').decode('ascii', 'ignore')
			# my_print("FAX: " + fax)
		result = re.search(r'.*Email:&nbsp;\s*(.*)$', input, re.DOTALL)
		
		if result is not None: 
			soup = BeautifulSoup(result.group(1), "html.parser")
			email = (soup.select(".bodycontext")[0]).contents[0].encode('utf-8', 'ignore').decode('ascii', 'ignore')
			# my_print("EMAIL: " + email)
		result = re.search(r'.*URL:&nbsp;\s*(.*)$', input, re.DOTALL)
		
		if result is not None: 
			soup = BeautifulSoup(result.group(1), "html.parser")
			website = (soup.select(".bodycontext")[0]).contents[0].encode('utf-8', 'ignore').decode('ascii', 'ignore')
			# my_print("Website: " + website)

		result = re.search(r'.*Address:&nbsp;\s*(.*)$', input, re.DOTALL)
		if result is not None: 
			soup = BeautifulSoup(result.group(1), "html.parser")
			attributes = (soup.select(".bodycontext")[1]).contents[0].encode('utf-8', 'ignore').decode('ascii', 'ignore')
			# my_print("attributes: " + attributes)

			attributes_array = attributes.split(' - ', 2)
			if len(attributes_array) > 0: 
				title = attributes_array[0]
			if len(attributes_array) > 1: 
				ministry = attributes_array[1]
			if len(attributes_array) > 2: 
				branch = attributes_array[2]

			# my_print(title + "---" + ministry + "---" + branch)

			addressSelector = soup.select(".bodycontext")
			for addressSize in range(ADDRESS_SIZE_START, ADDRESS_SIZE_END):
				if len(addressSelector) >  addressSize + 2: 
					address  = address + ((addressSelector[addressSize + 2]).contents[0]).encode('utf-8', 'ignore').decode('ascii', 'ignore')+ "\n" 
			# my_print("Address: " + address)
			row = [name, phone, fax, email, website, title, ministry, branch, address[:-2], url, str(i)]
			with open('output.csv', 'a', newline='') as fp:
				a = csv.writer(fp, delimiter=',')
				a.writerow(row)


