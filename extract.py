import gzip
import numpy as np
import pandas as pd

df = pd.read_csv("Training_Dataset.csv")

m14 = df['mvar5']

cnt = []
for i in xrange(400):
	cnt.append(0)

m46 = df['mvar48']
m47 = df['mvar51']
ix = 0
while ix < len(m46):
	if m46[ix] == 1 or m47[ix] == 1:
		cnt[m14[ix]] = cnt[m14[ix]] + 1
	ix = ix + 1

for i in xrange(356):
	print cnt[i]