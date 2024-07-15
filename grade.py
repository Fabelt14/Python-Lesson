grade = int(input("Enter your grade" "\n"))

if grade >= 90:
    print("You are in Grade A")
elif 80 <= grade < 90:
    print("You are in Grade B")
elif 70 <= grade < 80:
    print("You are in Grade C")
elif 60 <= grade < 70:
    print("You are in Grade D")
elif grade < 60:
    print("You are in Grade F")
else:
    print("You fail")
