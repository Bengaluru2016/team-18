import math
import random

centroids = []
class ClusterCenters(object):

    def __init__(self, data, k):
        """
        data is an iterable of tuples.
        """
        self.found = 0
        self.k = k
        self.data = data
        dim = self.dim = len(self.data[0])
        maxi = lambda i: max(x[i] for x in self.data)
        mini = lambda i: min(x[i] for x in self.data)

        self.guesses = []
        for guessi in range(k):
            guess = []

            for i in range(dim):
                guess.append(random.triangular(mini(i), maxi(i)))

            self.guesses.append(guess)

        self.initial_convert_and_sort()

    def initial_convert_and_sort(self):

        self.data = self.get_data(self.data)
        self.unpack_new_centers()

    def get_data(self, points):
        new_data = []

        for point in points:
            distances = []
            for guess in self.guesses:
                distance = math.sqrt(
                    sum((point[i] - guess[i])**2 for i in range(self.dim))
                )
                distances.append(distance)

            ki = distances.index(min(distances))

            d = {
                "ki": ki,
                "point": point
            }
            new_data.append(d)

        return new_data

    def unpack_new_centers(self):
        for ki, guess in enumerate(self.guesses):

            points = [d["point"] for d in self.data if d["ki"] == ki]
            new_guess = []

            if points:
                for i in range(self.dim):
                    iguess = sum(point[i] for point in points) / len(points)
                    new_guess.insert(i, iguess)

                self.guesses[ki] = new_guess
            else:
                mini = lambda i: min(d["point"][i] for d in self.data)
                maxi = lambda i: max(d["point"][i] for d in self.data)
                self.guesses[ki] = [random.triangular(mini(i), maxi(i)) for i in range(self.dim)]
                
        self.correspond_nearest()

    def correspond_nearest(self):

        points = [d["point"] for d in self.data]
        new_data = self.get_data(points)

        if new_data == self.data:
            self.found += 1
            if self.found > 10:
                global centroids
                centroids = self.guesses
            else:
                self.unpack_new_centers()
        else:
            self.data = new_data
            self.unpack_new_centers()


def findClosestCluster(data,centroids,dataDimension,nCluster):
    min_distance = 100000000
    index = -1
    for i in range (0,nCluster):
        distance = math.sqrt(sum((data[x] - centroids[i][x])**2 for x in range(0,dataDimension)))
        if distance < min_distance:
            min_distance = distance
            index = i
    return index

'''
0th dimension -> Type of social cause (0-education, 1-women welfare, 2-wildlife welfare, etc etc)
1st dimension -> No. of people involved in social cause
2nd dimension -> Total money invested
3rd dimension -> Credit score of the borrower(1-10)
etc etc. Add features
'''

if __name__ == "__main__":
    nCluster = 3
    dataSet = ((0,5,400,7), (1,11,0,9), (0, 2, 500,1), (1,22,100,4), (2, 5,50,2), (2,15,150,5), (1,100,100,4), (2,80,600,10), (1,60,500,5))
    dataDimension = len(dataSet[0])
    cc = ClusterCenters(dataSet, nCluster)
    clusters = [[] for i in range (0,nCluster)]
    for data in dataSet:
        i = findClosestCluster(data, centroids,dataDimension, nCluster)
        clusters[i].append(data)
    for i in range(0,len(clusters)):
        print "Data points in cluster",i," ",clusters[i]
