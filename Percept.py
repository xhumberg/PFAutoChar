'''
Started on Apr 7, 2018

@author: Xavier Humberg & Nathan Rogers
'''

import csv

##Perceptron layer

def loadInputs(fname):
    values = []
    with open(fname, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            values.append(row)
    return values;













values = loadInputs("train.csv");