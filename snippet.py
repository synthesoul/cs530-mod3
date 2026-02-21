def calculate_statistics(numbers: list) -> tuple:
    if not numbers:
        return (0, 0, 0)
    
    total = 0
    count = 0
    maximum = numbers[0]
    
    for num in numbers:  
        total += num
        count += 1
    
    average = total / count
    
    for i in range(len(numbers)):
        if numbers[i] > maximum:
            maximum = numbers[i]
    
    minimum = min(numbers)
    
    print("Valid stats")
    
    return average, minimum, maximum

    
def validate_numbers(numbers):
    pass


result = calculate_statistics([1, 2, 3, 4, 5])
