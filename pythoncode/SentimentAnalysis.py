# import parser object from tike
import re

from tika import parser

# opening pdf file
parsed_pdf = parser.from_file("3m_10-K.pdf")
  
# saving content of pdf
# you can also bring text only, by parsed_pdf['text'] 
# parsed_pdf['content'] returns string 
data = parsed_pdf['content'] 

# Data Sanitization
arr = data.split() # Split single string into array of words

for i in range(len(arr)):
    if not arr[i].isalnum():
        arr[i] = re.sub(r'[^\w]', '', arr[i])

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
    print(str(array[i]) + " exists: " + str(wordStore[i]) + " times.")

wordsFound = 0
for i in wordStore:
    if i != 0:
        wordsFound += 1

print("Ratio of words found: " + str(round((wordsFound / len(array)) * 100, 2)) + "%")

totalNumberOfWords = len(arr)

print("Total number of words in document: " + str(totalNumberOfWords))

#python3 SentimentAnalysis.py > 10K_NLP_%ofterms.txt 
#to make to text
# get into code
# ls --> cd Desktop ----> cd codingforlcg 
