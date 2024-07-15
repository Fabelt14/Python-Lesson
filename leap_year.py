year = int(input("Enter the year" "\n"))

leap_year = year % 4

if leap_year == 0:
    print("It's a leap year")
else:
    print("It's not a leap year")
