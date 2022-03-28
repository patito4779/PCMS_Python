


dict = {}
dict["Anna"] = 25
dict["james"] = 33
dict["Luke"] = 44

print(dict)

for keys, values in dict.items():
    print(values)


# short code to check for prime numbers in python
y = int(input("Enter a maximum value for the numbers you want to check for prime: "))
for n in range(2, y):
    prime = True
    for x in range(2, n):
        if n % x == 0:
            print(n, " is not a prime number")
            prime = False
            break
        
    if prime: print(n, " is a prime number") 



    


    


