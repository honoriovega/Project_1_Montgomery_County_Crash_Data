import pickle

def loadData():

	fin = open('data.pickle','r')

	data = pickle.load(fin)
	fin.close()
	return data


data = loadData()
