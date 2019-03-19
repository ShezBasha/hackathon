#sum array
def sum_array(array):

    '''Return sum of all items in array'''
    if len(array) == 0:
        return 0
    else:
        return array[0] + sum_array(array[1:])

#fibonacci
def fibonacci(n):

    '''Return nth term in fibonacci sequence'''
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

#Factorial
def factorial(n):

    '''Return n!'''

    if n == 1:
        return n
    else:
        return n * factorial(n-1)


#reverse
def reverse(word):

    '''Return word in reverse'''

    return reverse(word[1:]) + word[0]
