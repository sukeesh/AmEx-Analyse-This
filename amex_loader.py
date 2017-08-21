import gzip
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def load_data_wrapper():	
	df = pd.read_csv("Training_Dataset.csv")

	min_vals = []
	max_vals = []
	for ix in xrange(45):
		min_vals.append(100000000)
		max_vals.append(-100000000)

	idx = 0
	for x in df:
		if x != 'mvar1' and x != 'cm_key' and x != 'mvar12':
			for y in df[x]:
				min_vals[idx] = min(min_vals[idx], y)
				max_vals[idx] = max(max_vals[idx], y)
			idx = idx + 1
		if x == 'mvar45':
			break

	training_list = []
	training_list_y = []

	test_list = []
	test_list_y = []

	minwn = -10000000

	i = 0
	for idx, row in df.iterrows():
		new_list = []
		idx = 0
		for x in df:
			if x != 'mvar1' and x != 'cm_key' and x != 'mvar12':
				to_p = float(row[x] - min_vals[idx])
				to_p = float(to_p) / float(max_vals[idx] - min_vals[idx])
				new_list.append(to_p)
				if ( to_p > minwn ):
					minwn = to_p
				idx = idx + 1
			if x == 'mvar45':
				break

		new_list_y = []
		new_list_y.append(0)
		new_list_y.append(0)
		new_list_y.append(0)

		for x in df:
			if x == 'mvar46' or x == 'mvar49':
				new_list_y[0] = new_list_y[0] or int(row[x])
				if new_list_y[1] == 1 or new_list_y[2] == 1:
					new_list_y[0] = 0
			elif x == 'mvar47' or x == 'mvar50':
				new_list_y[1] = new_list_y[1] or int(row[x])
				if new_list_y[0] == 1 or new_list_y[2] == 1:
					new_list_y[1] = 0
			elif x == 'mvar48' or x == 'mvar51':
				new_list_y[2] = new_list_y[2] or int(row[x])
				if new_list_y[0] == 1 or new_list_y[1] == 1:
					new_list_y[2] = 0
		
		if i < 36000:
			training_list.append(new_list)
			training_list_y.append(new_list_y)
		else:
			test_list.append(new_list)
			test_list_y.append(new_list_y)

		i = i + 1

	print minwn	

	training_inputs = [np.reshape(x, (43, 1)) for x in training_list]
	training_results = [np.reshape(x, (3, 1)) for x in training_list_y]

	testing_inputs = [np.reshape(x, (43, 1)) for x in test_list]
	testing_results = [np.reshape(x, (3, 1)) for x in test_list_y]

	training_data = zip(training_inputs, training_results)
	testing_data = zip(testing_inputs, testing_results)

	return (training_data, testing_data)
