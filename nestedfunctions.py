x=1
def outer():
    x=2
    print(x)
    def inner():
        nonlocal x
        x=3
        print(x)
    print(x)
    inner()
    print(x)

print(x)
outer()
print(x)


