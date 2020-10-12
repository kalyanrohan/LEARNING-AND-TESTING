def fibonacci(n):
    if n<=1:
        return n
    else:
        return (fibonacci(n-1))+(fibonacci(n-2))

nterms= int(input("n= "))
for i in range(1,nterms+1,1):
    print(fibonacci(i))



