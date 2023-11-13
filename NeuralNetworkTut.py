import FunctionsNNTut as func


def main():
    input_vector = [1.72,1.23]
    weight_1 = [1.26,0]
    weight_2 = [2.17,0.32]
    inputandW1 = func.dot_product(input_vector,weight_1)
    inputandW2 = func.dot_product(input_vector,weight_2)
    print(inputandW1,inputandW2)


if __name__ == "__main__":
    main()