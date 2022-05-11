import numpy as np
import matplotlib.pyplot as plt

File_data = np.loadtxt("train.txt", dtype=int)

first = []

for x in File_data:
    if x[0] == 1:
        add = np.delete(x, 0)
        first.append(add)

first  = np.asarray(first)

loopleft = first[:,0]
Setting1 = first[:,1]
Setting2 = first[:,2]
Setting3 = first[:,3]
sens1 = first[:,4]
sens2 = first[:,5]
sens3 = first[:,6]
sens4 = first[:,7]
sens5 = first[:,8]
sens6 = first[:,9]
sens7 = first[:,10]
sens8 = first[:,11]
sens9 = first[:,12]
sens10 = first[:,13]

sens11 = first[:,14]
sens12 = first[:,15]
sens13 = first[:,16]
sens14 = first[:,17]
sens15 = first[:,18]
sens16 = first[:,19]
sens17 = first[:,20]
sens18 = first[:,21]
sens19 = first[:,22]
sens20 = first[:,23]

sens21 = first[:,24]




plt.title("Sensor Data")
plt.xlabel("Revolution")
plt.ylabel("Sensor")
plt.plot(loopleft, sens1, color = "red", marker = "o", label = "Sensor1")
plt.plot(loopleft, sens2, color = "green", marker = "x", label = "Sensor2")
plt.plot(loopleft, sens3, color = "blue", marker = "X", label = "Sensor3")
plt.plot(loopleft, sens4, color = "yellow", marker = "X", label = "Sensor4")
plt.plot(loopleft, sens5, color = "purple", marker = "X", label = "Sensor5")
plt.plot(loopleft, sens6, color = "gray", marker = "X", label = "Sensor6")
plt.plot(loopleft, sens7, color = "brown", marker = "X", label = "Sensor7")
plt.plot(loopleft, sens8, color = "orange", marker = "X", label = "Sensor8")
plt.plot(loopleft, sens9, color = "pink", marker = "X", label = "Sensor9")
plt.plot(loopleft, sens10, color = "violet", marker = "X", label = "Sensor10")

plt.plot(loopleft, sens11, color = "red", marker = "o", label = "Sensor11")
plt.plot(loopleft, sens12, color = "green", marker = "x", label = "Sensor12")
plt.plot(loopleft, sens13, color = "blue", marker = "X", label = "Sensor13")
plt.plot(loopleft, sens14, color = "yellow", marker = "X", label = "Sensor14")
plt.plot(loopleft, sens15, color = "purple", marker = "X", label = "Sensor15")
plt.plot(loopleft, sens16, color = "gray", marker = "X", label = "Sensor16")
plt.plot(loopleft, sens17, color = "brown", marker = "X", label = "Sensor17")
plt.plot(loopleft, sens18, color = "orange", marker = "X", label = "Sensor18")
plt.plot(loopleft, sens19, color = "pink", marker = "X", label = "Sensor19")
plt.plot(loopleft, sens20, color = "violet", marker = "X", label = "Sensor20")

plt.plot(loopleft, sens21, color = "violet", marker = "X", label = "Sensor21")
plt.legend()
plt.show()

