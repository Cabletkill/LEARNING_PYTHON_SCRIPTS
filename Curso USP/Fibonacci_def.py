def exemplo(n): #sequencia de Fibonacci ate o numero n
    a, b =0,1
    while a <n:
        print(a, end='')
        a,b=b, a+b
        print()

exemplo(20)

