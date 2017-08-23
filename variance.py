import gzip
import numpy as np
import pandas as pd

df = pd.read_csv("Training_Dataset.csv")

def sqr(x):
	x = x * 1.0 * x
	return x

for theFeature in df:
	if theFeature == 'mvar1' or theFeature == 'mvar12':
		# do nothing here
		fs = 10
	else:
		theMean = 0.0
		n = 0.0
		for x in df[theFeature]:
			theMean = theMean + float(x)
			n = n + 1.0

		theMean = theMean / float(n)

		vari = 0.0
		for x in df[theFeature]:
			vari = vari + float(sqr(x - theMean))

		vari = vari / float((n - 1.0) * 1.0)

		print vari