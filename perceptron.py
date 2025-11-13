import numpy as np
import matplotlib.pyplot as plt

class Perceptron():

    def __init__(self, inputs, function):
        self.i = inputs
        self.w = np.random.random(size = inputs)*2 - 1 # Weight 1
        self.b = np.random.random()*2 - 1 # Bias
        self.lr = np.random.random() # Learning Rate
        self.a = function # Activation Function

    def forward(self, X):
        y = np.dot(self.w, X) + self.b
        return self.a(y)

class NeuralNet():
    def __init__(self, inputs, hidden, ouputs, function):
        self.i = inputs
        self.h = hidden
        self.o = ouputs
        self.hls = []
        for i in range(len(self.h)):
            hl = []
            for j in range(self.h[i]):
                if i == 0:
                    hl.append(Perceptron(self.i, function))
                else:
                    hl.append(Perceptron(self.h[i-1], function))
            self.hls.append(hl)
        self.hos = [] # Hidden Outputs
        self.end = [Perceptron(self.h[-1], function) for i in range(self.o)]
        self.output = [0 for i in range(self.o)]
        self.lr = 0.1 # Learning Rate

    def setParams(self, gene):
        i = 0
        for hl in self.hls:
            for neuron in hl:
                w_vals = gene[i: i + neuron.i]
                i += neuron.i
                neuron.w = np.array(w_vals, dtype=float)
                neuron.b = float(gene[i])
                i += 1

        for neuron in self.end:
            w_vals = gene[i: i + neuron.i]
            i += neuron.i
            neuron.w = np.array(w_vals, dtype=float)
            neuron.b = float(gene[i])
            i += 1

    def forward(self, X):
        ho = X
        self.hos = []  # reset hidden outputs
        for hl in self.hls:
            ho = [neuron.forward(ho) for neuron in hl]
            self.hos.append(ho)
        for i in range(len(self.output)):
            self.output[i] = self.end[i].forward(self.hos[-1])
        return self.output