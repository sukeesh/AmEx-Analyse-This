import gzip
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Training_Dataset.csv")

i = 0

training_list = []
training_list_y = []

validation_list = []
validation_list_y = []

test_list = []
test_list_y = []

for idx, row in df.iterrows():
	new_list = []
	for x in df:
		if x != 'mvar1' and x != 'cm_key':
			new_list.append(row[x])
		if x == 'mvar45':
			break

	new_list_y = []
	new_list_y.append(0)
	new_list_y.append(0)
	new_list_y.append(0)

	for x in df:
		if x == 'mvar46' or x == 'mvar49':
			new_list_y[0] = new_list_y[0] or int(row[x])
		elif x == 'mvar47' or x == 'mvar50':
			new_list_y[1] = new_list_y[1] or int(row[x])
		elif x == 'mvar48' or x == 'mvar51':
			new_list_y[2] = new_list_y[2] or int(row[x])
	
	if i < 20000:
		training_list.append(new_list)
		training_list_y.append(new_list_y)	
	elif i < 30000:
		validation_list.append(new_list)
		validation_list_y.append(new_list_y)
	else:
		test_list.append(new_list)
		test_list_y.append(new_list_y)

	i = i + 1

training_inputs = [np.reshape(x, (44, 1)) for x in training_list]
training_results = [np.reshape(x, (3, 1)) for x in training_list_y]

validation_inputs = [np.reshape(x, (44, 1)) for x in validation_list]
validation_results = [np.reshape(x, (3, 1)) for x in validation_list_y]

testing_inputs = [np.reshape(x, (44, 1)) for x in test_list]
testing_results = [np.reshape(x, (3, 1)) for x in test_list_y]

training_data = zip(training_inputs, training_results)
validation_data = zip(validation_inputs, validation_results)
testing_data = zip(testing_inputs, testing_results)
