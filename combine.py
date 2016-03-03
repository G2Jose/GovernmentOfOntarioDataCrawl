import csv

MAX_NUM_PARENTS = 0 
REQ_LIST_SIZE = 20
def findSize(list):
	listSize = 0
	for i in range(0, len(list)):
		if list[i] == "":
			listSize = i
			break
	return listSize

def writeLine(row):
	with open('testoutput.csv', 'a', newline='') as fp:
		a = csv.writer(fp, delimiter=',')
		a.writerow(row)

def getNumParents(row):
	listSize = 0
	for i in range(0, len(row)):
		if row[i] == "" or row[i] == " " or row[i] == None:
			listSize = i
			break
	return listSize - 2

def addPadding(row):
	for i in range(0, 12 - len(row)):
		row =  row + [""] 
	return row

def rightAlign(row, size):
	for i in range(0, size - len(row)):
		row = [" "] + row
	return row

dOrg = {'org': '', 'data': []};
dPeeps = {'org': '', 'data': [[]], 'parents': []}

with open('peopleinput.csv', 'r', newline='') as f:
	reader = csv.reader(f)
	for row in reader:
		if row[5] in dPeeps:
			# print(type(dPeeps[row[5]])) 
			newDict = dPeeps[row[5]]
			# print(newDict['rows'])
			newDict['rows'] = newDict['rows']  + [row]
			# print(newDict)
			dPeeps[row[5]] = newDict
			# dPeeps[row[5]] = (dPeeps[row[5]])['rows'] + row
			# dPeeps[row[5]] = dPeeps[row[5]] + [row]
		else:
			dPeeps[row[5]] = {'rows': [row]}
			# dPeeps[row[5]] = [row]

# for key in dPeeps: 
# 	print(dPeeps[key])

with open('organizations.csv', 'r', newline='') as f:
	reader = csv.reader(f)
	for row in reader:
		if len(row) > 1:
			dOrg[row[1]] = addPadding(row)
			# print (addPadding(row))	


found = 0 
notfound = 0 

for org in dPeeps:
# org = 'CENTRAL REGION'
# if 1 is 1: 
	if org in dOrg:
		# print("Found organization in dOrgs: " + str(dOrg[org]))
		found = found + 1 
		currentDictionary = dPeeps[org]

		if 'parents' in currentDictionary: 
			# print(len(dOrg[org]))
			if len(dOrg[org]) > 1:
				for k in range(1, 2 + getNumParents(dOrg[org])): 
					# print("Parent: " + str(k-1)+ " " + dOrg[org][k])
					currentDictionary['parents'] = currentDictionary['parents'].append(dOrg[org][k])
				# print(currentDictionary)
				# dPeeps[org] = currentDictionary
		else: 
			parentsArray = []
			if len(dOrg[org]) > 1:
				for l in range(1, 2 + getNumParents(dOrg[org])): 
					parentsArray = parentsArray + [dOrg[org][l]]
					if l > MAX_NUM_PARENTS:
						MAX_NUM_PARENTS = l 
						# print("Max = " + str(MAX_NUM_PARENTS))
					# print("Parent: " + str(l-1)+ " " + dOrg[org][l])
				currentDictionary['parents'] =  parentsArray
				# print(currentDictionary)

		# print(dPeeps[org])

	else:
		# print(org + " not found")
		notfound  = notfound + 1 
		print(org)

print("Found: " + str(found) + "\tNot found: " + str(notfound))

# print(dPeeps['CENTRAL REGION'])
for organization in dPeeps: 
	currentPeopleDict = dPeeps[organization]
	if organization.upper() in dOrg:
		# print("found organization: " + organization + " in dOrg")
		if 'rows' in currentPeopleDict:
			# print(currentPeopleDict)
			if 'parents' in currentPeopleDict:
				# print("found parents: " + currentPeopleDict['parents'])
				for i in range(0, len(currentPeopleDict['rows'])):
					# print(currentPeopleDict['rows'][i] + rightAlign(currentPeopleDict['parents'], MAX_NUM_PARENTS))
					# if organization == "PROPERTY SECTION" or organization == "ISSUES MANAGEMENT AND MEDIA RELATIONS":
						# print(rightAlign(currentPeopleDict['parents'], MAX_NUM_PARENTS))
					currentRow = currentPeopleDict['rows'][i] + rightAlign(currentPeopleDict['parents'], MAX_NUM_PARENTS)
					if len(currentRow) is not 17:
						print(len(currentRow))
					writeLine(currentRow)

	# else:
		# print("Can't find organization: " + organization + " in dOrg")



# print(getNumParents(dOrg['CENTRAL REGION']))

