def f(x):
    print(id(x)) # id(x) returns the id of the 10 or 123 object
    x = 1024
    return(x)

x=10
print(id(x))
print(id(10)) # note that id(x) and id(10) return the same value
print( id( f(10) ) ) # shows the id of the 1024 object
x=123
print(id(x))
print(id(123)) # note that id(x) and id(123) return the same value
print( id( f(123) ) )  # prints the id of the 1024 object
