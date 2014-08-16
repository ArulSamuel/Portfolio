import json
import csv

global jsonDict
jsonDict = {}

def readCSVFile(csvFile):

	## Read the data from the csv file - using DictReader
	with open(csvFile,"rb") as csvf:
		courses = csv.DictReader(csvf)
		
		courseList = []
		## Add the courses to the list
		for course in courses:
			courseList.append(course)
	
	jsonDict["Courses"] = courseList
	
def writeToJSON(jsonFile):

	print jsonDict
	with open(jsonFile, "w") as jsonf:
		jsonf.write(json.dumps(jsonDict,indent = 4))

def main():
	csvFile = "../data/courses.csv"
	jsonFile = "../data/courses.json"

	readCSVFile(csvFile)
	writeToJSON(jsonFile)

if __name__ == "__main__":
	main()
