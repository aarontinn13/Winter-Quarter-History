import math

#formula for the euclidean distance
def euclidean_distance(p,q):
    return math.sqrt(((p[0]-q[0])**2)+((p[1]-q[1])**2)+((p[2]-q[2])**2))

#copying distances from file
list_of_distances = [20.900,15.300,20.400],[0.600,34.700,8.100],[12.100,15.800,2.300],[15.000,5.800,16.900]
list_of_origin_distance = [0,0,0]
minimum_list = []
minimum_list2 = []

#computing the distances from the origin
for i,j in enumerate(list_of_distances):
    print('The distance between point {} and the origin is {}'.format(i+1, euclidean_distance(j,list_of_origin_distance)))
    #finding minimum distance and appending to another list
    minimum_list.append(euclidean_distance(j,list_of_origin_distance))

print
print 'The minimum distance to origin is: ',min(minimum_list) # The minimum is 20.033471990646056
print

#computing distances between all points
for x in list_of_distances:
    for y,z in enumerate(list_of_distances):
        if list_of_distances.index(z) <= list_of_distances.index(x):
            continue
        else:
            print('The distance between point {} and point {} is: {}'.format(list_of_distances.index(x)+1,list_of_distances.index(z)+1, euclidean_distance(x,z)))
            minimum_list2.append(euclidean_distance(x,z))

print
print 'The minimum distance between the points are points 1 and 4: ', min(minimum_list2)  #The minimum is point 1 and 4:  11.717934971657762
print
