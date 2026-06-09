import random

class Layer:
    def __init__(self,n_in,n_out):
        self.W = []
        for i in range(n_out):
            row = []
            for k in range(n_in):
                row.append((random.random()*2-1)*(1/(n_out**0.5)))
            self.W.append(row)
        self.b = [0]*n_out
    def forwardpass(self,x):
        output = []
        #dot product of x and W
        for neuron in range (len(self.W)):
            outsum = 0
            for weight in range(len(self.W[neuron])):
                out = self.W[neuron][weight]*x[weight]
                outsum+=(out+self.b[weight])
            if outsum>0:

                output.append(outsum)
            else:
                output.append(0)
        return output


class NeuralNetwork:
    def __init__(self):
        self.layers = []
    def add_layers(self,n_in,n_out):
                pass