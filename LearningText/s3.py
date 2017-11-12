from numpy import *
import operator


def classify(inMat, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    # KNN的算法核心就是欧式距离的计算，一下三行是计算待分类的点和训练集中的任一点的欧式距离
    diffMat = tile(inMat, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    distance = sqDiffMat.sum(axis=1) ** 0.5
    # 接下来是一些统计工作
    sortedDistIndicies = distance.argsort()
    classCount = {}
    for i in range(k):
        labelName = labels[sortedDistIndicies[i]]
        classCount[labelName] = classCount.get(labelName, 0) + 1;
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def file2Mat(testFileName, parammterNumber):
    fr = open(testFileName)
    lines = fr.readlines()
    lineNums = len(lines)
    resultMat = zeros((lineNums, parammterNumber))
    classLabelVector = []
    for i in range(lineNums):
        line = lines[i].strip()
        itemMat = line.split('\t')
        resultMat[i, :] = itemMat[0:parammterNumber]
        classLabelVector.append(itemMat[-1])
    fr.close()
    return resultMat, classLabelVector;


# 为了防止某个属性对结果产生很大的影响，所以有了这个优化，比如:10000,4.5,6.8 10000就对结果基本起了决定作用
def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normMat = zeros(shape(dataSet))
    size = normMat.shape[0]
    normMat = dataSet - tile(minVals, (size, 1))
    normMat = normMat / tile(ranges, (size, 1))
    return normMat, minVals, ranges


def test(trainigSetFileName, testFileName):
    trianingMat, classLabel = file2Mat(trainigSetFileName, 3)
    trianingMat, minVals, ranges = autoNorm(trianingMat)
    testMat, testLabel = file2Mat(testFileName, 3)
    testSize = testMat.shape[0]
    errorCount = 0.0
    for i in range(testSize):
        result = classify((testMat[i] - minVals) / ranges, trianingMat, classLabel, 3)
        if (result != testLabel[i]):
            errorCount += 1.0
    errorRate = errorCount / (float)(len(testLabel))
    return errorRate;


if __name__ == "__main__":
    errorRate = test('datingTrainingSet.txt', 'datingTestSet.txt')
    print("the error rate is :%f" % (errorRate))