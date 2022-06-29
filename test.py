import numpy as np
import matplotlib.pyplot as plt

File_data = np.loadtxt("train.txt", dtype=float)

units = int(File_data[-1][0])
for x in range(units):
    section = File_data[File_data[:, 0] == x+1, :]
    XSensors = np.shape(section)[1]
    XDatapoints = np.shape(section)[0]

    for y in range(XSensors-2):
        measurement = section[:,y+2]
        #measurement = measurement/np.linalg.norm(measurement)
        #measurement = (measurement- np.min(measurement)) / (np.max(measurement) - np.min(measurement))# normalizing between 1 and 0
        plt.plot(measurement)  # plotting


    plt.title('Turbine ' + str(x))
    plt.xlabel('Time')
    plt.ylabel('Sensors')
    plt.savefig('pics/' + str(x) + '.png', dpi=2500)
    plt.close()

