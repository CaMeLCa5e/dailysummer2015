from __future__ import print_function 

import re 
import sys 
from operator import add 

from pyspark import SparkContext 

def computeContribs(urls, rank): 
	num_urls = len(urls)
	for url in urls: 
		yield (url, rank / num_urls)

def parseNeighbors(urls): 
	parts = re.split(r'\s+', urls)
	return parts[0], parts[1]

if __name__ == "__main__": 
	if len(sys.argv) != 3: 
		print ("Usage: pagerank <file><iterations>", file=sys.stderr)
		exit(-1)

	# initialize SC 
	sc = SparkContext(appName="PythonPageRank")

	lines = sc.textFile(sys.argv[1], 1)

	links = lines.map(lambda urls: parseNeighbors(urls)).distinct().groupByKey().cache()

	ranks = links.map(lambda url_neighbors: (url_neighbors[0], 1.0))

	for iteration in range(int(sys.argv[2])):
		contribs = links.join(ranks).flatMap(
			lambda url_urls_rank: computeContribs(url_urls_rank[1][0], url_urls_rank[1][1]))

		ranks = contribs.reduceByKey(add).mapValues(lambda rank: rank * 0.85 + 0.15)

	for (link, rank) in ranks.collect(): 
		print("%s has rank: %s." % (link, rank))

	sc.stop()
