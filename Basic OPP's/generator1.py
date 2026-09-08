def count_up_to(max_val):
    count = 1
    while count <= max_val:
        yield count
        count += 1


counter = count_up_to(5)

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))