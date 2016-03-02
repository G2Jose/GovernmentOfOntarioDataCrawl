from bs4 import BeautifulSoup
import re
import urllib.request
import sys
import csv


UNIT_START = 2
UNIT_START = 4777
UNIT_END = 7356
# UNIT_START = 1240
# UNIT_END = UNIT_START + 100

def my_print(text):
    sys.stdout.write(str(str(text)) + "\n")
    sys.stdout.flush()

def writeLine(row):
	with open('organizations.csv', 'a', newline='') as fp:
		a = csv.writer(fp, delimiter=',')
		a.writerow(row)

for i in range(UNIT_START, UNIT_END): 
	print("\n")

	url = "http://www.infogo.gov.on.ca/infogo/office.do?actionType=telephonedirectory&infoType=telephone&unitId=" + str(i) + "&locale=en"
	response = urllib.request.urlopen(url)
	result = str(response.read().decode('UTF-8', 'ignore'))


	if result is not None: 
		soup = BeautifulSoup(result, "html.parser")
		# print(soup.encode('utf-8', 'ignore').decode('ascii', 'ignore'))
		# print(soup.select(".bodycontext")[0])
		# print(len(soup.select("a")[0].contents))
		if(len(soup.select("ul")[0].contents) is not 0):
			row = []
			end_index = 0
			my_print(str(i))
			for noOfParents in range(0, len(soup.select(".content ul a")) - 1):
				item = (soup.select(".content ul a")[noOfParents].contents[0]).encode('utf-8', 'ignore').decode('ascii', 'ignore')
				if item == "OfficesDirectory": 
					break
				row.append(item)
				my_print(item)
			row.append(str(i))
			writeLine(list(reversed(row)))


