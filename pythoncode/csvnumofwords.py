# import parser object from tike
import re
import csv
from tika import parser

# opening pdf file
parsed_pdf = parser.from_file("American Public Education Inc Annual Report 10-K.pdf")

# file you're writing to
#
f = open('testsheet.csv', 'w')

# CSV Writer
writer = csv.writer(f)

# saving content of pdf
# you can also bring text only, by parsed_pdf['text'] 
# parsed_pdf['content'] returns string 
data = parsed_pdf['content'] 

# Data Sanitization
arr = data.split() # Split single string into array of words

for i in range(len(arr)):
    if not arr[i].isalnum():
        arr[i] = re.sub(r'[^\w]', '', arr[i])
oldarr=arr
#print(arr)

array = ['Heart',
'Human',
'Humanity',
'Humane',
'Feel',
'Feeling',
'Understand',
'Understanding',
'Compassionate',
'Sympathetic',
'Belong',
'Belonging',
'Person',
'People',
'Love',
'Loving',
'Community',
'Communities',
'Empathy',
'Empath',
'Empathetic',
'Nurture',
'Nurturing',
'Culture',
'Cultural',
'Cultures',
'Spirit',
'Spiritual Engagement',
'Emotional Engagement',
'Mental Engagement',
'Physical Engagement',
'Inclusion',
'Inclusive',
'Diversity',
'Diversify',
'Equitable',
'Equity',
'Accessibility',
'Sustainability',
'Sustainability',
'Collaboration',
'Collaborative',
'Environment',
'Peer',
'Peers',
'Sensitive',
'Sensitivity',
'Care',
'Caring',
'Protect',
'Protection',
'Protecting']
#print(array)

wordStore= [0] * len(array)

for i in range(len(array)):
    for y in arr:
        if array[i].lower() == y.lower():
            wordStore[i] += 1

for i in range(len(array)):
    print(str(array[i]) + " ,exists:, " + str(wordStore[i]) + ",times,")
    arr = [str(array[i]), "exists:", str(wordStore[i]),  "times"]
    writer.writerow(arr)

wordsFound = 0
for i in wordStore:
    if i != 0:
        wordsFound += 1


print("Ratio,of,words,found:," + str(round((wordsFound / len(array)) * 100, 2)) + "%")
arr = ["Ratio of words found:", str(round((wordsFound / len(array)) * 100, 2)) + "%"]
writer.writerow(arr)

totalNumberOfWords = len(oldarr)
#print(oldarr)

print("Total,number,of,words,in,document:," + str(totalNumberOfWords))
arr = ["Ratio of words found:", str(round((wordsFound / len(array)) * 100, 2)) + "%"]
writer.writerow(arr)

#close the file
f.close()

#python3 csvnumofwords.py > _num_of_words.csv 
#python3 csvnumofwords.py > 10K_NLP_%ofterms.csv
#to make to text
# get into code
# ls --> cd Desktop ----> cd codingforlcg 
