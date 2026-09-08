def PowTwoGen(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1

max_power = int(input("Enter the number of powers of 2 to generate: "))

print("Powers of 2 are:")
for value in PowTwoGen(max_power):
    print(value)