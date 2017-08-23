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

	for ix in xrange(30):
		min_vals.append(1000000)
		max_vals.append(-1000000)

	theGarbage = ['mvar17', 'mvar18', 'mvar19', 'mvar21', 'mvar22', 'mvar23', 'mvar25', 'mvar26', 'mvar27', 'mvar29', 'mvar30', 'mvar31', 'mvar33', 'mvar34', 'mvar35', 'mvar37', 'mvar38', 'mvar39']

	idx = 0
	for x in df:
		# print "Done processing {0} this".format(x)
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
		elif x != 'mvar1' and x != 'cm_key':
			for y in df[x]:
				min_vals[idx] = min(min_vals[idx], y)
				max_vals[idx] = max(max_vals[idx], y)
			idx = idx + 1
		if x == 'mvar45':
			break

	# print idx

	leaderboard_data = []
	a = -1.0
	b = 1.0

	for row in df.iterrows():
		print row[1]['mvar3']

	for row in df.iterrows():
		new_list = []
		idx = 0
		iy = 0
		for x in df:
			# print x, idx
			# print iy
			if x in theGarbage:
				theGarbage2 = 0
			elif x == 'mvar12':
				for y in df[x]:
					min_vals[idx] = min(min_vals[idx], float(ret_val(str(y))))
					max_vals[idx] = max(max_vals[idx], float(ret_val(str(y))))
				idx = idx + 1
			elif x == 'mvar16' or x == 'mvar20' or x == 'mvar24' or x == 'mvar28' or x == 'mvar28' or x == 'mvar32' or x == 'mvar36':
				to_p = 0.0 + float(row[iy])
				to_p = to_p + float(row[iy + 1])
				to_p = to_p + float(row[iy + 2])
				to_p = to_p + float(row[iy + 3])
				to_p = to_p / float(4.0)
				to_p = to_p - min_vals[idx]
				to_p = to_p / float(float(max_vals[idx]) - float(min_vals[idx]))
				new_list.append(((b - a) * to_p) + (a * 1.0))
				idx = idx + 1
			elif x == 'mvar12':
				to_p = float(ret_val(row[iy]) - min_vals[idx])
				to_p = float(to_p) / float(float(max_vals[idx]) - float(min_vals[idx]))
				new_list.append(((b - a) * to_p) + (a * 1.0))
				idx = idx + 1
			elif x != 'mvar1' and x != 'cm_key':
				print iy, x
				to_p = float(row[iy] - min_vals[idx])
				to_p = float(to_p) / float(float(max_vals[idx]) - float(min_vals[idx]))
				new_list.append(((b - a) * to_p) + (a * 1.0))
				idx = idx + 1
			if x == 'mvar45':
				break
			iy = iy + 1

		leaderboard_data.append(new_list)

	leaderboard_data = [np.reshape(x, (25, 1)) for x in leaderboard_data]

	return leaderboard_data
