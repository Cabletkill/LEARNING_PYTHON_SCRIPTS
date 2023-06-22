
def fizzbuzz(x):
    if x % 3 == 0 and x % 5 == 0:
        certo = 'FizzBuzz'
    elif x % 5 == 0:
        certo = 'Buzz'
    elif x % 3 == 0:
        certo = 'Fizz'
    return certo
x=