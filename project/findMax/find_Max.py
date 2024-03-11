def find_max(numbers):
    if not numbers:
        # Return None when list empty
        return None  
    max = numbers[0]
    for num in numbers:
        if num > max:
            max = num
    return max