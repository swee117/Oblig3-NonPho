from leap_year import isLeapYear
#Akseptansekriterier: delelig med 4
def test_leap_year_divideable_by_4():
    assert isLeapYear(2400) == True
    assert isLeapYear(1996) == True

#Akseptansekriterier: delelig med 100
def test_leap_year_divideable_by_100():
    assert isLeapYear(2300) == False
    assert isLeapYear(3500) == False

#Akseptansekriterier: delelig med 400
def test_leap_year_divideable_by_400():
    assert isLeapYear(1600) == True
    assert isLeapYear(2800) == True

#Akseptansekriterier: test PASS, om (year) input er ikke leap year
def test_not_leap_year():
    assert isLeapYear(2002) == False
    assert isLeapYear(2125) == False

#Akseptansekriterier: test PASS, om (year) input er leap year
def test_leap_year():
    assert isLeapYear(2000) == True
    assert isLeapYear(2124) == True