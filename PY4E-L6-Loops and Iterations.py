# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
# Once 'done' is entered, print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
# Enter 7, 2, bob, 10, and 4 and match the output below.

#Initiate variables 'largest' & 'smallest' - assign null value
largest = None
smallest = None

#Enter infinite loop
while True:

    #Initiate variable 'num' - assign user input
    num = input("Enter an integer number (or 'done' to finish): ")

    #If the number (in lower case) is equal to 'done' exit the loop
    #Example of a One-Way Decision
    if num.lower() == 'done':
        break

    try:
        num = int(num)
        if largest is None or num > largest:
            largest = num
        if smallest is None or num < smallest:
            smallest = num
    except ValueError:
        print("Invalid input")

print("Maximum", largest)
print("Minimum", smallest)