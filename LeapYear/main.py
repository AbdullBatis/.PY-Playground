def is_leap_year(year):  
    """A Function that finds the leap year"""
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return f"The year {year} is a Leap year."
    else:
        return f"The year {year} is not a Leap year."

# Loop to print leap years from 0 to 2000
for i in range(0, 2001):
    print(is_leap_year(i))

