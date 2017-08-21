import random
import numpy as np

class Network(object):

    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)
                        for x, y in zip(sizes[:-1], sizes[1:])]

    def feedforward(self, a):
        for b, w in zip(self.biases, self.weights):
            a = relu(np.dot(w, a)+b)
        return a

    def SGD(self, training_data, epochs, mini_batch_size,
            test_data=None):
        if test_data: n_test = len(test_data)
        n = len(training_data)
        learning_rates = 0.0001
        ieta = 0
        acc_max = 0.0
        for j in xrange(epochs):
            random.shuffle(training_data)
            mini_batches = [
                training_data[k:k+mini_batch_size]
                for k in xrange(0, n, mini_batch_size)]
            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, learning_rates)
                
            numerator = float(self.evaluate(test_data))
            denominator = float(n_test)
            percentage = float( (numerator * 100.0) / denominator )
            acc_max = max(acc_max, percentage)
            # print "Epoch {0}: {1} %".format(
            #     j, percentage)
        return acc_max

    def update_mini_batch(self, mini_batch, eta):
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        for x, y in mini_batch:
            delta_nabla_b, delta_nabla_w = self.backprop(x, y)
            nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw+dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
        self.weights = [w-(eta/len(mini_batch))*nw
                        for w, nw in zip(self.weights, nabla_w)]
        self.biases = [b-(eta/len(mini_batch))*nb
                       for b, nb in zip(self.biases, nabla_b)]

    def backprop(self, x, y):
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        activation = x
        activations = [x]
        zs = []
        for b, w in zip(self.biases, self.weights):
            z = np.dot(w, activation)+b
            zs.append(z)
            activation = relu(z)
            activations.append(activation)
        delta = self.cost_derivative(activations[-1], y) * \
            relu_prime(zs[-1])
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())
        for l in xrange(2, self.num_layers):
            z = zs[-l]
            sp = relu_prime(z)
            delta = np.dot(self.weights[-l+1].transpose(), delta) * sp
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(delta, activations[-l-1].transpose())
        return (nabla_b, nabla_w)

    def leader_print(self, leaderboard_data):
    	y = [(np.argmax(self.feedforward(x)))
                        for x in leaderboard_data]
        Fo = open("output.txt", "w")
        for i in y:
        	Fo.write(str(i))
        Fo.close()

    def evaluate(self, test_data):
        test_results = [(np.argmax(self.feedforward(x)), y)
                        for (x, y) in test_data]
        ans = []
        for (x, y) in test_results:
        	if y[x] == 1:
        		ans.append(1)
        	else:
        		ans.append(0)
        return sum(ans)

    def cost_derivative(self, output_activations, y):
        return (output_activations-y)

def relu(z):
    nz = z
    for i in xrange(len(z)):
        nz[i] = max(0.01*z[i], z[i])
    return nz

def relu_prime(z):
    dz = z
    for i in xrange(len(z)):
        if z[i] <= 0:
            dz[i] = 0.01
        else:
            dz[i] = 1
    return dz

def sigmoid(z):
    return 1.0/(1.0+np.exp(-z))

def sigmoid_prime(z):
    return sigmoid(z)*(1-sigmoid(z))