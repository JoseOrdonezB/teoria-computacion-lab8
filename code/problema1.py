import time

def function(n):
    counter = 0
    for i in range(n // 2, n + 1):
        j_limit = n - n // 2
        for j in range(1, j_limit + 1):
            k = 1
            while k <= n:
                counter += 1
                k *= 2
    return counter
n = 1000
t0 = time.perf_counter()
res = function(n)
elapsed = time.perf_counter() - t0

print(res)
print(f"Tiempo de ejecución (n={n}): {elapsed:.6f} s")
