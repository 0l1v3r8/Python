#1
def xs():
    lst = []
    for i in range(0,101,1):
        lst.append(i/100)
    return lst

def ys():
    lst = []
    for i in xs():
        lst.append(3*pow(i,2) + 4)
    return lst

#2
list1 = [73, 128525, 85, 69, 65]
list2 = [70, 105, 114, 115, 116, 44, 32, 115, 111, 108, 118, 101, 32, 116, 104, 101, 32, 112, 114, 111, 98, 108, 101, 109, 46, 32, 84, 104, 101, 110, 44, 32, 119, 114, 105, 116, 101, 32, 116, 104, 101, 32, 99, 111, 100, 101, 46]

def decode1():
    word = ""
    for i in list1:
        word = word + (chr(i))
    return word

def decode2():
    word = ""
    for i in list2:
        word = word + (chr(i))
    return word

words = "Hello, this is a message to whoever decodes this."

def encode(words):
    code = []
    for letter in words:
        code.append(ord(letter))
    return code

#3
def FizzBuzz(n):
    for i in range (1, n +1, 1):
        if ((i%3) == 0) and ((i%5) == 0):
            print("FizzBuzz")
        elif ((i%3) == 0):
            print("Fizz")
        elif ((i%5) == 0):
            print("Buzz")
        else:
            print(str(i))

#4
ns  = [4,1,5,2]
def barh(ns):
    for item in ns:
        bar = ""
        for i in range(0, item, 1):
            bar = bar + "*"
        print(bar)
        bar = ""

def  barv(ns):
    largest = 0
    for item in ns:
        if (item > largest):
            largest = item;
    line = ""
    for i in range (largest, 0, -1):
        for j in ns:
            if (j >= i):
                line = line + "*"
            else:
                line = line + " "
        print(line)
        line = ""

#5
def book3():
    fileread = open("mybook.txt")
    filewrite = open("mybook3.txt", "w")
    for line in fileread:
        line = line.replace("e", "3")
        filewrite.writelines(line)      
    fileread.close()
    filewrite.close()

#formative
def formative():
    lst = []
    for i in range(20, 41, 1):
        lst.append((5*(i/10)) + pow((i/10),2))
    return lst
            