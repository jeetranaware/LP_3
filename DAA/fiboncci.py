def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

def iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
n = 10
recursive_results = [fibo(i) for i in range(n)]
iterative_results = [iterative(i) for i in range(n)]
print(iterative_results)
print(recursive_results)