import gzip
import numpy as np
import pandas as pd

df = pd.read_csv("Training_Dataset.csv")

m = df['mvar45']


for i in m:
	print i
