import pymongo as pm
from datetime import * 
from time import * 


'''
	returns the dict of the parameters passed for fetching the data
'''
def get_param_dict(params):
	d = {}
	for p in params:
		d[p] = 1

	return d


def  get_data_tuple(params, collection_name,handler):

	'''
		returns the latest tuple
	'''
	param_dict = get_param_dict(params)
	now = int(time()) - 120 # back by 2 minutes

	print now

	data = {}
	for doc in handler[collection_name].find({'Timestamp':now},param_dict):
		
		for p in params:
			data[p] = doc[p]


	print data
	return data


def  get_N_data_tuples(T, params, collection_name,handler):

	'''
		returns the latest tuple
	'''
	param_dict = get_param_dict(params)
	end_now = int(time()) - 120 # back by 2 minutes
	st_now = int(time()) - 120 - T * 60 # back by T minutes 

	print st_now, end_now

	data = []
	for doc in handler[collection_name].find({'Timestamp':{'$gte':st_now, '$lte':end_now}},param_dict):
		d = {}
		for p in params:
			d[p] = doc[p]

		data.append(d)


	#print data
	return data






