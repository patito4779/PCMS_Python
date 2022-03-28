for n in range(2, 10):
    prime = True
    for x in range(2, n):
        if n % x == 0:
            print(n, " is not a prime number")
            prime = False
            exit
    if prime: print(n, " is a prime number")