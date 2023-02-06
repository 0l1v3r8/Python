import numpy as np

#1
numbers1 = np.linspace(3,3.5,6)
numbers2 = np.arange(3, 3.51, 0.1)
xs = [0,1,2,3,4,5]
xa = np.array(xs)
xa = np.add((np.divide(xa,10)),3) #I dont know what "pointwise arythemtic" is

import matplotlib.pyplot as plt 

#2
x = np.linspace(0,8,10000)
x = x[1:]
y = (np.cos(pow(x,2)))/x
#plot1 = plt.plot(x, y)


#3
n = np.linspace(1, 10, 10)
ones = np.linspace(1,1,10)
funcn = (1 - 1/n)
plt.scatter(n,funcn,marker ="x")
plt.xlabel("n")
plt.ylabel("1 - 1/n")
plt.plot(n, ones, linestyle='dashed', color = 'green')
plt.show()

#4
def countMatrix(n, m):
    numbers = np.arange(1, (n * m) +1 , 1)
    return numbers.reshape(n,m)

def countmatrix(n,m):
    matrix = []
    for i in range(n):
        numbers = np.arange(1*(1+i*m),(1+i)*m +1)
        matrix.append(numbers)
    print(np.array(matrix))
        


#5
adj = np.array([[0,0,1,0,0,0],
                [0,0,1,1,0,0],
                [0,0,0,0,1,0],
                [0,0,0,0,0,1],
                [0,0,0,0,0,2],
                [0,1,0,0,0,0]])

identity = np.array([[1,0,0,0,0,0],
                     [0,1,0,0,0,0],
                     [0,0,1,0,0,0],
                     [0,0,0,1,0,0],
                     [0,0,0,0,1,0],
                     [0,0,0,0,0,1]])

for i in range(50):
    if i ==0:
        result = adj @ identity
    else:
        result = result @ adj
    
    
    

print(result)