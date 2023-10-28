def find_numbers(data): # find numbers in string and store them in list
    numbers_list = []
    string_number = ""
    for char in data:
        if char.isdigit():
            string_number += char
        else:
            numbers_list.append(int(string_number))
            string_number = ""
    if string_number:
        numbers_list.append(int(string_number))
    return numbers_list

def classify_numbers(numbers_list): # classify, wheter the number is odd or even
    odd_numbers = []
    even_numbers =[]
    for item in numbers_list:
        if item % 2 == 0:
            even_numbers.append(item)
        else:
            odd_numbers.append(item)
    return odd_numbers, even_numbers # function has returned a tuple!!! then we can unpack it

data = input("Input numbers separated by space:")
numbers_list = find_numbers(data)
odd_numbers , even_numbers = classify_numbers(numbers_list)

print("Odd numbers: ")
print(odd_numbers)
print("Even numbers: ")
print(even_numbers)
