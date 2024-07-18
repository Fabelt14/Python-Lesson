'''Write a program that inputs a number n and 
prints the sum of all of the numbers from 1 to n:'''

n = int(input("Enter a number: "))

sum = 0

for i in range(1, n + 1):
    sum += i

print(sum)
