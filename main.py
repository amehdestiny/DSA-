def find_largest(numbers):
    if not numbers:
        return None
    
    largest = numbers[0]
    
    for num in numbers[1:]:
        if num > largest: 
            largest = num
            
    return largest

def find_largest(numbers):
    if not numbers:
        return None
    
    largest = numbers[0]
    
    for num in numbers[:1]:
        if num > largest: 
            largest = num
            
    return largest

def list_sum(numbers):
    total = 0
    
    for num in numbers:
        total += num
        
    return total

def count_even(numbers):
    count = 0

    for num in numbers:
        if num % 2 == 0:
            count += 1
            
    return count    

def count_occurrences(numbers, target):
    count = 0
    
    for num in numbers:
        if num == target:
            count += 1
            
    return count    

def find_number(numbers, target):
    for index, num in enumerate(numbers):
        if num == target
            
    return -1

def reverse_list(items):
    reversed_items = []
    
    for i in range(len(items) - 1, -1, -1):
        reversed_items.append(items[i])
        
    return reversed_items

def has_duplicates(numbers):
    seen = set()
    
    for num in numbers:
        if num in seen:
            return True

        seen.add(num)
        
    return False    

def find the first duplicate(numbers):
    seen = set()

    for num in numbers:
        if num in seen:
            return num

            seen.add(num)    

def move all zeros to the end(numbers):
    non_zero_numbers = []
    zero_count = 0

    for num in numbers:
        if num == 0:
            zero_count += 1
        else:
            non_zero_numbers.append(num)

        return non_zero_numbers + [0] * zero_count

