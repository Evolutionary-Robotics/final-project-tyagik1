import numpy as np
import matplotlib.pyplot as plt

class EvolutionaryAlgorithm():
    def __init__(self, ff, gs, b, mp, rp, g, p):
        self.ff = ff # Fitness Function
        self.gs = gs # Gene Size
        self.b = b # List of barrier values for each gene
        self.mp = mp # Mutation Probability determines mutation size
        self.rp = rp # Recombination Probability
        self.g = g # Generations
        self.p = p # Population
        self.i = np.zeros((self.p, self.gs))
        for i in range(self.p):
            for j in range(self.gs):
                self.i[i][j] = np.random.rand() * (self.b[j][1] - self.b[j][0]) # Creates individual [-1, 1]
        self.fHistory = np.zeros(self.g) # Fitness History
        self.t = self.g*self.p
        self.gene = self.i[0]

    def run(self):
        for i in range(self.g):
            bestF = -1e9
            for j in range(self.t):
                print(f"Running Gen {i + 1}/{self.g} Tournament {j + 1}/{self.t}")
                a = np.random.randint(0, self.p)
                b = np.random.randint(0, self.p)
                while a == b:
                    b = np.random.randint(0, self.p)
                fA = self.ff(self.i[a])
                fB = self.ff(self.i[b])
                winner = a
                loser = b
                if fA < fB:
                    winner = b
                    loser = a
                if self.ff(self.i[winner]) >= bestF:
                    bestF = self.ff(self.i[winner])
                    self.gene = self.i[winner]
                for k in range(self.gs):
                    if np.random.random() < self.rp:
                        self.i[loser][k] = self.i[winner][k]
                for k in range(self.gs):
                    self.i[loser][k] += np.random.normal(self.mp*(-1*(self.b[k][1] - self.b[k][0]))/5, self.mp*(self.b[k][1] - self.b[k][0]), size = 1)
                    self.i[loser][k] = np.clip(self.i[loser][k], self.b[k][0], self.b[k][1])
            self.fHistory[i] = bestF
            np.save(f"gene{i+1}.npy", self.gene) # only use to use generational data
        print(f"Fitness Acheived: {self.fHistory[-1]}")

        plt.plot(self.fHistory)
        plt.xlabel("Generations")
        plt.ylabel("Fitness")
        plt.title(f"Evolution with Population = {self.p}, Mutation Probability = {self.mp}, Recombination Probability = {self.rp}")
        plt.show()

        # np.save(f"gene.npy", self.gene) # use for normal run