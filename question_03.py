# Write a Python program to count the number of even and odd numbers from a series of numbers.

numbers = (1,2,3,4,5,6,7,8,9,10,11)

even_number = 0
odd_number = 0

for i in numbers :
    if i % 2 == 0 :
        even_number+=1
    else:
        odd_number+=1
print(f"The count of even numbers are {even_number} \nThe count of odd numbers are {odd_number}")
