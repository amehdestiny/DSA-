def find the first duplicate(numbers):
    seen = set()

    for num in numbers:
        if num in seen:
            return num

            seen.add(num)  