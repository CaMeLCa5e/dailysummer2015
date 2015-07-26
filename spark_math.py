import numpy as np 

x = 5 

print type(sc)

data = sc.textFile('../rotten_tomatoes_train.tsv')
type(data)

print data.count()

negative_reviews = data.filter(lambda line: '0' == line.split('\t')[3])
print negative_reviews

print type(negative_reviews)

