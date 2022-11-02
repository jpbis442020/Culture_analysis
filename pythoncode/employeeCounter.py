# import parser object from tike
import re

from tika import parser

# opening pdf file
parsed_pdf = parser.from_file("Airsculpt Technologies, Inc. 2021 Annual Report 10-K.pdf")
  
# saving content of pdf
# you can also bring text only, by parsed_pdf['text'] 
# parsed_pdf['content'] returns string 
data = parsed_pdf['content'] 

# Data Sanitization
arr = data.split() # Split single string into array of words

for i in range(len(arr)):
    if not arr[i].isalnum():
        arr[i] = re.sub(r'[^\w]', '', arr[i])

humanCapitalParagraph = []
firstIndex = 0
lastIndex = 0

for i in range(len(arr)):
    if(arr[i].lower() == "human" and arr[i+1].lower() == "capital"):
        firstIndex = i
        #print("Hello")
        break

for i in range(firstIndex,len(arr)):
    if(arr[i].lower() == "table" and arr[i+1].lower() == "of" and arr[i+2].lower() == "contents"):
        lastIndex = i
        break

for i in range(firstIndex, lastIndex):
    humanCapitalParagraph.append(arr[i])

numOfEmployees = 0

for i in range(len(humanCapitalParagraph)):
    if(humanCapitalParagraph[i].isdigit() and int(humanCapitalParagraph[i]) > 2030 and int(humanCapitalParagraph[i]) > numOfEmployees):
        numOfEmployees = int(humanCapitalParagraph[i])

print("Total number of employees is: " + str(numOfEmployees))


#print(firstIndex)
#print(lastIndex)
#print(humanCapitalParagraph)
#wordsBeforeEmployees = []

#for i in range(len(arr)):
#    if(arr[i] == "employees"):
#        wordsBeforeEmployees.append(arr[i-1])

#print(wordsBeforeEmployees)

#numEmployees = 0

#for i in range(len(wordsBeforeEmployees)):
#    if(wordsBeforeEmployees[i].isdigit()):
#        numEmployees = int(wordsBeforeEmployees[i])

#print("Total number of employees is: " + str(numEmployees))
#print(str(arr))
#python3 employeeCounter.py > entirepdf.txt 


