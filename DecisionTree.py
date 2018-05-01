'''
Started on Apr 7, 2018

@author: Xavier Humberg & Nathan Rogers
'''

import csv
import os

from sklearn import tree
from sklearn.linear_model import perceptron

debug = False

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

def GenPerceptronLayer(vals):
	nets = {}
	trainingData = {}
	trainingValues = {}
	for i in range (0, 36):
		indx = i+1
		data = [0]*12;
		for j in range(0, 11):
			data[j] = float(vals[indx][j])
		for j in [13, 15, 17]:
			if vals[indx][j] not in trainingData:
				trainingData[vals[indx][j]] = []
				trainingValues[vals[indx][j]] = []
			trainingData[vals[indx][j]].append(data);
			if vals[indx][j+1] is "1":
				trainingValues[vals[indx][j]].append(1);
			else:
				trainingValues[vals[indx][j]].append(0);
	for string in trainingData:
		if 1 not in trainingValues[string] or 0 not in trainingValues[string]:
			print "-E- Only one label exists for " + string + ": " + str(trainingValues[string]);
			continue
		nets[str(string)] = perceptron.Perceptron(max_iter=100, tol=None, verbose=0, random_state=None, fit_intercept=True, eta0=0.002)
		nets[str(string)].fit(trainingData[string], trainingValues[string]);
		if debug is True:
			print string + ": " + str(nets[string].score(trainingData[string], trainingValues[string])*100) + "% testing accuracy"
	return nets;

def perceptronPredict(aggressiveTree, middleTree, passiveTree, perceptrons, testArray):
	prediction1 = str(aggressiveTree.predict(testArray)[0]);
	prediction2 = str(middleTree.predict(testArray)[0]);
	prediction3 = str(passiveTree.predict(testArray)[0]);
	net = perceptrons[prediction1]
	if debug is True:
		print "Aggressively predicted: " + prediction1 + ". Perceptron says : " + str(perceptrons[prediction1].predict(testArray)[0]);
		print "Progressively predicted: " + prediction2 + ". Perceptron says : " + str(perceptrons[prediction2].predict(testArray)[0]);
		print "Defensively predicted: " + prediction3 + ". Perceptron says : " + str(perceptrons[prediction3].predict(testArray)[0]);

	result = prediction3
	if str(perceptrons[prediction1].predict(testArray)[0]) is "1":
		result = prediction1
	elif str(perceptrons[prediction2].predict(testArray)[0]) is "1":
		result = prediction2
	return result

##change current working directory, needed for my computer
#os.chdir(r'F:\school\Nate\cs5350\project\PFAutoChar')
values = loadInputs("percepTrain.csv")
#print(values[4][13])
aggressiveTree = DecisionTree(values, 1)
middleTree = DecisionTree(values, 2)
passiveTree = DecisionTree(values, 3)

#Create the perceptron nets
perceptrons = GenPerceptronLayer(values);

result = perceptronPredict(aggressiveTree, middleTree, passiveTree, perceptrons, [[3,0,0,1,1,1,2,1,2,0.18,0.57,3]]);

print "You should " + result

##code testing

#prediction1 = aggressiveTree.predict([[5, 11, 11, -1, 1, 4, 4, -1, 6, 1, 0.68, 19]])
#print(prediction1)
#prediction2 = middleTree.predict([[5, 11, 11, -1, 1, 4, 4, -1, 6, 1, 0.68, 19]])
#print(prediction2)
#prediction3 = passiveTree.predict([[5, 11, 11, -1, 1, 4, 4, -1, 6, 1, 0.68, 19]])
#print(prediction3)

#testvals = loadInputs("test.csv")
#print(aggressiveTree.predict(testvals))
#print(middleTree.predict(testvals))
#print(passiveTree.predict(testvals))
