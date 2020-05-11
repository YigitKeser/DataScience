from csv import reader
import numpy as np

# loading data into np array
def read_data(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	return np.array(dataset)

# split train test using first and fourth features
def train_test_split(dataset):
    X = dataset[:,[0,3,4]]
    train = np.concatenate([X[:30] , X[50:80] , X[100:130]])
    test = np.concatenate([X[30:50] ,X[80:100] , X[130:150]])
    return train ,test

# distance calculater
def get_distance(datapoint1, datapoint2, distance_metric):
    distance = 0.0
    if distance_metric == 'euclidian': # use euclidian 
        for i in range(len(datapoint1)-1):
            distance += (datapoint1[i].astype(float) - datapoint2[i].astype(float))**2
        return np.sqrt(distance)
    if distance_metric == 'manhattan': # use manhattan
        for i in range(len(datapoint1)-1):
            distance += abs(datapoint1[i].astype(float) - datapoint2[i].astype(float))
        return distance
        
# find neighbors
def get_neighbors(train, test_row, num_neighbors ,distance_metric):
	distances = list()
	for train_row in train:
		dist = get_distance(test_row, train_row , distance_metric)
		distances.append((train_row, dist))
	distances.sort(key=lambda tup: tup[1])
	neighbors = list()
	for i in range(num_neighbors):
		neighbors.append(distances[i][0])
	return neighbors

# prediction function
def predict(train, test_row, num_neighbors, distance_metric):
	neighbors = get_neighbors(train, test_row, num_neighbors , distance_metric)
	output_values = [row[-1] for row in neighbors]
	prediction = max(set(output_values), key=output_values.count)
	return prediction

# calculate accuracy
def accuracy(train ,test ,num_neighbors ,distance_metric):
    success = 0
    fail = 0
    for i in range(len(test)):
        predicted = predict(train, test[i], num_neighbors, distance_metric)
        actual = test[i,[2]]
        if predicted == actual:
            success += 1
        else:
            fail +=1
    return (success / (success + fail)) , (str(fail)+'/'+str(fail + success))

# inputs
filename = 'iris_data.txt'
data = read_data(filename)
train , test = train_test_split(data)

# print accuracy calculations
print('***Euclidian***')
print('k = 1' + ' euclidian'+ ' ' + str(accuracy(train, test, 1, 'euclidian')))
print('k = 3' + ' euclidian'+ ' ' + str(accuracy(train, test, 3, 'euclidian')))
print('k = 5' + ' euclidian'+ ' ' + str(accuracy(train, test, 5, 'euclidian')))
print('k = 7' + ' euclidian'+ ' ' + str(accuracy(train, test, 7, 'euclidian')))
print('k = 9' + ' euclidian'+ ' ' + str(accuracy(train, test, 9, 'euclidian')))
print('k = 11' + ' euclidian'+ ' ' + str(accuracy(train, test, 11, 'euclidian')))
print('k = 15' + ' euclidian'+ ' ' + str(accuracy(train, test, 15, 'euclidian')))
print('***Manhattan***')
print('k = 1' + ' manhattan'+ ' ' + str(accuracy(train, test, 1, 'manhattan')))
print('k = 3' + ' manhattan'+ ' ' + str(accuracy(train, test, 3, 'manhattan')))
print('k = 5' + ' manhattan'+ ' ' + str(accuracy(train, test, 5, 'manhattan')))
print('k = 7' + ' manhattan'+ ' ' + str(accuracy(train, test, 7, 'manhattan')))
print('k = 9' + ' manhattan'+ ' ' + str(accuracy(train, test, 9, 'manhattan')))
print('k = 11' + ' manhattan'+ ' ' + str(accuracy(train, test, 11, 'manhattan')))
print('k = 13' + ' manhattan'+ ' ' + str(accuracy(train, test, 15, 'manhattan')))


