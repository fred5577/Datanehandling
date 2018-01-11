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
    data1 = np.genfromtxt(filename, delimiter=' ')
    data1 = checkData(data1)
    return data1


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

def askInitInput(data):
    userInput = input("\n  Type the number corresponding to the action you want to perform. \n1. Load data \n2. Filter data \n3. Display statistic \n4. Generate plots \n5. Quit\n")
    if userInput == "1":
        textFileName = input("Input text file's name.\n")
        data = dataLoad(textFileName)
        askInitInput(data)
    elif userInput == "2":
        print("\n  Choose a filter")
        while 1:
            menu = input("1. Filter based on bacteria \n2. Filter based on Growth rate\n")
            if menu == "1":    
                print("\n  Choose a bacteria.")
                while 1:
                    bactName = input("1. Salmonella enterica \n2. Bacillus cereus \n3. Listeria \n4. Brochothrix thermosphacta\n")
                    if bactName == "1":
                        print()
                        askInitInput(data)
                    elif bactName == "2":
                        print()
                        askInitInput(data)
                    elif bactName == "3":
                        print()
                        askInitInput(data)
                    elif bactName == "4":
                        print()
                        askInitInput(data)
                    else:
                        print("Wrong input. Try again")
            elif menu == "2":
                while 1:
                    lower = int(input("Choose lower bound: "))
                    upper = int(input("Choose upper bound: "))
                    if lower < upper:
                        print("frederiks ting") #TODO
                        askInitInput(data)
                    else:
                        print("Lower bound is a bigger number than the upper bound. Try again")
                    
            else:
                print("Wrong input. Try again.")
                        
        askInitInput(data)
    elif userInput == "3":
        print("\n  Choose statistic to show.")
        stat = input("1. Mean Temperature \n2. Mean Growth rate \n3. Std Temperature \n4. Std Growth rate \n5. Rows \n6. Mean Cold Growth rate \n7. Mean Hot Growth rate\n")
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
                
        askInitInput(data)
    elif userInput == "4":
        print("")
        askInitInput(data)
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
    
    
    
    

    
    
    
    
   