def isLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0):
        print("Leap year")
        return True
    elif (year % 400 == 0):
        print("Lear year")
        return True
    else:
        print("Not leap year")
        return False

isLeapYear(2002)