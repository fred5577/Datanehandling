import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import random


# Purpose of function is to round a vector of grades, to the nearest on the 7-step-scale
# Input and output is a vector of arbitrary length
# Author: Jacob Pjetursson, s153718, 2018
def roundGrade(grades):
    sevenStep = np.array([-3, 0, 2, 4, 7, 10, 12])
    gradesRounded = []
    for grade in grades:
        gradesRounded.append(min(sevenStep, key=lambda x: abs(x - grade)))
    return gradesRounded


# NxM, n students and m assignments
def computeFinalGrades(grades):
    (x, y) = np.shape(grades)
    gradesFinal = np.array([])

    if x == 1:
        return np.append(grades, [])

    for i in range(y):
        temp = grades[:, i]
        if np.amin(temp) == -3:
            gradesFinal = np.append(gradesFinal, -3)
        else:
            tempMin = np.argmin(temp)
            tempArray = np.delete(temp, tempMin)
            tempM = tempArray.mean()
            gradesFinal = np.append(gradesFinal, tempM)

    return roundGrade(gradesFinal)


def displayData(data):
    namesAndGrades = data.drop(['StudieID'], axis=1)
    print("\nNames and grades for the students assignments")
    namesAndGrades = namesAndGrades.sort_values(by=['Name'])
    namesAndGrades.set_index('Name', inplace=True)
    print(namesAndGrades)
    namesAndGrades = data.drop(['StudieID'], axis=1).values
    namesAndGrades = namesAndGrades[namesAndGrades[:, 0].sort()]
    namesAndGrades = namesAndGrades[0]
    temp = computeFinalGrades(np.transpose(namesAndGrades[:, 2:]))
    out = np.vstack((namesAndGrades[:, 0], temp))

    print("\nThe finale grades for the students assignments")
    printOut = pd.DataFrame(np.transpose(out), columns=['Name', 'Finale grade'])
    printOut.set_index('Name', inplace=True)
    print(printOut)
    print("\n\n")


def gradesPlot(grades):
    final = computeFinalGrades(grades)

    # Setup the figure to contain both plots
    plt.figure(figsize=(15, 6))
    plt.subplots_adjust(wspace=0.5)
    # ------ FIRST PLOT :-------
    plt.subplot(1, 2, 1)

    # Setup a bin containing all kinds of grades
    bins = np.array([-3, 0, 2, 4, 7, 10, 12])

    # Create a dictionary to count grades and convert it to a list
    dict = {-3: 0, 0: 0, 2: 0, 4: 0, 7: 0, 10: 0, 12: 0}
    for i in range(np.size(final)):
        dict[final[i]] += 1
    totals = list(dict.values())

    # Plot the bar for the final grades
    plt.bar(bins, totals)

    # Customize ticks to make the plot prettier
    plt.xticks(bins, ('-3', '00', '02', '4', '7', '10', '12'))
    plt.yticks(np.arange(0, np.max(totals) + 1, 1))

    plt.title("Final grades")
    plt.xlabel("Grades")
    plt.ylabel("Number of students")

    # -----SECOND PLOT :-----
    # Setup for the Scatterplot
    (x, y) = np.shape(grades)
    gradesRandomized = grades.astype(float)
    # Randomize the +/-0.1 for each value in the grades matrix
    for k in range(y):
        for i in range(x):
            gradesRandomized[i][k] = grades[i][k] + ((random.random() * 2 * 0.1) - 0.1)

    plt.subplot(1, 2, 2)
    # Loop through every row of the grades matrix and create a scatterplot for each, with the x value 'i +/-0.1'
    for i in range(x):
        iList = np.zeros(y)
        for k in range(y):
            iList[k] = i + (random.random() * 2 * 0.1) - 0.1
        plt.scatter(iList, gradesRandomized[i, :], label="Assignment %s" % i)

    # Calculate a vector with the mean of each assignment
    avg = np.zeros(x)
    for i in range(x):
        avg[i] = np.mean(grades[i, :])

    # Plot the line of averages
    plt.plot(avg, '-', label="Avg. grade")

    plt.xticks(np.arange(0, x + 1, 1), )

    # Show the two subplots
    plt.legend(loc='upper right', fontsize=8, bbox_to_anchor=(1.2, 1.0))
    plt.title("Grades per assignment")
    plt.xlabel("Assignment")
    plt.ylabel("Grade")
    plt.show()


# Purpose of function is to spot errors in the data, and print an error report.
# Input is an NxM matrix, holding students (studyID, Name) and their grades on a series of assignments
# Function has no output, but shows the error report to the console.
# Author: Jacob Pjetursson, s153718, 2018
def checkDataErrors(data):
    studieIDS = data['StudieID'].values
    grades = data.drop(['StudieID', 'Name'], axis=1).values
    if np.unique(studieIDS).size != len(studieIDS):
        print("Study-ids are not unique! \n")

    seven = [-3, 0, 2, 4, 7, 10, 12]
    for i in range(len(grades)):
        for j in range(len(grades[i])):
            if grades[i][j] not in seven:
                print("%s is not on 7-step-scale, for assignment %s, student %s" % (grades[i][j], i + 1, studieIDS[j]))

    print("\n")


# Purpose of function is to print the amount of assignments and students
# Input is an NxM matrix, holding students (studyID, Name) and their grades on a series of assignments
# Function has no output
# Author: Jacob Pjetursson, s153718, 2018
def printDescription(data):
    assignmentAmount, studentAmount = data.shape
    print("Number of students in file: %s" % (studentAmount - 1))
    print("Number of assignments in file: %s" % (assignmentAmount - 2))


# Purpose of function is to load in data from a filename specified by the user
# Function has no input (other than user input)
# Function outputs the data from the file which has been loaded in
# Author: Jacob Pjetursson, s153718, 2018
def dataLoad():
    while True:
        filename = input("Enter name of CSV-file : ")
        try:
            data = pd.read_csv(filename, quotechar='"')
            break
        except FileNotFoundError:
            print("File does not exist!")
            pass
    printDescription(data)
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
        print("{:d}. {:s}".format(i + 1, options[i]))
    # Get a valid menu choice
    choice = 0
    while not (np.any(choice == np.arange(len(options)) + 1)):
        choice = inputNumber("Please choose a menu item: ")

    return choice


def startProgram():
    # INITIAL FILE LOAD IN:
    data = dataLoad()

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
        # ------------------------------------------------------------------
        # 3. Generate plots
        elif choice == 3:
            grades = data.drop(['StudieID', 'Name'], axis=1).values.T
            gradesPlot(grades)
        # ------------------------------------------------------------------
        # 4. Display list of grades
        elif choice == 4:
            displayData(data)
        # ------------------------------------------------------------------
        # 5. Quit
        elif choice == 5:
            # End
            break


if __name__ == "__main__":
    print("\n Greetings!")
    startProgram()
