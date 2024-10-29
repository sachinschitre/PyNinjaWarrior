def fibonacci_generator(max_num):
    a, b = 0, 1
    while a <= max_num:
        yield a
        a, b = b, a + b

# Usage:
for num in fibonacci_generator(10):
    print(num)
