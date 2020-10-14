# try:
#     age=int(input("age: "))
#     print(age)
# except ValueError:
#     print("Invalid Value")

try:
    num1=int(input("enter number: "))
    num2=int(input("enter another number: "))
    result=num1/num2
    print(result)
except ValueError:
    print("Invalid Input")
except ZeroDivisionError as err:
    print(err)


 
        


