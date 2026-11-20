def double(number):
    return number * 2
result = double(7)
print(result)



def average(a, b, c):
    return(a + b + c ) / 3
print(average(4, 5, 9))



def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    print(is_even(5))




def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b
print(max_of_two(5, 9))