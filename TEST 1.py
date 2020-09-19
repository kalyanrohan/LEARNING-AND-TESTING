#my_func is to tell which number is greater
def my_func():
    num1=float(input("enter the first number: "))
    num2=float(input("enter the second number: "))
    num3=float((input("enter the third number: ")))
    if num1>=num2 and num1>=num3:
        return num1
    elif num2 >=num1 and num2 >= num3:
        return num2
    else:
        return num3
#function_2 is to tell whether the sum of 2 numbers are even/odd
def function_2():
    num1=float(input("enter the first number: "))
    num2=float(input("enter the second number: "))
    if (num1+num2)%2 ==0:
        return("even")
    else:
        return("odd")
print(function_2())




































































