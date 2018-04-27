'''
Started on Apr 7, 2018

@author: Xavier Humberg & Nathan Rogers
'''

import csv
import os

from sklearn import tree

def loadInputs(fname):
    retvalues = []
    with open(fname, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            retvalues.append(row)
    return retvalues

## makes a decision tree based on the given values (retrieved from our csv file)
## trains the tree based on given treeNum value
#### 1 = aggressive tree; 2 = middle tree; 3 = passive tree
def DecisionTree(vals, treeNum):
    ##testing purposes
    #print(vals[2][13])

    retval = tree.DecisionTreeClassifier()
    parameters = [[0 for i in range(12)] for j in range(36)]
    labels = [0 for i in range(36)]

    num = 0
    if treeNum == 1:
        num = 13
    if treeNum == 2:
        num = 15
    if treeNum == 3:
        num = 17

    for i in range(0, 36):
        indx = i+1
        #print(indx)
        #print(num)
        labels[i] = vals[indx][num]
        for j in range(0, 11):
            parameters[i][j] = vals[indx][j]
    retval = retval.fit(parameters, labels)
    return retval

##change current working directory, needed for my computer
#os.chdir(r'F:\school\Nate\cs5350\project\PFAutoChar')
values = loadInputs("percepTrain.csv")
#print(values[4][13])
aggressiveTree = DecisionTree(values, 1)
middleTree = DecisionTree(values, 2)
passiveTree = DecisionTree(values, 3)

##code testing

#prediction1 = aggressiveTree.predict([[3, 0, 0, -1, 1, 1, 1, 1, 12, 1, 1, 0]])
#print(prediction1)
#prediction2 = middleTree.predict([[3, 0, 0, -1, 1, 1, 1, 1, 12, 1, 1, 0]])
#print(prediction2)
#prediction3 = passiveTree.predict([[3, 0, 0, -1, 1, 1, 1, 1, 12, 1, 1, 0]])
#print(prediction3)