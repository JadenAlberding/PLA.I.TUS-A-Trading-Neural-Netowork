
def write1ToFile(w, file):
    x = open(str(file), 'a')
    x.write(str(w))
    x.write("\n")
    x.close()

def write2ToFile( w , y , file):

    # Writes to inputs to a file separated by a comma
    
    x = open(str(file), 'a')
    x.write(str(w))
    x.write(",")
    x.write(str(y))
    x.write("\n")
    x.close()

def resetFile(file):
    x = open(str(file), 'w')
    x.write("")
    x.close()


def main():
    resetFile("Stock_Data.txt")
    write2ToFile(2 , 110, "Stock_Data.txt")
if __name__ == "__main__":
    main()