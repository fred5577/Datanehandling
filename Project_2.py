import numpy as np
#Program for grading students


def roundGrade(grades):
    sevenStep = np.array([-3, 0, 2, 4, 7, 10, 12])
    #print(np.abs(grades, sevenStep))
    for grade in grades:
        print(grade)
        print(min(sevenStep, key=lambda x:abs(x-grade)))

    gradesRounded = [1]
    return gradesRounded


print(roundGrade(np.array([1, 2, 3, 4, 5, 6, 7])))
