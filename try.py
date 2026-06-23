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
        self.input = x
        self.output = []
        self.z = []
        #dot product of x and W
        for neuron in range (len(self.W)):
            outsum = 0
            for weight in range(len(self.W[neuron])):
                out = self.W[neuron][weight]*self.input[weight]
                outsum+=(out)
            outsum+=self.b[neuron]
            self.z.append(outsum)
            if outsum>0:
                self.output.append(outsum)
            else:
                self.output.append(0)
        return self.output
    def backwardpass(self,delta):
        self.W_grads = []
        self.b_grads = []
        delta_z = delta[::]
        input_grad = []
        for i in range(len(self.z)):
            if self.z[i]<=0:
                delta_z[i] = 0
        for i in range(len(delta_z)):
            w_grad = []
            self.b_grads.append(delta_z[i])
            for j in range(len(self.input)):
                grad = self.input[j]*delta_z[i]
                w_grad.append(grad)
            self.W_grads.append(w_grad)
        for j in range(len(self.input)):
            total = 0
            for i in range(len(delta_z)):
                total+=(self.W_grads[i][j]*delta_z[i])
            input_grad.append(total)
        return input_grad


class NeuralNetwork:
    def __init__(self):
        self.layers = []
    def add_layers(self,n_in,n_out):
        layer = Layer(n_in,n_out)
        self.layers.append(layer)
    def forward(self,x):
        for layer in self.layers:
            x = layer.forwardpass(x)
        return x