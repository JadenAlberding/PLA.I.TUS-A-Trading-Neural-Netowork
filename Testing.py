

def main():
    arr = [1,2,3,4,5]
    print(arr)
    for i in range(len(arr)-1):
        arr[i] = arr[i+1]
    arr[len(arr)-1 ]= 6
    print(arr)

if __name__ == "__main__":
    main()