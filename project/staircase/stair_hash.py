def hash_pyramid(n, k=0):
    for i in range(1, n+1):
        for space in range(1, (n-i)+1):
            print(end="")
        while k!=(i):
            print("#", end="")
            k += 1
        k = 0
        print()


n = int(input("Enter number of n: "))
hash_pyramid(n)

