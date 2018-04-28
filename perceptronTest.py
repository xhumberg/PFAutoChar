from sklearn.linear_model import perceptron

d = [[3, 3], [1, -1], [1, -3], [-1, 1], [-3, 1], [-2,-1], [-1, -3], [-3,-3]];

t = [0, 0, 0, 0, 0, 1, 1, 1]

net = perceptron.Perceptron(n_iter=100, verbose=0, random_state=None, fit_intercept=True, eta0=0.002)
net.fit(d, t);

print "Accuracy   " + str(net.score(d, t)*100) + "%"
