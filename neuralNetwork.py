import numpy as np

def tanh(x):
    x = np.clip(x, -50, 50)
    return np.tanh(x)

def inv_tanh(y):
    y = np.clip(y, -0.999999, 0.999999)
    return 0.5 * np.log((1 + y) / (1 - y))

class NeuralNetwork():

    def __init__(self, inputsize, size, outputsize):
        self.Size = size # number of neurons in the network
        self.InputSize = inputsize
        self.OutputSize = outputsize
        self.Voltage = np.zeros(size) # neuron activation vector
        self.TimeConstants = np.ones(size) # time-constant vector
        self.Biases = np.zeros(size) # bias vector
        self.Weights = np.zeros((size,size)) # weight matrix
        self.SensorWeights = np.zeros((inputsize,size)) # neuron output vector
        self.MotorWeights = np.zeros((size,outputsize)) # neuron output vector
        self.Output = np.zeros(size) # neuron output vector
        self.Input = np.zeros(size) # neuron output vector

    def decodeGeneValue(self, val, low, high):
        if low - 1e-12 <= val <= high + 1e-12:
            return float(val)
        span = high - low
        if 0.0 <= val <= span + 1e-12:
            return low + float(val)
        if -1.0 - 1e-12 <= val <= 1.0 + 1e-12:
            return low + ((float(val) + 1.0) / 2.0) * span
        return float(np.clip(val, low, high))

    def setParams(self, gene, b):
        k = 0
        for i in range(self.Size):
            for j in range(self.Size):
                low, high = b[k]
                self.Weights[i, j] = self.decodeGeneValue(gene[k], low, high)
                k += 1
        for i in range(self.InputSize):
            for j in range(self.Size):
                low, high = b[k]
                self.SensorWeights[i, j] = self.decodeGeneValue(gene[k], low, high)
                k += 1
        for i in range(self.Size):
            for j in range(self.OutputSize):
                low, high = b[k]
                self.MotorWeights[i, j] = self.decodeGeneValue(gene[k], low, high)
                k += 1
        for i in range(self.Size):
            low, high = b[k]
            self.Biases[i] = self.decodeGeneValue(gene[k], low, high)
            k += 1
        for i in range(self.Size):
            low, high = b[k]
            self.TimeConstants[i] = self.decodeGeneValue(gene[k], low, high)
            k += 1
        self.invTimeConstants = 1.0 / self.TimeConstants

    def initializeState(self,v):
        self.Voltage = v
        self.Output = tanh(self.Voltage+self.Biases)

    def step(self,dt,i):
        self.Input = np.dot(self.SensorWeights.T, i)
        netinput = self.Input + np.dot(self.Weights.T, self.Output)
        self.Voltage += dt * (self.invTimeConstants*(-self.Voltage+netinput))
        self.Voltage = np.clip(self.Voltage, -50, 50)
        self.Output = tanh(self.Voltage+self.Biases)

    def out(self):
        return tanh(np.dot(self.MotorWeights.T, self.Output))