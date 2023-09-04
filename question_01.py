# Write a Python program to get the Fibonacci series between 0 to 50

# we can write the fibonacci series on both loops(we can choose either version depending on your preference.)



# Using for loop.

no1 = 0
no2 = 1
print(no1, no2 , end = " ")

for i in range (2,51):
    new_number = no1 + no2
    if new_number <= 50 :
        print(new_number, end =" ")
        no1 = no2  
        no2 = new_number
    else:
        break


    # or
   

# using while loop

no1 = 0 
no2 = 1

print( no1, no2, end=" ")

while no2 <= 50 :
    new_number = no1 + no2
    
    if new_number <= 50 :
        print(new_number, end=" ")
        no1 = no2
        no2 = new_number
    else:
        break