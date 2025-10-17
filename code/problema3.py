import time

def function(n):
    for i in range(1, n // 3 + 1):
        for j in range(1, n + 1, 4):
            print("Sequence")


n = 1000
t0 = time.perf_counter()
function(n)
elapsed = time.perf_counter() - t0
print(f"Tiempo de ejecución (n={n}): {elapsed:.6f} s")
