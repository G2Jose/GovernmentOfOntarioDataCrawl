import csv


REQ_LIST_SIZE = 20
def findSize(list):
	listSize = 0
	for i in range(0, len(list)):
		if list[i] == "":
			listSize = i
			break
	return listSize

def writeLine(row):
	with open('test.csv', 'a', newline='') as fp:
		a = csv.writer(fp, delimiter=',')
		a.writerow(row)

def getNumParents(row):
	listSize = 0
	for i in range(0, len(row)):
		if row[i] == "":
			listSize = i
			break
	return listSize - 2

def addPadding(row, REQ_LIST_SIZE):
	for i in range(0, REQ_LIST_SIZE- len(row)):
		row = [""] + row
	return row

dOrg = {'org': '', 'data': []};
dPeeps = {'org': '', 'data': [[]], 'parents': []}

with open('peopleinput.csv', 'r', newline='') as f:
	reader = csv.reader(f)
	for row in reader:
		if row[5].upper() in dPeeps:
			# print(type(dPeeps[row[5]])) 
			newDict = dPeeps[row[5].upper()]
			# print(newDict['rows'])
			newDict['rows'] = newDict['rows']  + [row]
			# print(newDict)
			dPeeps[row[5].upper()] = newDict
			# dPeeps[row[5]] = (dPeeps[row[5]])['rows'] + row
			# dPeeps[row[5]] = dPeeps[row[5]] + [row]
		else:
			dPeeps[row[5].upper()] = {'rows': [row]}
			# dPeeps[row[5]] = [row]

# for key in dPeeps: 
# 	print(dPeeps[key])

with open('organizations.csv', 'r', newline='') as f:
	reader = csv.reader(f)
	for row in reader:
		if len(row) > 1:
			dOrg[row[1].upper()] = row


found = 0 
notfound = 0 

for org in dPeeps:
# org = 'CENTRAL REGION'
# if 1 is 1: 
	# print("Found: " + str(found) + "\tNot found: " + str(notfound))

	if org.upper() in dOrg:
		
		# print("Found organization in dOrgs: " + str(dOrg[org]))
		if 'rows' in dPeeps[org.upper()]:
			found = found + len(dPeeps[org.upper()]['rows'])
		# found = found + 1 
		# print(org.upper())
		currentDictionary = dPeeps[org.upper()]

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
					if org.upper() == "THUNDER BAY":
						print(parentsArray)
					parentsArray = parentsArray + [dOrg[org][l].upper()]
					# print("Parent: " + str(l-1)+ " " + dOrg[org][l])
				currentDictionary['parents'] =  parentsArray
		dPeeps[org.upper()] = currentDictionary
				# print(currentDictionary)

		# print(dPeeps[org])

	else:
		# print(org + " not found")
		# print("Can't find: "  + org)
		if org.upper() in dPeeps:
			if 'rows' in dPeeps[org.upper()]:
				notfound = notfound + len(dPeeps[org.upper()]['rows'])
		# notfound  = notfound + 1 

print("Found: " + str(found) + "\tNot found: " + str(notfound))

for org in dPeeps:
	if 'rows' in dPeeps[org]:
		parentArray = []
		# if 'parents' in dPeeps[org]:
			# print(dPeeps[org])
			# parentArray = dPeeps[org]['parents']
			# print(parentArray)
		# print(dPeeps[org]['rows'])

			

# print(dOrg['CENTRAL REGION'])

# print(getNumParents(dOrg['CENTRAL REGION']))


