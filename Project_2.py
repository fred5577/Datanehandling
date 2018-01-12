import numpy as np
import pandas as pd


def roundGrade(grades):
    sevenStep = np.array([-3, 0, 2, 4, 7, 10, 12])
    gradesRounded = []
    for grade in grades:
        gradesRounded.append(min(sevenStep, key=lambda x: abs(x-grade)))
    return gradesRounded

#NxM, n students and m assignments
def computeFinalGrades(grades):
    (x,y) = np.shape(grades)
    gradesFinal = np.array([])

    if x == 1:
        return np.append(grades, [])

    for i in range(y):
        temp = grades[:, i]
        if np.amin(temp) == -3:
            gradesFinal = np.append(gradesFinal, -3)
        else :
            tempMin = np.argmin(temp)
            tempArray = np.delete(temp, tempMin)
            tempM = tempArray.mean()
            gradesFinal = np.append(gradesFinal, tempM)

    return roundGrade(gradesFinal)


def checkDataErrors(data):
    studieIDS = data['StudieID'].values
    

def dataLoad():
    while True:
        filename = input("Enter name of CSV-file")
        try:
            data = pd.read_csv(filename, quotechar='"')
            break
        except FileNotFoundError:
            print("Can't find the fucking file you moron")
            pass
    return data


# INPUTNUMBER Prompts user to input a number
#
# Usage: num = inputNumber(prompt) Displays prompt and asks user to input a
# number. Repeats until user inputs a valid number.
#
# Author: Mikkel N. Schmidt, mnsc@dtu.dk, 2015
def inputNumber(prompt):
    while True:
        try:
            num = float(input(prompt))
            break
        except ValueError:
            pass
    return num


# DISPLAYMENU Displays a menu of options, ask the user to choose an item
# and returns the number of the menu item chosen.
#
# Usage: choice = displayMenu(options)
#
# Input options Menu options (array of strings)
# Output choice Chosen option (integer)
#
# Author: Mikkel N. Schmidt, mnsc@dtu.dk, 2015
def displayMenu(options):
    # Display menu options
    for i in range(len(options)):
        print("{:d}. {:s}".format(i+1, options[i]))
    # Get a valid menu choice
    choice = 0
    while not(np.any(choice == np.arange(len(options))+1)):
        choice = inputNumber("Please choose a menu item: ")

    return choice

def startProgram():
    # INITIAL FILE LOAD IN:
    data = dataLoad()
    #printDescription(data)

    # Define menu items
    menuItems = np.array(["Load new data", "Check for data errors",
                          "Generate plots", "Display list of grades", "Quit"])
    # Start
    while True:
        # Display menu options and ask user to choose a menu item
        choice = displayMenu(menuItems)
        # Menu item chosen
        # ------------------------------------------------------------------
        # 1. Enter name
        if choice == 1:
            # Load new data
            data = dataLoad()
        # ------------------------------------------------------------------
        # 2. Check for data errors
        elif choice == 2:
            checkDataErrors(data)
            print("bla")
        # ------------------------------------------------------------------
        # 3. Generate plots
        elif choice == 3:
            #gradesPlot(data)
            print("meh")
        # ------------------------------------------------------------------
        # 4. Display list of grades
        elif choice == 4:
            #displayGrades(data)
            print("diller")
        # ------------------------------------------------------------------
        # 5. Quit
        elif choice == 5:
            # End
            break

if __name__ == "__main__":

    print("\n Greetings!")
    startProgram()

