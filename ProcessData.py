#ProcessData.py
#Name:Fatima Davila
#Date:4/6/2025
#Assignment:process data

import random

def main():
  def ClassYear(major, year):
    majorabr = major[0:3]
    yearabr = ""
    if year == "Freshman":
      yearabr = "FR"
    elif year == "Sophomore":
      yearabr = "SO"
    elif year == "Junior":
      yearabr = "JR"
    elif year == "Senior":
      yearabr = "SR"

    majoryear = majorabr + "-" + yearabr
    return majoryear
  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  #line = inFile.readline()
  for line in inFile:
    data = line.split()
    first = data[0]
    last = data[1]
    idNum = data[3]
    student_id = makeID(first, last, idNum)
    major = data[6]
    year = data[5]
    majoryear = ClassYear(major, year)
    output = last + "," + first + "," + student_id + "," + majoryear + "\n"
    outFile.write(output)

  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

def makeID(first, last, idNum):
  def ClassYear(major, year):
    majorabr = major[0:3]
    yearabr = ""
    if year == "Freshman":
      yearabr = "FR"
    elif year == "Sophomore":
      yearabr = "SO"
    elif year == "Junior":
      yearabr = "JR"
    elif year == "Senior":
      yearabr = "SR"

    majoryear = majorabr + "-" + yearabr
    return majoryear

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  for line in inFile:
    data = line.split()
    first = data[0]
    last = data[1]
    idNum = data[3]
    student_id = makeID(first, last, idNum)
    major = data[6]
    year = data[5]
    majoryear = ClassYear(major, year)
    output = last + "," + first + "," + student_id + "," + majoryear + "\n"
    outFile.write(output)



  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()
def makeID(first, last, idNum):
  #print(first, last, idNum)
  idLen = len(idNum)

  if len(last) < 5:
    last = last + "X"

  id = first[0] + last + idNum[idLen - 3: ]

  return id

if __name__ == '__main__':
  main()
