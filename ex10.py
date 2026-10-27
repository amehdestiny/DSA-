def move all zeros to the end(numbers):
    non_zero_numbers = []
    zero_count = 0

    for num in numbers:
        if num == 0:
            zero_count += 1
        else:
            non_zero_numbers.append(num)

        return non_zero_numbers + [0] * zero_count

