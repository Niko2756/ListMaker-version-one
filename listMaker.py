import sys

def main():
	specialCharacters = ["!","@",",",".","#","$","%","^","&","*",";",":","?","/"]

	dataSetOne = loadFile(specialCharacters)
	dataSetTwo = loadFile2(specialCharacters)

	finalArray = maker(dataSetOne,dataSetTwo)

	print(len(finalArray), "Possible permutations")
	print()
	saveList(finalArray)
	sys.exit()

def inputNameOfFile():
	while True:
		nameOfFile = input("Enter title of save file: ") or "Final list of permutations"
		if not nameOfFile.isalpha() and not nameOfFile.isprintable():
			print("Come on that's not what I asked for.\nPlease just give me a name in English please.\n")
			continue
		else:
			return nameOfFile.capitalize()

def saveList(finalArray):
	nameOfFile = inputNameOfFile()
	with open("""{}.txt""".format(nameOfFile),"w") as inFile:
		inFile.write("{} Possible permutations".format(len(finalArray)) + "\n\n\n")
		for item in finalArray:
			inFile.write(str(item) + "\n")
	inFile.close()
	print("Your list has been saved under: " """{}.txt""".format(nameOfFile))

def maker(dataSetOne,dataSetTwo):
	finalArray = []
	tempArray = []
	for num in range(len(dataSetOne)):
		for x in range(len(dataSetTwo)):
			if [dataSetOne[num], dataSetTwo[x]] == [dataSetOne[num], dataSetOne[num]]:
				pass
			else:
				tempArray.append([dataSetOne[num], dataSetTwo[x]])

	for count,item in enumerate(tempArray):
		if [tempArray[count][1], tempArray[count][0]] in tempArray[(count+1):]:
			pass
		#if [tempArray[count][1], tempArray[count][0]] in tempArray[:count]:
		else:
			finalArray.append(item)
	
	return finalArray
	

def loadFile(specialCharacters):
	array = []
	fullListWithDuplicates = []
	temp = ""

	with open("""listAey.txt""","r") as outFile:
		temp = outFile.read()
	outFile.close()
	for num in range(len(specialCharacters)):
		temp = temp.replace(specialCharacters[num],"")

	fullListWithDuplicates = temp.split()

	for stringThing in fullListWithDuplicates:
		if stringThing.lower() in array:
			pass
		else:
			array.append(stringThing.lower())

	return array

def loadFile2(specialCharacters):
	array = []
	fullListWithDuplicates = []
	temp = ""

	with open("""listBii.txt""","r") as outFile:
		temp = outFile.read()
	outFile.close()
	for num in range(len(specialCharacters)):
		temp = temp.replace(specialCharacters[num],"")

	fullListWithDuplicates = temp.split()

	for stringThing in fullListWithDuplicates:
		if stringThing.lower() in array:
			pass
		else:
			array.append(stringThing.lower())
			
	return array

main()
