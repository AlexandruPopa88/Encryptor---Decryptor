def solve(n):
    a = 0
    while a * 10 + 9 <= n:
        a = a * 10 + 9
    return sum(map(int, str(a) + str(n-a)))

import time
start_time = time.time()

solve(10**10)

print("--- %s seconds ---" % (time.time() - start_time))