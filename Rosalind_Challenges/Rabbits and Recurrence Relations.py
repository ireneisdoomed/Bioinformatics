def rabbit_population(n, k):
    fn_2, fn_1 = 1, 1
    fn = 1
    for iter in range(2, n):
        fn = fn_2 * k + fn_1 
        fn_2, fn_1 = fn_1, fn
    
    return fn

file = open("data/rosalind_fib.txt")
file = file.read()
n = int(file.split(" ")[0])
k = int(file.split(" ")[1])

print(rabbit_population(n, k))
