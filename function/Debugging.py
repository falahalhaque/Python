def add(*number):
    sum = 0
    for num in number:
        sum = sum + num
    return sum

print(add(10, 20))
