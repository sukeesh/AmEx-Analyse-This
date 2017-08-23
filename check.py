import gzip
import numpy as np
import pandas as pd
from sets import Set

df = pd.read_csv("Training_Dataset.csv")

m = df['mvar14']

a = -10000000
b =  10000000

st = Set([])

for i in m:
	st.add(i)
	a = max(a, i)
	b = min(b, i)

for i in st:
	print i