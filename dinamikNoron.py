from noronStructure import nouralNetwork
import numpy as np

agırliklar =[]
inputset=np.array([[1,1,0,0],[0,0,0,1],[0,0,0,1]])
outputset=np.array([[0,1],[1,1],[0,0]])
mynoron = nouralNetwork(inputset,outputset,5,3,4,1,2,5,2)
np.random.seed(1)
print(mynoron.noronYapisi());
agırliklar =mynoron.agirlikBelirle()
print(agırliklar[0])
print("\n")
print(agırliklar[1])
print("\n")
print(agırliklar[2])
print("\n")
print(mynoron.islemekoy());







