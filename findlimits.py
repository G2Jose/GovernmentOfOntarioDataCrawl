from bs4 import BeautifulSoup
import re
import urllib.request
import sys
import csv

def my_print(text):
    sys.stdout.write(str(str(text)) + "\n")
    sys.stdout.flush()

def findStart(START, END):
	MIDDLE = int((END + START)/2)
	start_url = "http://www.infogo.gov.on.ca/infogo/employee.do?actionType=browse&id=" + str(START) + "&infoType=telephone&locale=en"
	if not (isBlank(start_url)):
		my_print ("Checking : " + str(START))
		my_print ("FOUND START: " + str(START))
		return START
	
	my_print ("Start_URL: " + str(START) +" Blank. Checking MIDDLE: " + str(MIDDLE))
	middle_url = "http://www.infogo.gov.on.ca/infogo/employee.do?actionType=browse&id=" + str(MIDDLE) + "&infoType=telephone&locale=en"
	if not (isBlank(middle_url)): 
		my_print("Middle URL: " + str(MIDDLE) + " is not blank")
		findStart(START, MIDDLE)
	else: 
		my_print("Middle URL: " + str(MIDDLE) + " is blank")

	my_print("CHECKING BETWEEN: " + str(MIDDLE) + ", " + str(END))
	findStart(int(MIDDLE + 1), END)	

def isBlank(url):
	my_print(type(url))
	response = urllib.request.urlopen(url)
	input = str(response.read().decode('UTF-8', 'ignore'))
	result = re.search(r'.*Phone:&nbsp;\s*(.*)$', input, re.DOTALL)
	if result is not None: 
		return False
	else:
		return True

findStart(0, 100000)