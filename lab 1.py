print("Enter 'c' to convert from Celsius to Fahrenheit")
print("Enter 'f' to convert from Fahrenheit to Celsius")
choice = input("Enter your choice: ")
if choice == 'c':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5)+32
    print('%.2fCelsius is: %0.2fFahrenheit'%(celsius,fahrenheit))
elif choice == 'f':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32)*5/9
    print('%.2fFahrenheit is: %0.2fCelsius'%(fahrenheit,celsius))
else:
    print('Invalid Input')
