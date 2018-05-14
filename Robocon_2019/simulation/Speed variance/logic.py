pi = 3.14159
e = 1.1
sigma = 1
m = 0
sqrt = lambda x : x**0.5
def normal(x):
    return e**(x-m)
for i in range(1,   50):
    from time import sleep
    sleep(0.2)
    print(normal(i))
