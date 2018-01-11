import numpy as np
from matplotlib import pyplot as plt


def checkData(arr):
    res = np.array([])

    rounds = int(np.size(arr)/3)

    for i in range(rounds):
        fault = False

        if not(10 < arr[i][0] < 60):
            print("Error temperature: " + str(i+1))
            fault = True
        elif not(arr[i][1] > 0):
            print("Error growth rate: "+str(i+1))
            fault = True
        elif not(arr[i][2] == 1 or arr[i][2] == 2 or arr[i][2] == 3 or arr[i][2] == 4):
            print("Error bacteria: "+str(i+1))
            fault = True
        if i == 0:
            res = np.array([np.array([arr[i][0], arr[i][1], arr[i][2]])])
            print(res)
        if not fault and not i == 0:
            res = np.concatenate((res, np.array([np.array([arr[i][0], arr[i][1], arr[i][2]])])), axis=0)

    return res


def dataLoad(filename):
    # Insert your code here
    data = np.genfromtxt(filename, delimiter=' ')
    data = checkData(data)
    return data


def dataStatistics(data, statistic):
    # Insert your code here
    if statistic == "Mean Temperature":
        result = data[:, 0].mean()
    elif statistic == "Mean Growth rate":
        result = data[:, 1].mean()
    elif statistic == "Std Temperature":
        result = data[:, 0].std(ddof=1)
    elif statistic == "Std Growth rate":
        result = data[:, 1].std(ddof=1)
    elif statistic == "Rows":
        result = np.size(data)/3
    elif statistic == "Mean Cold Growth rate":
        result = data[:, 0]
        result = result[result<20].mean()
    elif statistic == "Mean Hot Growth rate":
        result = data[:, 0]
        result = result[result>50].mean()
    return result


def dataPlot(data):
    plt.subplot(1, 4, 1)
    plt.hist(data[:, 2], edgecolor='black')
    plt.xlabel("Number of bacteria")

    plt.subplot(1, 4, 2)

    plt.scatter(data[:, 0], data[:, 1])

    plt.show()

if __name__ == "__main__":
    data = dataLoad('bacteria.txt')

    print(dataStatistics(data, "Mean Hot Growth rate"))

    dataPlot(data)
