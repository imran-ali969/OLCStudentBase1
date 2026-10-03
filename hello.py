def getgradepoint(mark):
    if mark >=75:
        return 1
    elif mark >= 70:
        return 2
    elif mark >= 65:
        return 3
    elif mark >= 60:
        return 4
    elif mark >= 55:
        return 5
    elif mark >= 50:
        return 6
    elif mark >= 45:
        return 7
    elif mark >= 40:
        return 8
    else:
        return 9
resultdict = {"English":54, "Higher Chinese":70, "Chemistry":50, "Geography":56, "Mathematics":63, "Physics":71,"Computing":68}
def calL1R5(resultdict):
    english = getgradepoint(resultdict["English"])
    chinese = getgradepoint(resultdict["Higher Chinese"])
    if english < chinese:
        total = english
    else:
        total = chinese
    for result in resultdict:
        if result != "English" and result != "Higher Chinese":
            total += getgradepoint(resultdict(subject))
    return total