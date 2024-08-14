# Promt user for input
num = int(input("Please enter a number between 0 to 100: "))

# Check condition if the input number is less than 0
if(num<0):
    print("Please enter a higher number")
    
# Check condition if the input number is greater than 100
elif(num>100):
    print("Please enter a lower number")

# Print the number
else:
    print(f'Your number is: {num}')

# Check if the number is odd or even
print("Number is even" if num % 2 == 0 else "Number is odd")
    
print("End of program")
