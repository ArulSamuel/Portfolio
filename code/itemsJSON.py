import json
import csv

global jsonDict
jsonDict = {}

def readCSVFile(csvFile,dictKey):

	## Read the data from the csv file - using DictReader
	with open(csvFile,"rb") as csvf:
		items = csv.DictReader(csvf)
		
		itemList = []
		## Add the Items to the list
		for item in items:
			itemList.append(item)
	
	jsonDict[dictKey] = itemList
	
def writeToJSON(jsonFile):

	## Writing the dictionary as a JSON file
	with open(jsonFile, "w") as jsonf:
		jsonf.write(json.dumps(jsonDict,indent = 4))

def main():
	csvProjectFile = "../data/projects.csv"
	csvCourseFile = "../data/courses.csv"
	jsonFile = "../templates/portfolio/data/items.json"

	dictKey = "Projects"
	readCSVFile(csvProjectFile,dictKey)

	dictKey = "Courses"
	readCSVFile(csvCourseFile,dictKey)
	writeToJSON(jsonFile)

if __name__ == "__main__":
	main()
