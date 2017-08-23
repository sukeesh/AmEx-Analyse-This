import gzip
import numpy as np
import pandas as pd

def ret_val(stro):
	strl = str(stro)
	if "Du" in strl:
		return 1.0
	if "Per" in strl:
		return 2.0
	if "Const" in strl:
		return 3.0
	if "Fi" in strl:
		return 4.0
	if "Ho" in strl:
		return 5.0
	if "En" in strl:
		return 6.0
	if "Mis" in strl:
		return 7.0
	if "No" in strl:
		return 8.0
	if "Ap" in strl:
		return 9.0
	if "Of" in strl:
		return 10.0
	if "Consu" in strl:
		return 11.0
	if "Ma" in strl:
		return 12.0
	if "So" in strl:
		return 13.0
	if "Au" in strl:
		return 14.0
	if "Pr" in strl:
		return 15.0
	if "Tr" in strl:
		return 16.0
	if "Un" in strl:
		return 17.0
	if "Mi" in strl:
		return 18.0

def load_data_wrapper():	
	df = pd.read_csv("Training_Dataset.csv")

	min_vals = []
	max_vals = []

	a = -1.0
	b =  1.0

	features = 25

	for ix in xrange(30):
		min_vals.append(1000000)
		max_vals.append(-1000000)

	theGarbage = ['cm_key', 'mvar1', 'mvar3', 'mvar17', 'mvar18', 'mvar19', 'mvar21', 'mvar22', 'mvar23', 'mvar25', 'mvar26', 'mvar27', 'mvar29', 'mvar30', 'mvar31', 'mvar33', 'mvar34', 'mvar35', 'mvar37', 'mvar38', 'mvar39']

	idx = 0
	for x in df:
		if x in theGarbage:
			theGarbage2 = 0
		elif x == 'mvar12':
			for y in df[x]:
				min_vals[idx] = min(min_vals[idx], float(ret_val(str(y))))
				max_vals[idx] = max(max_vals[idx], float(ret_val(str(y))))
			idx = idx + 1
		elif x == 'mvar16':
			y = 0
			leng = len(df[x])
			while y < leng:
				theSum = float(df.get_value(y, x) + df.get_value(y, 'mvar17') + df.get_value(y, 'mvar18') + df.get_value(y, 'mvar19'))/float(4.0)
				min_vals[idx] = min(min_vals[idx], theSum)
				max_vals[idx] = max(max_vals[idx], theSum)
				y = y + 1
			idx = idx + 1
		elif x == 'mvar20':
			y = 0
			leng = len(df[x])
			while y < leng:
				theSum = float(df.get_value(y, x) + df.get_value(y, 'mvar21') + df.get_value(y, 'mvar22') + df.get_value(y, 'mvar23'))/float(4.0)
				min_vals[idx] = min(min_vals[idx], theSum)
				max_vals[idx] = max(max_vals[idx], theSum)
				y = y + 1
			idx = idx + 1
		elif x == 'mvar24':
			y = 0
			leng = len(df[x])
			while y < leng:
				theSum = float(df.get_value(y, x) + df.get_value(y, 'mvar25') + df.get_value(y, 'mvar26') + df.get_value(y, 'mvar27'))/float(4.0)
				min_vals[idx] = min(min_vals[idx], theSum)
				max_vals[idx] = max(max_vals[idx], theSum)
				y = y + 1
			idx = idx + 1
		elif x == 'mvar28':
			y = 0
			leng = len(df[x])
			while y < leng:
				theSum = float(df.get_value(y, x) + df.get_value(y, 'mvar29') + df.get_value(y, 'mvar30') + df.get_value(y, 'mvar31'))/float(4.0)
				min_vals[idx] = min(min_vals[idx], theSum)
				max_vals[idx] = max(max_vals[idx], theSum)
				y = y + 1
			idx = idx + 1
		elif x == 'mvar32':
			y = 0
			leng = len(df[x])
			while y < leng:
				theSum = float(df.get_value(y, x) + df.get_value(y, 'mvar33') + df.get_value(y, 'mvar34') + df.get_value(y, 'mvar35'))/float(4.0)
				min_vals[idx] = min(min_vals[idx], theSum)
				max_vals[idx] = max(max_vals[idx], theSum)
				y = y + 1
			idx = idx + 1
		elif x == 'mvar36':
			y = 0
			leng = len(df[x])
			while y < leng:
				theSum = float(df.get_value(y, x) + df.get_value(y, 'mvar37') + df.get_value(y, 'mvar38') + df.get_value(y, 'mvar39'))/float(4.0)
				min_vals[idx] = min(min_vals[idx], theSum)
				max_vals[idx] = max(max_vals[idx], theSum)
				y = y + 1
			idx = idx + 1
		# elif x == 'mvar14':
		# 	for y in df[x]:
		# 		if y == 1:
		# 			min_vals[idx] = min(min_vals[idx], y)
		# 			max_vals[idx] = max(max_vals[idx], y)
		# 		else:
		# 			min_vals[idx] = min(min_vals[idx], 0)
		# 			max_vals[idx] = max(max_vals[idx], 0)
		# 	idx = idx + 1
		# elif x == 'mvar15':
		# 	for y in df[x]:
		# 		if y == 1:
		# 			min_vals[idx] = min(min_vals[idx], 0)
		# 			max_vals[idx] = max(max_vals[idx], 0)
		# 		else:
		# 			min_vals[idx] = min(min_vals[idx], 1)
		# 			max_vals[idx] = max(max_vals[idx], 1)
		# 	idx = idx + 1
		else:
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

	maxa = -10000000
	mina = 10000000

	i = 0
	for row in df.iterrows():
		i = i + 1
		new_list = []
		idx = 0
		for x in df:
			if x in theGarbage:
				theGarbage2 = 0
			elif x == 'mvar16':
				to_p = float(row[1][x] + row[1]['mvar17'] + row[1]['mvar18'] + row[1]['mvar19'])
				to_p = ((to_p / 4.0) - min_vals[idx]) / float(max_vals[idx] - min_vals[idx])
				new_list.append(((b - a) * to_p) + (a * 1.0))
				maxa = max(maxa, ((b - a) * to_p) + (a * 1.0))
				mina = min(mina, ((b - a) * to_p) + (a * 1.0))
				idx = idx + 1
			elif x == 'mvar20':
				to_p = float(row[1][x] + row[1]['mvar21'] + row[1]['mvar22'] + row[1]['mvar23'])
				to_p = ((to_p / 4.0) - min_vals[idx]) / float(max_vals[idx] - min_vals[idx])
				new_list.append(((b - a) * to_p) + (a * 1.0))
				maxa = max(maxa, ((b - a) * to_p) + (a * 1.0))
				mina = min(mina, ((b - a) * to_p) + (a * 1.0))
				idx = idx + 1
			elif x == 'mvar24':
				to_p = float(row[1][x] + row[1]['mvar25'] + row[1]['mvar26'] + row[1]['mvar27'])
				to_p = ((to_p / 4.0) - min_vals[idx]) / float(max_vals[idx] - min_vals[idx])
				new_list.append(((b - a) * to_p) + (a * 1.0))
				maxa = max(maxa, ((b - a) * to_p) + (a * 1.0))
				mina = min(mina, ((b - a) * to_p) + (a * 1.0))
				idx = idx + 1
			elif x == 'mvar28':
				to_p = float(row[1][x] + row[1]['mvar29'] + row[1]['mvar30'] + row[1]['mvar31'])
				to_p = ((to_p / 4.0) - min_vals[idx]) / float(max_vals[idx] - min_vals[idx])
				new_list.append(((b - a) * to_p) + (a * 1.0))
				maxa = max(maxa, ((b - a) * to_p) + (a * 1.0))
				mina = min(mina, ((b - a) * to_p) + (a * 1.0))
				idx = idx + 1
			elif x == 'mvar32':
				to_p = float(row[1][x] + row[1]['mvar33'] + row[1]['mvar34'] + row[1]['mvar35'])
				to_p = ((to_p / 4.0) - min_vals[idx]) / float(max_vals[idx] - min_vals[idx])
				new_list.append(((b - a) * to_p) + (a * 1.0))
				maxa = max(maxa, ((b - a) * to_p) + (a * 1.0))
				mina = min(mina, ((b - a) * to_p) + (a * 1.0))
				idx = idx + 1
			elif x == 'mvar36':
				to_p = float(row[1][x] + row[1]['mvar37'] + row[1]['mvar38'] + row[1]['mvar39'])
				to_p = ((to_p / 4.0) - min_vals[idx]) / float(max_vals[idx] - min_vals[idx])
				new_list.append(((b - a) * to_p) + (a * 1.0))
				maxa = max(maxa, ((b - a) * to_p) + (a * 1.0))
				mina = min(mina, ((b - a) * to_p) + (a * 1.0))
				idx = idx + 1
			elif x == 'mvar12':
				to_p = float(ret_val(row[1][x]) - min_vals[idx])
				to_p = float(to_p) / float(max_vals[idx] - min_vals[idx])
				new_list.append(((b - a) * to_p) + (a * 1.0))
				maxa = max(maxa, ((b - a) * to_p) + (a * 1.0))
				mina = min(mina, ((b - a) * to_p) + (a * 1.0))
				idx = idx + 1
			# elif x == 'mvar14':
			# 	if row[1][x] == 1:
			# 		to_p = float(row[1][x] - min_vals[idx])
			# 		to_p = float(to_p) / float(float(max_vals[idx]) - float(min_vals[idx]))
			# 		new_list.append(((b - a) * to_p) + (a * 1.0))
			# 		maxa = max(maxa, ((b - a) * to_p) + (a * 1.0))
			# 		mina = min(mina, ((b - a) * to_p) + (a * 1.0))
			# 		idx = idx + 1
			# 	else:
			# 		to_p = float(0 - min_vals[idx])
			# 		to_p = float(to_p) / float(float(max_vals[idx]) - float(min_vals[idx]))
			# 		new_list.append(((b - a) * to_p) + (a * 1.0))
			# 		maxa = max(maxa, ((b - a) * to_p) + (a * 1.0))
			# 		mina = min(mina, ((b - a) * to_p) + (a * 1.0))
			# 		idx = idx + 1
			# elif x == 'mvar15':
			# 	if row[1][x] == 0:
			# 		to_p = float(1 - min_vals[idx])
			# 		to_p = float(to_p) / float(float(max_vals[idx]) - float(min_vals[idx]))
			# 		new_list.append(((b - a) * to_p) + (a * 1.0))
			# 		maxa = max(maxa, ((b - a) * to_p) + (a * 1.0))
			# 		mina = min(mina, ((b - a) * to_p) + (a * 1.0))
			# 		idx = idx + 1
			# 	else:
			# 		to_p = float(0 - min_vals[idx])
			# 		to_p = float(to_p) / float(float(max_vals[idx]) - float(min_vals[idx]))
			# 		new_list.append(((b - a) * to_p) + (a * 1.0))
			# 		maxa = max(maxa, ((b - a) * to_p) + (a * 1.0))
			# 		mina = min(mina, ((b - a) * to_p) + (a * 1.0))
			# 		idx = idx + 1
			else:
				to_p = float(row[1][x] - min_vals[idx])
				to_p = float(to_p) / float(float(max_vals[idx]) - float(min_vals[idx]))
				new_list.append(((b - a) * to_p) + (a * 1.0))
				maxa = max(maxa, ((b - a) * to_p) + (a * 1.0))
				mina = min(mina, ((b - a) * to_p) + (a * 1.0))
				idx = idx + 1
			if x == 'mvar45':
				break

		new_list_y = []
		new_list_y.append(0)
		new_list_y.append(0)
		new_list_y.append(0)

		for x in df:
			if x == 'mvar46' or x == 'mvar49':
				new_list_y[0] = new_list_y[0] or int(row[1][x])
				if new_list_y[1] == 1 or new_list_y[2] == 1:
					new_list_y[0] = 0
			elif x == 'mvar47' or x == 'mvar50':
				new_list_y[1] = new_list_y[1] or int(row[1][x])
				if new_list_y[0] == 1 or new_list_y[2] == 1:
					new_list_y[1] = 0
			elif x == 'mvar48' or x == 'mvar51':
				new_list_y[2] = new_list_y[2] or int(row[1][x])
				if new_list_y[0] == 1 or new_list_y[1] == 1:
					new_list_y[2] = 0
		
		if i < 70000:
			training_list.append(new_list)
			training_list_y.append(new_list_y)
		else:
			test_list.append(new_list)
			test_list_y.append(new_list_y)

		i = i + 1

	print mina, maxa

	training_inputs = [np.reshape(x, (features, 1)) for x in training_list]
	training_results = [np.reshape(x, (3, 1)) for x in training_list_y]

	testing_inputs = [np.reshape(x, (features, 1)) for x in test_list]
	testing_results = [np.reshape(x, (3, 1)) for x in test_list_y]

	training_data = zip(training_inputs, training_results)
	testing_data = zip(testing_inputs, testing_results)

	return (training_data, testing_data)
