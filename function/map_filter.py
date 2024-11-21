'''
# map (() man ber klore jemon(square))

def square(x):
    return x*x
    num = [5,4,6,77,82]
    result = list(map(square,num))
    print(result)
    




# Filter () jei ta tar satha mach na kore seta remove kore dei


# filter

num = [ 2,44,33,63,4]
result = list(filter (lambda x :  x%2==0,num))
print(result)

'''

#filter


num = [1,2,3,4,5]

result = list(filter(lambda x: x%2 == 0,num))

print(result)