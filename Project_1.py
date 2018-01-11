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
        result = data[:, 0].mean()
    elif statistic == "Mean Hot Growth rate":
        result = data[:, 1].mean()

    return result


def dataPlot(data):
    plt.figure(figsize=(15, 6))
    plt.subplots_adjust(wspace=0.5)
    plt.subplot(1, 2, 1)
    plt.hist(data[:, 2], edgecolor='black')
    plt.title("Amount of each bacteria type")
    plt.xlabel("Bacteria types")
    plt.ylabel("Number of bacteria")

    bacteria1 = data[data[:, 2] == 1]
    bacteria2 = data[data[:, 2] == 2]
    bacteria3 = data[data[:, 2] == 3]
    bacteria4 = data[data[:, 2] == 4]

    plt.subplot(1, 2, 2)
    plt.scatter(bacteria1[:, 0], bacteria1[:, 1], color='blue')
    plt.scatter(bacteria2[:, 0], bacteria2[:, 1], color='green')
    plt.scatter(bacteria3[:, 0], bacteria3[:, 1], color='orange')
    plt.scatter(bacteria4[:, 0], bacteria4[:, 1], color ='red')
    plt.xlim([10, 60])
    plt.ylim(0)
    plt.title("Rate vs. temperature")
    plt.xlabel("Temperature")
    plt.ylabel("Growth Rate")
    plt.show()

if __name__ == "__main__":
    data = dataLoad('bacteria.txt')

    print(dataStatistics(data, "Mean Hot Growth rate"))

    dataPlot(data)
