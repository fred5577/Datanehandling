import numpy as np
#Program for grading students


def roundGrade(grades):
    sevenStep = np.array([-3, 0, 2, 4, 7, 10, 12])
    gradesRounded = []
    for grade in grades:
        gradesRounded.append(min(sevenStep, key=lambda x: abs(x-grade)))
    return gradesRounded


