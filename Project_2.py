import numpy as np
#Program for grading students

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
        temp = np.asarray(roundGrade(grades[:, i]))
        if np.amin(temp) == -3:
            gradesFinal = np.append(gradesFinal, -3)
        else :
            tempMin = np.argmin(temp)
            tempArray = np.delete(temp, tempMin)
            tempM = tempArray.mean()
            gradesFinal = np.append(gradesFinal, tempM)

    return gradesFinal




if __name__ == "__main__":

    print(computeFinalGrades(np.array([[7.2,3.12,10.34,11.23],
                                        [-2.4,4.1,7,10]])))