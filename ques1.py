def calculate_average(numbers):
    total = 0
    for i in range(numbers):
        total += numbers[i]
    average = total / len(numbers)
    return average

nums = [10, 20, 30, 40]
print("The average is: " + calculate_average(nums))
