enPages = paagecounts.filter(lambda x: x.split(" ")[1] == "en").cache()

print enPages.count()

enTuples = enPages.map(lambda x: x.split(" "))
enKeyValuePairs = enTuples.map(lambda x: (x[0], int(x[3])))

enKeyValuePairs.reduceByKey(lambda x, y: x + y, 1).collect()