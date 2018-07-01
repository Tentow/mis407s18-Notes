numbers = [1,2,3,4,5,6,7,8]

squares = list(map(lambda x: x**2, numbers))
cubes = list(map(lambda x: x**3, numbers))
quartics = list(map(lambda x: x**4, numbers))

print(numbers)
print(squares)
print(cubes)
print(quartics)
