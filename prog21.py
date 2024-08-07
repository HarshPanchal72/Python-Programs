# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
def generate_dict(n):
    return {x: x*x for x in range(1, n+1)}

n = 10
dict = generate_dict(n)
print(dict)