def dot_product(input1, input2):
    arr = []
    for x,y in zip(input1,input2):
        arr.append(x*y)
    dot = 0
    for e in arr:
        dot+= e
    return float(dot)
