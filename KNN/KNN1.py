import numpy as np
import operator
def loadDataset(filename, trainingSet=[], posSet=[]):
    with open(filename, "r") as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        dataset = list(lines)
        for i in range(len(dataset)):
            for j in range(len(dataset[i])):
                dataset[i][j] = float(dataset[i][j])
                if dataset[i][-1] == 0:  # 2代表少数类样本的类标，即正类样本
                    posSet.append(dataset[i])
            trainingSet.append(dataset[i])
def euclideanDistance(trainingSet, testInstance):
    distance = []
    instance1 = mat(np.array(trainingSet))
    instance2 = mat(np.array(testInstance))
    dist = instance1[:, :-1] - instance2[:, :-1]
    for i in range(len(dist)):
        distance.append(np.sqrt(np.sum(np.square(dist[i]))))
    return distance
# 返回k个最近邻
def getNeighbors(trainingSet, testInstance, m):
    distances = []
    for i in range(len(trainingSet) - 1):
        dist1 = euclideanDistance(trainingSet[i], testInstance)
        distances.append((trainingSet[i], dist1))
    distances.sort(key=operator.itemgetter(1))
    # 返回k个最近邻
    for x in range(m):
        neighbors.append(distances[x + 1])
    return neighbors