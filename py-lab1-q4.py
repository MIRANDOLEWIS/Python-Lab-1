number = int(input("enter a number : "))

answer = []

for i in range (2 , number):
    if number %  i  == 0:

        answer.append(i)

print(" Divisor of the number is ",answer)        


