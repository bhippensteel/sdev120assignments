#Hippensteel SDEV120

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] #creates a list of numbers 1-15

for number in numbers: #For loop to cycler through all numbers
    if number % 2 == 0: #Checks if number is even
        print(str(number) + " is Even")
    else: #If not even, number must be odd
        print(str(number) + " is Odd")