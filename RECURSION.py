def fact(n):
	if n==0:
		return 1
	return n*fact(n-1)
factorial=fact(eval(input("n= ")))
print(factorial)