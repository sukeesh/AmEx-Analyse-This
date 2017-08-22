import gzip
import numpy as np
import pandas as pd

def ret_val(stro):
	strl = str(stro)
	if "Dur" in strl:
		return 1.0
	if "Per" in strl:
		return 2.0
	if "Const" in strl:
		return 3.0
	if "Fin" in strl:
		return 4.0
	if "Hou" in strl:
		return 5.0
	if "Ent" in strl:
		return 6.0
	if "Mis" in strl:
		return 7.0
	if "Non" in strl:
		return 8.0
	if "App" in strl:
		return 9.0
	if "Off" in strl:
		return 10.0
	if "Consu" in strl:
		return 11.0
	if "Manufa" in strl:
		return 12.0
	if "Soci" in strl:
		return 13.0
	if "Autom" in strl:
		return 14.0
	if "Produ" in strl:
		return 15.0
	if "Tran" in strl:
		return 16.0
	if "Unkno" in strl:
		return 17.0
	if "Mining" in strl:
		return 18.0

def load_data_wrapper():	
	df = pd.read_csv("Training_Dataset.csv")

	min_vals = []
	max_vals = []

	for ix in xrange(46):
		min_vals.append(100000000)
		max_vals.append(-100000000)

	idx = 0
	for x in df:
		print "Done processing {0} this".format(x)
		if x == 'mvar17' or x == 'mvar18' or x == 'mvar19' or x == 'mvar21' or x == 'mvar22' or x == 'mvar23' or x == 'mvar25':
			garbage = 0
		elif x == 'mvar26' or x == 'mvar27' or x == 'mvar29' or x == 'mvar30' or x == 'mvar31' or x == 'mvar33' or x == 'mvar34':
			garbage = 0
		elif x == 'mvar35' or x == 'mvar37' or x == 'mvar38' or x == 'mvar39':
			garbage = 0
		elif x == 'mvar12':
			for y in df[x]:
				min_vals[idx] = min(min_vals[idx], float(ret_val(str(y))))
				max_vals[idx] = max(max_vals[idx], float(ret_val(str(y))))
			idx = idx + 1
		elif x == 'mvar16':
			y = 0
			while y < len(df[x]):
				min_vals[idx] = min(min_vals[idx], float(df[x][y] + df['mvar17'][y] + df['mvar18'][y] + df['mvar19'][y])/float(4.0) )
				max_vals[idx] = max(max_vals[idx], float(df[x][y] + df['mvar17'][y] + df['mvar18'][y] + df['mvar19'][y])/float(4.0) )
				y = y + 1
		elif x == 'mvar20':
			y = 0
			while y < len(df[x]):
				min_vals[idx] = min(min_vals[idx], float(df[x][y] + df['mvar21'][y] + df['mvar22'][y] + df['mvar23'][y])/float(4.0) )
				max_vals[idx] = max(max_vals[idx], float(df[x][y] + df['mvar21'][y] + df['mvar22'][y] + df['mvar23'][y])/float(4.0) )
				y = y + 1
		elif x == 'mvar24':
			y = 0
			while y < len(df[x]):
				min_vals[idx] = min(min_vals[idx], float(df[x][y] + df['mvar25'][y] + df['mvar26'][y] + df['mvar27'][y])/float(4.0) )
				max_vals[idx] = max(max_vals[idx], float(df[x][y] + df['mvar25'][y] + df['mvar26'][y] + df['mvar27'][y])/float(4.0) )
				y = y + 1
		elif x == 'mvar28':
			y = 0
			while y < len(df[x]):
				min_vals[idx] = min(min_vals[idx], float(df[x][y] + df['mvar29'][y] + df['mvar30'][y] + df['mvar31'][y])/float(4.0) )
				max_vals[idx] = max(max_vals[idx], float(df[x][y] + df['mvar29'][y] + df['mvar30'][y] + df['mvar31'][y])/float(4.0) )
				y = y + 1
		elif x == 'mvar32':
			y = 0
			while y < len(df[x]):
				min_vals[idx] = min(min_vals[idx], float(df[x][y] + df['mvar33'][y] + df['mvar34'][y] + df['mvar35'][y])/float(4.0) )
				max_vals[idx] = max(max_vals[idx], float(df[x][y] + df['mvar33'][y] + df['mvar34'][y] + df['mvar35'][y])/float(4.0) )
				y = y + 1
		elif x == 'mvar36':
			y = 0
			while y < len(df[x]):
				min_vals[idx] = min(min_vals[idx], float(df[x][y] + df['mvar37'][y] + df['mvar38'][y] + df['mvar39'][y])/float(4.0) )
				max_vals[idx] = max(max_vals[idx], float(df[x][y] + df['mvar37'][y] + df['mvar38'][y] + df['mvar39'][y])/float(4.0) )
				y = y + 1
		elif x != 'mvar1' and x != 'cm_key':
			for y in df[x]:
				min_vals[idx] = min(min_vals[idx], y)
				max_vals[idx] = max(max_vals[idx], y)
			idx = idx + 1
		if x == 'mvar45':
			break


	leaderboard_data = []
	a = -1
	b = 1

	for idx, row in df.iterrows():
		print "Done processing {0}\n".format(idx)
		new_list = []
		idx = 0
		for x in df:
			if x == 'mvar17' or x == 'mvar18' or x == 'mvar19' or x == 'mvar21' or x == 'mvar22' or x == 'mvar23' or x == 'mvar25':
				garbage = 0
			elif x == 'mvar26' or x == 'mvar27' or x == 'mvar29' or x == 'mvar30' or x == 'mvar31' or x == 'mvar33' or x == 'mvar34':
				garbage = 0
			elif x == 'mvar35' or x == 'mvar37' or x == 'mvar38' or x == 'mvar39':
				garbage = 0
			elif x == 'mvar12':
				for y in df[x]:
					min_vals[idx] = min(min_vals[idx], float(ret_val(str(y))))
					max_vals[idx] = max(max_vals[idx], float(ret_val(str(y))))
				idx = idx + 1
			elif x == 'mvar16':
				to_p = float((float(row[x] + row['mvar17'] + row['mvar18'] + row['mvar19'])/float(4.0)) - min_vals[idx])
				to_p = float(to_p) / float(float(max_vals[idx]) - float(min_vals[idx]))
				new_list.append(((b - a) * 1.0 * to_p) + (a * 1.0))
				idx = idx + 1
			elif x == 'mvar20':
				to_p = float((float(row[x] + row['mvar21'] + row['mvar22'] + row['mvar23'])/float(4.0)) - min_vals[idx])
				to_p = float(to_p) / float(float(max_vals[idx]) - float(min_vals[idx]))
				new_list.append(((b - a) * 1.0 * to_p) + (a * 1.0))
				idx = idx + 1
			elif x == 'mvar24':
				to_p = float((float(row[x] + row['mvar25'] + row['mvar26'] + row['mvar27'])/float(4.0)) - min_vals[idx])
				to_p = float(to_p) / float(float(max_vals[idx]) - float(min_vals[idx]))
				new_list.append(((b - a) * 1.0 * to_p) + (a * 1.0))
				idx = idx + 1
			elif x == 'mvar28':
				to_p = float((float(row[x] + row['mvar29'] + row['mvar30'] + row['mvar31'])/float(4.0)) - min_vals[idx])
				to_p = float(to_p) / float(float(max_vals[idx]) - float(min_vals[idx]))
				new_list.append(((b - a) * 1.0 * to_p) + (a * 1.0))
				idx = idx + 1
			elif x == 'mvar32':
				to_p = float((float(row[x] + row['mvar33'] + row['mvar34'] + row['mvar35'])/float(4.0)) - min_vals[idx])
				to_p = float(to_p) / float(float(max_vals[idx]) - float(min_vals[idx]))
				new_list.append(((b - a) * 1.0 * to_p) + (a * 1.0))
				idx = idx + 1
			elif x == 'mvar36':
				to_p = float((float(row[x] + row['mvar37'] + row['mvar38'] + row['mvar39'])/float(4.0)) - min_vals[idx])
				to_p = float(to_p) / float(float(max_vals[idx]) - float(min_vals[idx]))
				new_list.append(((b - a) * 1.0 * to_p) + (a * 1.0))
				idx = idx + 1
			elif x == 'mvar12':
				to_p = float(ret_val(row[x]) - min_vals[idx])
				to_p = float(to_p) / float(float(max_vals[idx]) - float(min_vals[idx]))
				new_list.append(((b - a) * 1.0 * to_p) + (a * 1.0))
				idx = idx + 1
			elif x != 'mvar1' and x != 'cm_key':
				to_p = float(row[x] - min_vals[idx])
				to_p = float(to_p) / float(float(max_vals[idx]) - float(min_vals[idx]))
				new_list.append(((b - a) * 1.0 * to_p) + (a * 1.0))
				idx = idx + 1
			if x == 'mvar45':
				break

		leaderboard_data.append(new_list)

	leaderboard_data = [np.reshape(x, (26, 1)) for x in leaderboard_data]

	return leaderboard_data
