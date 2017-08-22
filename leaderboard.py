import numpy as np
import pandas as pd

def load_data_wrapper():	
	df = pd.read_csv("Leaderboard_Dataset.csv")

	min_vals = []
	max_vals = []
	for ix in xrange(45):
		min_vals.append(1000000)
		max_vals.append(-1000000)

	idx = 0
	for x in df:
		if x != 'mvar1' and x != 'cm_key' and x != 'mvar12':
			for y in df[x]:
				min_vals[idx] = min(min_vals[idx], y)
				max_vals[idx] = max(max_vals[idx], y)
			idx = idx + 1
		if x == 'mvar45':
			break

	leaderboard_data = []
	for idx, row in df.iterrows():
		new_list = []
		idx = 0
		for x in df:
			if x != 'mvar1' and x != 'cm_key' and x != 'mvar12':
				to_p = float(row[x] - min_vals[idx])
				to_p = float(to_p) / float(max_vals[idx] - min_vals[idx])
				new_list.append(to_p)
				idx = idx + 1
			if x == 'mvar45':
				break
		leaderboard_data.append(new_list)

	leaderboard_data = [np.reshape(x, (43, 1)) for x in leaderboard_data]

	return leaderboard_data