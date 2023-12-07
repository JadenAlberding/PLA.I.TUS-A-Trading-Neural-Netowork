
import re

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


def combine2File(f1,f2):
    try:
        file1 = open(str(f1), 'r')
        file2 = open(str(f2), 'r')
    except:
        print("Invalid File")
        return
    comb = []
    for (i,j) in zip(file2,file1):
        temp = []

        i = i.replace("\n", "")
        i = i.replace("[", "")
        i = i.replace("]", "")


        j = j.replace("\n","")
        j+= ","
        j += i 

        j = j.split(",")
        for i in j:
            temp.append(float(i))
      
        comb.append(temp)

    return comb


def main():
    resetFile("Stock_Data.txt")
    write2ToFile(2 , 110, "Stock_Data.txt")
if __name__ == "__main__":
    main()