class FibonacciIterator:
    def __init__(self, max_num):
        self.max_num = max_num
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.max_num:
            raise StopIteration
        fib = self.a
        self.a, self.b = self.b, self.a + self.b
        return fib

# Usage:
fib_iter = FibonacciIterator(10)
for num in fib_iter:
    print(num)
