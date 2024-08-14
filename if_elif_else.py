num = int(input("Please enter a number between 0 to 100: "))

if(num<0):
    print("Please enter a higher number")

elif(num>100):
    print("Please enter a lower number")

else:
    print(f'Your number is: {num}')

print("Number is even" if num % 2 == 0 else "Number is odd")
    
print("End of program")