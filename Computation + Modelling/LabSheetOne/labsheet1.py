#1
def miles_to_kilometers(miles):
    kilometers = 1.6*miles
    return kilometers

#2
def f(x):
    result = 3*x -2
    return result

def g(x, y):
    result = pow((pow(x,2) + pow(y, 2)), 0.5)
    return result

def h(a, b, c):
    result = (3 * pow(a, 3) * b) - (4*b*c) + (c - a)
    return result


#3
longName = "University of East Anglia"
#a
i = 0
for letter in longName:
    if letter.__contains__("e"):
        print("longName["+str(i)+"] : " + longName[i])
        break
    i = i + 1

#b
for k in range(0, len(longName), 1):
        if longName[k:].__eq__("East Anglia"):
            print("longName["+str(k)+"]: " + longName[k:])
            break

#c
for k in range(0, len(longName), 1):
    for l in range(0, len(longName), 1):
        if longName[k:l].__eq__("East"):
            print("longName["+str(k)+":"+str(l)+"]: " + longName[k:l])
            break
#d
for word in longName.split():
    if word.__eq__("University"):
        print(str(longName.split().index(word)))
        
#e
print(longName[0:len(longName):2]) # prints every other letter

#f 
print(longName[-5]) #starts from the end

#4
#a
def remove_first(n,s):
    shortened = s[n:]
    return shortened

#b
def remove_letter(i, s):
    s = str(s)
    removed = s[:i] +s[i+1:]
    return removed

#5
print(("University of East Anglia" > "University of Cambridge"))
#this just compares the strings alphabetically - c appearing before e in the
#alphabet thus uea is listed later and is greater

#6
#a
def longer(s,n):
    if len(s) > len(n):
        return True
    else:
        return False

#b
def startfin(s):
    if s[0].__eq__(s[len(s)]):
        return True
    else:
        return False
    
    
#c
def within(a, b, d):
    dist = abs(a-b)
    if dist < d:
        return True
    else:
        return False

#7
#a , b - it is better to store cost in pence, c 


class greengrocer:
    __apples = 0.34
    __bananas = 0.25
    __cherries = 0.06
    __mushrooms = 0.1
    __pumpkins = 1.15
    __total = 0.00
    __applesCost = 0
    __bananasCost = 0
    __cherriesCost = 0
    __mushroomsCost = 0
    __pumpkinsCost = 0
    
    def __init__(self, a, b, c, m, p):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__m = m
        self.__p = p
        self.__applesCost = 0.34 * a
        self.__bananasCost = 0.25 * b
        self.__cherriesCost = 0.06 * c
        self.__mushroomsCost = 0.1 * m
        self.__pumpkinsCost = 1.15 * p
        self.__total = self.__applesCost + self.__bananasCost + self.__cherriesCost + self.__mushroomsCost + self.__pumpkinsCost
        self.lst= {
            "apples" : (a, self.__apples),
            "bananas" : (b, self.__bananas),
            "cherries" : (c, self.__cherries),
            "mushrooms" : (m, self.__mushrooms),
            "pumpkins" : (p, self.__pumpkins)
              }
        
    
    def total(self):
        return self.__total
    
    def recipt(self):
        __rec = str()
        for  (x,y) in self.lst.values():
            
            for i in range(0, len(self.lst), 1):
                print(self.lst.items()[i])
                __rec = __rec + "You bought "+ str(x) +" "+ str(self.lst[i]) +", at a cost of " + str(y)+"\n"
        
        __rec = __rec + "\nThe total price is £" + str(self.total())
        loyalty = self.total()
        points = 0
        while(loyalty > 1):
            points = points + 1
            loyalty = loyalty -1
        __rec = __rec + "\n\nYou have earned " + str(points) + " loyalty points"
        return __rec
        
        









#Formative
def q(x):
    res = 7 - x**2
    return res