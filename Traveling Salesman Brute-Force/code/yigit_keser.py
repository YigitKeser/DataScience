"""
Yiğit Keser
311904016
2020.07.10

Calculate all possibilities , choose shortest one
"""
from csv import reader
import itertools
import math
import time

#Data read
def read_data(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	return dataset

#Locate migros index
def find_store(data):
    for number,row in enumerate(data):
        if len(row) == 3:
            break
    return number

#Remove migros from data
def pop_store(data):
    return [i for i,x in enumerate(data) if i != find_store(data)]

#Calculate all possible routes  + add migros location to both start and end
def create_combinations(data):
    storeless = pop_store(data) #removing migros from data
    combinations = list(itertools.combinations(storeless)) #calculating all possible routes
    for i in range(0,len(combinations)):
        combinations[i] = list(combinations[i])
        combinations[i].insert(0,find_store(data)) #inserting migros location as first location
        combinations[i].append(find_store(data)) #inserting migros location as last location
    print('Kombinasyon sayısı : {}'.format(len(combinations)))
    return combinations

#Calculate distance between 2 points
def calculate_distance(a,b):
    a = list(map(float,a))
    b = list(map(float,b))
    return math.sqrt(abs(((a[0]-b[0])**2 - (a[1]-b[1])**2)))

#Calculate distances for all possible routes and return shortest
def calculate_route_distances(data,combinations):
    distances =[]
    distance = 0.0
    for i in range(0,len(combinations)):
        for j in range(0,len(combinations[i])-1):
            distance += calculate_distance(data[combinations[i][j]][0:2] , data[combinations[i][j+1]][0:2])
        distances.append(distance)
        distance = 0.0
        #print("Route {} : {}\nToplam Yol : {}".format(i+1,combinations[i]+1,distances[i]))
    return print('En kısa route numarası : Route {}\nKullanılan route : {}\nToplam Yol : {}'.format(distances.index(min(distances))+1,combinations[distances.index(min(distances))],min(distances)))

def run():
    for i in range(1,4):
        print('***data{}***: '.format(i))
        data = read_data('data'+str(i)+'.txt')    
        combinations = create_combinations(data)
        calculate_route_distances(data,combinations)
        
start = time.time()
run()
end = time.time()
minutes = (end - start) / 60
print("Toplam süre {} dakika ---".format(minutes))









