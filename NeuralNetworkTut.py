import NN 
import numpy as np
import matplotlib.pyplot as plt


def main():
    i_vectors = np.array([[3, 1.5],[2, 1],[4, 1.5],[3, 4],[3.5, 0.5],[2, 0.5],[5.5, 1],[1, 1],])

    targets = np.array([0, 1, 0, 1, 0, 1, 1, 0])

    learning_rate = 0.01

    neural_network = NN.NeuralNetwork(learning_rate)

    training_error = neural_network.train(i_vectors, targets, 100000)

    plt.plot(training_error)
    plt.xlabel("Iterations")
    plt.ylabel("Error for all training instances")
    plt.savefig("cumulative_error.png")


if __name__ == "__main__":
    main()