import numpy as np
from matplotlib import pyplot as plt


def checkData(arr):
    res = np.array([])

    rounds = int(np.size(arr) / 3)

    for i in range(rounds):
        fault = False

        if not (10 < arr[i][0] < 60):
            print("Error temperature: " + str(i + 1))
            fault = True
        elif not (arr[i][1] > 0):
            print("Error growth rate: " + str(i + 1))
            fault = True
        elif not (arr[i][2] == 1 or arr[i][2] == 2 or arr[i][2] == 3 or arr[i][2] == 4):
            print("Error bacteria: " + str(i + 1))
            fault = True
        if i == 0:
            res = np.array([np.array([arr[i][0], arr[i][1], arr[i][2]])])
            print(res)
        if not fault and not i == 0:
            res = np.concatenate((res, np.array([np.array([arr[i][0], arr[i][1], arr[i][2]])])), axis=0)

    return res


def dataLoad(filename):
    # Insert your code here
    data1 = np.genfromtxt(filename, delimiter=' ')
    data1 = checkData(data1)
    return data1


def dataStatistics(data, statistic):
    # Insert your code here
    result = []
    if statistic == "Mean Temperature":
        result = data[:, 0].mean()
    elif statistic == "Mean Growth rate":
        result = data[:, 1].mean()
    elif statistic == "Std Temperature":
        result = data[:, 0].std(ddof=1)
    elif statistic == "Std Growth rate":
        result = data[:, 1].std(ddof=1)
    elif statistic == "Rows":
        result = np.size(data) / 3
    elif statistic == "Mean Cold Growth rate":
        result = data[:, 0].mean()
    elif statistic == "Mean Hot Growth rate":
        result = data[:, 1].mean()

    return result


# Purpose of function is to show two plots,
#  one of the amount of each bacteria types, one of the growth and temperature of each bacteria
# It takes as input a 3x3 numpy array of the bacteria data and has no output arguments
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
    bac1 = plt.scatter(bacteria1[:, 0], bacteria1[:, 1], color='blue')
    bac2 = plt.scatter(bacteria2[:, 0], bacteria2[:, 1], color='green')
    bac3 = plt.scatter(bacteria3[:, 0], bacteria3[:, 1], color='orange')
    bac4 = plt.scatter(bacteria4[:, 0], bacteria4[:, 1], color='red')
    plt.legend((bac1, bac2, bac3, bac4), ('Bacteria 1', 'Bacteria 2', 'Bacteria 3', 'Bacteria 4'),
               loc='upper right', bbox_to_anchor=(1.2, 1.0))
    plt.xlim([10, 60])
    plt.ylim([0, 1])
    plt.title("Rate vs. temperature")
    plt.xlabel("Temperature")
    plt.ylabel("Growth Rate")
    plt.show()


def dataFilterBact(data, filterType):
    if filterType == "1":
        data = data[data[:, 2] == 1]
        return data
    elif filterType == "2":
        data = data[data[:, 2] == 2]
        return data
    elif filterType == "3":
        data = data[data[:, 2] == 3]
        return data
    elif filterType == "4":
        data = data[data[:, 2] == 4]
        return data


def dataFilterGrowthRate(data, input1, input2):
    temp = data

    temp = temp[temp[:, 1] > input1]
    temp = temp[temp[:, 1] < input2]

    return temp



#  MENU: Read prints for clarification

def askInitInput(data):

    # --- ASK FOR INITIAL OPTION ----
    userInput = input("\n  Type the number corresponding to the action you want to perform. \n1. Load data \n2. "
                      "Filter data \n3. Display statistic \n4. Generate plots \n5. Quit\n")
    # --- OPTION 1: LOAD DATA ----

    if userInput == "1":
        while 1:
            textFileName = input("Input text file's name.\n")
            try:
                data = dataLoad(textFileName)
                askInitInput(data)
            except ValueError:
                print("Can't find file. Try again.")

    # --- OPTION 2: FILTER DATA
    elif userInput == "2":
        print("\n  Choose a filter")
        while 1:
            menu = input("1. Filter based on bacteria \n2. Filter based on Growth rate\n")
            if menu == "1":
                print("\n  Choose a bacteria.")
                while 1:
                    bactName = input("1. Salmonella enterica \n2. Bacillus cereus \n3. Listeria \n4. Brochothrix "
                                     "thermosphacta\n")
                    if bactName == "1" or bactName == "2" or bactName == "3" or bactName == "4":
                        data = dataFilterBact(data, bactName)
                        askInitInput(data)
                    else:
                        print("Wrong input. Try again")
            elif menu == "2":
                while 1:
                    lower = float(input("Choose lower bound: "))
                    upper = float(input("Choose upper bound: "))
                    if lower < upper:
                        data = dataFilterGrowthRate(data, lower, upper)
                        askInitInput(data)
                    else:
                        print("Lower bound is a bigger number than the upper bound. Try again")

            else:
                print("Wrong input. Try again.")               
    # --- OPTION 3: DISPLAY STATISTIC
    elif userInput == "3":
        print("\n  Choose statistic to show.")
        stat = input("1. Mean Temperature \n2. Mean Growth rate \n3. Std Temperature \n4. Std Growth rate \n5. Rows "
                     "\n6. Mean Cold Growth rate \n7. Mean Hot Growth rate\n")
        while 1:
            if stat == "1":
                print("Mean Temperature: %s" % (dataStatistics(data, "Mean Temperature")))
                askInitInput(data)
            elif stat == "2":
                print("Mean Growth rate: %s" % (dataStatistics(data, "Mean Growth rate")))
                askInitInput(data)
            elif stat == "3":
                print("Std Temperature: %s" % (dataStatistics(data, "Std Temperature")))
                askInitInput(data)
            elif stat == "4":
                print("Std Growth rate: %s" % (dataStatistics(data, "Std Growth rate")))
                askInitInput(data)
            elif stat == "5":
                print("Rows: %s" % (dataStatistics(data, "Rows")))
                askInitInput(data)
            elif stat == "6":
                print("Mean Cold Growth rate: %s" % (dataStatistics(data, "Mean Cold Growth rate")))
                askInitInput(data)
            elif stat == "7":
                print("Mean Hot Growth rate: %s" % (dataStatistics(data, "Mean Hot Growth rate")))
                askInitInput(data)
            else:
                print("Wrong input. Try again.")
         
    # --- OPTION 4: GENERATE PLOTS ---
    elif userInput == "4":
        dataPlot(data)
        askInitInput(data)
    # --- OPTION 5: QUIT ---
    elif userInput == "5":
        quit()
    else:
        print("Wrong input. Try again.")
        askInitInput(data)


if __name__ == "__main__":
    print("\n\n")
    print("Greetings!")
    data = np.array([])
    askInitInput(data)
