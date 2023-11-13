import numpy as np

class NeuralNetwork:
    def __init__ (self, learning_rate):
        self.weights = np.array([np.random.randn(), np.random.randn()])
        self.bais = np.random.randn()
        self.learning_rate = learning_rate

    def sigmoid(self, x):
        return 1/ (1+np.exp(-x))

    def sigmoid_deriv(self ,x):
        return self.sigmoid(x) *(1-self.sigmoid(x))

    def predict(self, input_v):
        layer1 = np.dot(input_v, self.weights) + self.bais
        layer2 = self.sigmoid(layer1)
        prediction = layer2
        return prediction
    
    def compute_gradient(self, input_vector, target):
        layer1 = np.dot(input_vector, self.weights) + self.bais
        layer2 = self.sigmoid(layer1)
        prediction = layer2

        derror = 2 * (prediction - target) # derivitave of the error to prediction
        dprediction = self.sigmoid_deriv(layer1)
        dlayer1 = 1
        dlayer1_w = (0*self.weights) +(1*input_vector)

        derror_dbais = (
            derror * dprediction * dlayer1
        )

        derror_dweights = (
            derror * dprediction * dlayer1_w
        )

        return derror_dbais, derror_dweights
    
    def update_param(self, derror_dbais, derror_dweights):
        self.bais = self.bais - (derror_dbais * self.learning_rate)
        self.weights = self.weights - (derror_dweights * self.learning_rate)

    def train(self, input_vectors, targets, iterations):
        cumulative_errors = []
        for current_it in range(iterations):
            random_data_i = np.random.randint(len(input_vectors))

            input_vector = input_vectors[random_data_i]
            target = targets[random_data_i]

            derror_dbais, derror_dweights = self.compute_gradient(input_vector,target)

            self.update_param(derror_dbais, derror_dweights)
            
            if current_it % 100 == 0:
                cumulative_error = 0
                for data_instance_index in range(len(input_vectors)):
                    data_point = input_vectors[data_instance_index]
                    target = targets[data_instance_index]

                    prediction = self.predict(data_point)
                    error = np.square(prediction - target)

                    cumulative_error = cumulative_error + error
                cumulative_errors.append(cumulative_error)

        return cumulative_errors
