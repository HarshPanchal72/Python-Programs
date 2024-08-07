def is_prime(num):
    if num == 0:
        return 'this is a whole number'
    elif num == 1:
        return 'this is a natural number'
     
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            return 'this is prime number'
    return 'this is not prime number'

num = int(input('Enter a number: '))
print(is_prime(num))    