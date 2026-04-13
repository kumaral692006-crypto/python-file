def sum(n):
    total=0
    for digital in str(n):
        total+=int(digital)
    return total
print(sum(1235))