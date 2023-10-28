def sum_of_elements(numbers, exclude_negative = False):
    sum = 0
    if exclude_negative == False:
        for item in numbers:
            sum += item

    else:
        for item in numbers:
            if item > 0:
                sum += item
    return sum

string_number = input("Enter a list of numbers separated by spaces: ")
numbers = string_number.split()
numbers = [int(num) for num in numbers]
print (numbers)
exclude_negative = input("Exclude negative numbers (yes or no)?")

if exclude_negative == "yes":
    print(sum_of_elements(numbers, True))
else:
    print(sum_of_elements(numbers))