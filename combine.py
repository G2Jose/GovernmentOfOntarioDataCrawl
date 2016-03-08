import csv

MAX_NUM_PARENTS = 0 
REQ_LIST_SIZE = 20

levels = [
	["PRESIDENT"], 
	["VICE PRESIDENT", "VP"], 
	["CHIEF FINANCIAL", "CHIEF EXECUTIVE", "CEO", "CFO", "CDO", "CIO"], 
	["DIRECTOR", "ADVISOR", "CHAIR"], 
	["MANAGER", "SUPERVISOR", "ADMINISTRATOR", "LEADER", "LEAD", "OFFICER", "COORDINATOR", "CO-ORDINATOR", "SPECIALIST"], 
	["ASSISTANT", "ANALYST"]
]

def getHighest(peopleArray, currentHighest):
	highest = []
	nextHighest = 0
	highestLevel = 0 
	# currentHighest = 0
	foundPeopleAtLevel = False
	for i in range(currentHighest, len(levels)):
		if foundPeopleAtLevel is not True:
			for j in range(0, len(levels[i])):
				for k in range(0, len(peopleArray)):
					if str(peopleArray[k][4]).upper().find(levels[i][j]) is not -1:
						highest = highest + peopleArray[k] + [str(highestLevel)]
						foundPeopleAtLevel = True
						nextHighest = i + 1
						highestLevel = highestLevel + 1
	if foundPeopleAtLevel is False:
		nextHighest = -1
	return highest, nextHighest

def addLevelDetails(org, dPeeps):
	i = 0 
	startLevel = -1
	while i  <= len(levels) and i is not -1:
		currentHighest, i = getHighest(dPeeps[org]["rows"], i)
		if i is not -1:
			startLevel = startLevel + 1
			dPeeps[org]["rows"][i] = dPeeps[org]["rows"][i] + [i]
		else: 
			startLevel = ""
		print(currentHighest)

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
		key = row[5].upper()
		if row[6] is not "-":
			key = key + " - " + row[6].upper()
			print("current key: " + key)
		if key in dPeeps:
			# print(type(dPeeps[row[5]])) 
			newDict = dPeeps[key]
			# print(newDict['rows'])
			newDict['rows'] = newDict['rows']  + [row]
			# print(newDict)
			dPeeps[key] = newDict
			# dPeeps[row[5]] = (dPeeps[row[5]])['rows'] + row
			# dPeeps[row[5]] = dPeeps[row[5]] + [row]
		else:
			#check if branch exists
			# key = row[5]
			# if row[6] is not "-":
				# key = key + " - " + row[6]
			dPeeps[key] = {'rows': [row]}
			print(dPeeps[key])
			# dPeeps[row[5]] = [row]

# for key in dPeeps: 
# 	print(dPeeps[key])

with open('organizations.csv', 'r', newline='') as f:
	reader = csv.reader(f)
	for row in reader:
		if len(row) > 1:
			org = row[1].upper()
			dOrg[org] = addPadding(row)
			# print (addPadding(row))	


found = 0 
notfound = 0 
writeLine(["Name", "Phone", "Fax", "Email", "Title", "Ministry", "Branch", "Address","Parent 9", "Parent 8", "Parent 7", "Parent 6", "Parent 5", "Parent 4", "Parent 3", "Parent 2", "Parent 1", "Parent 0"])
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
				for l in range(2, 2 + getNumParents(dOrg[org])): 
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
		if 'rows' in dPeeps[org]:
			for i in range(0, len(dPeeps[org]['rows'])):
				writeLine(dPeeps[org]['rows'][i])

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
					# if len(currentRow) is not 17:
					# 	print(len(currentRow))
					writeLine(currentRow)
print("done")
	# else:
		# print("Can't find organization: " + organization + " in dOrg")



# print(levels[1])

# i = 0 
# startLevel = -1
# while i  <= len(levels) and i is not -1:
# 	currentHighest, i = getHighest(dPeeps["DEBT MANAGEMENT"]["rows"], i)
# 	if i is not -1:
# 		startLevel = startLevel + 1
# 	else: 
# 		startLevel = ""
# 	print(currentHighest)

# addLevelDetails(org, dPeeps)

# print(getNumParents(dOrg['CENTRAL REGION']))

