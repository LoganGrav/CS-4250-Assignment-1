#-------------------------------------------------------------------------
# AUTHOR: Logan Gravitt
# FILENAME: indexing.py
# SPECIFICATION: tf-idf calculator
# FOR: CS 4250- Assignment #1
# TIME SPENT: 2 hours
#-----------------------------------------------------------*/
#Importing some Python libraries
import csv
import numpy


documents = []
#Reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
            if i > 0: # skipping the header
                documents.append (row[0])

#Conducting stopword removal for pronouns/conjunctions. Hint: use a set to define your stopwords.
#--> add your Python code here
stopWords = {'I', 'She', 'They', 'her', 'their', 'and'}

#Conducting stemming. Struggled with a dictionary, but this works :P.
#--> add your Python code here
def stemming(word):
    if word == "loves" :
        return "love"
    elif word == "cats" :
        return "cat"
    elif word == "dogs" :
        return "dog"
    else:
        return word


#Identifying the index terms.
#--> add your Python code here
new_data = []
for doc in documents:
    tokens = [stemming(word) for word in doc.split() if word not in stopWords] #remove stopwords
    new_data.append(' '.join(tokens))

term_set = set()
for doc in new_data:
    term_set.update(doc)

terms = sorted(term_set)

#Building the document-term matrix by using the tf-idf weights.
#--> add your Python code here
docTermMatrix = numpy.zeros((len(new_data), len(terms)))
for doc_idx, doc in enumerate(new_data):
    tf = defaultdict(int)
    for term in doc:
        tf[term] += 1

    for term in tf:
        if term in terms:
            term_index = terms.index(term)
            docTermMatrix[doc_idx][term_index] = tf[term]

idf = {}
num_docs = len(new_data)

for term in terms:
    doc_count = sum(1 for doc in new_data if term in doc)
    idf[term] = numpy.log(num_docs/doc_count)

final_matrix = docTermMatrix * numpy.array([idf[term] for term in terms])



#Printing the document-term matrix.
#--> add your Python code here


for i, doc in enumerate(tfidf_matrix):
    print(f"Document {i + 1}:", doc)
