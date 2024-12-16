#Counting the odd and even numbers 
def count_odd_even(numbers):
    odd_count = 0
    even_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return odd_count, even_count

n = int(input("Enter the number of elements in the list: "))
numbers = []

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)


odd_count, even_count = count_odd_even(numbers)


print(f"The list of numbers is: {numbers}")
print(f"Number of odd numbers: {odd_count}")
print(f"Number of even numbers: {even_count}")
