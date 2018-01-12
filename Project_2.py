import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import random


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

def gradesPlot(data):
    grades = data.drop(['StudieID', 'Name'], axis=1).values.T
    final = computeFinalGrades(grades)
    
    #Setup the figure to contain both plots
    plt.figure(figsize=(15, 6))
    plt.subplots_adjust(wspace=0.5)
    plt.subplot(1, 2, 1)
    
    #Plot the histogram for the final grades
    plt.hist(final, rwidth=0.75, edgecolor='black')
    plt.title("Amount of each grade")
    plt.xlabel("Grades")
    plt.ylabel("Number of students")
    
    #Setup for the Scatterplot
    (x, y) = np.shape(grades)
    grades = grades.astype(float)
    #Randomize the +/-0.1 for each value in the grades matrix
    for k in range(y):
        for i in range(x):
            grades[i][k] = grades[i][k]+((random.random()*2*0.1)-0.1)
 
    
    plt.subplot(1, 2, 2)
    #Loop through every row of the grades matrix and create a scatterplot for each, with the x value 'i +/-0.1'
    for i in range(x):
        iList = np.zeros(y)
        for k in range(y):
            iList[k] = i+(random.random()*2*0.1)-0.1
        plt.scatter(iList, grades[i, :])
    
    #Calculate a vector with the mean of each assignment
    avg = np.zeros(x)
    for i in range(x):
        avg[i] = np.mean(grades[i, :])
    
    #Plot the line of averages
    plt.plot(avg, '-')
    
    #Show the two subplots
    plt.title("Grades")
    plt.xlabel("Assignment")
    plt.ylabel("Grade")
    plt.show()
    

def checkDataErrors(data):
    studieIDS = data['StudieID'].values
    grades = data.drop(['StudieID', 'Name'], axis=1).values
    if np.unique(studieIDS).size != len(studieIDS):
        print("Study-ids are not unique! \n")

    seven = [-3, 0, 2, 4, 7, 10, 12]
    for i in range(len(grades)):
        for j in range(len(grades[i])):
            if grades[i][j] not in seven:
                print("%s is not on 7-step-scale, for assignment %s, student %s" % (grades[i][j], i+1, studieIDS[j]))

    print("\n")

def printDescription(data):
    assignmentAmount, studentAmount = data.shape
    print("Number of students in file: %s" % (studentAmount-1))
    print("Number of assignments in file: %s" % (assignmentAmount-2))


def dataLoad():
    while True:
        filename = input("Enter name of CSV-file")
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
        print("{:d}. {:s}".format(i+1, options[i]))
    # Get a valid menu choice
    choice = 0
    while not(np.any(choice == np.arange(len(options))+1)):
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
            gradesPlot(data)
        # ------------------------------------------------------------------
        # 4. Display list of grades
        elif choice == 4:
            print("ehh")
            #displayGrades(data)
        # ------------------------------------------------------------------
        # 5. Quit
        elif choice == 5:
            # End
            break

if __name__ == "__main__":
    print("\n Greetings!")
    startProgram()

