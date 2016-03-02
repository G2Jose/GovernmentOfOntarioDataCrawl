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
	with open('output.csv', 'a', newline='') as fp:
		a = csv.writer(fp, delimiter=',')
		a.writerow(row)

def getNumParents(row):
	listSize = 0
	for i in range(0, len(row)):
		if row[i] == "":
			listSize = i
			break
	return listSize - 2

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

with open('input.csv', 'r', newline='') as f:
	reader = csv.reader(f)
	for row in reader:
		dOrg[row[1]] = row		


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
			print(len(dOrg[org]))
			if len(dOrg[org]) > 1:
				for k in range(1, 2 + getNumParents(dOrg[org])): 
					# print("Parent: " + str(k-1)+ " " + dOrg[org][k])
					currentDictionary['parents'] = currentDictionary['parents'].append(dOrg[org][k])
				print(currentDictionary)
				# dPeeps[org] = currentDictionary
		else: 
			parentsArray = []
			if len(dOrg[org]) > 1:
				for l in range(1, 2 + getNumParents(dOrg[org])): 
					parentsArray = parentsArray + [dOrg[org][l]]
					# print("Parent: " + str(l-1)+ " " + dOrg[org][l])
				currentDictionary['parents'] =  parentsArray
				# print(currentDictionary)

		# print(dPeeps[org])

	else:
		# print(org + " not found")
		notfound  = notfound + 1 

print("Found: " + str(found) + "\tNot found: " + str(notfound))

# print(dOrg['CENTRAL REGION'])

# print(getNumParents(dOrg['CENTRAL REGION']))


