def factorials(n):
    #Calculate factorials
    if n < 0:
        return None  
    elif n == 0:
        return 1  
    else:
        fact = 1  
        for i in range(1, n + 1):
            fact *= i
        return fact
