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

#how dictionary works, ditionary uses {}
#essentially it uses keys to indetify certain values
Months= {"Jan":"Januray",
"Feb":"February",
"Mar":"March",
"Apr":"April",
"May":"May",
"Jun":"June",
"Jul":"July",
"Aug":"August",
'Sept':"September",
"Oct":"October",
"Nov":"November",
"Dec":"December"
}
#to print all of the keys in the dcitionary
for x in Months:
    print(x)
#to print the values of the keys in the dictionary
for x in Months:
    print(Months[x])
#another way to print the values of the keys in the dictionary
for x in Months.values():
    print(x)
#If want to print both values and keys
for x in Months.items():
    print(x)
# you can also check whether a key exist in a dictionary
if "Jan" in Months:
    print("January is there")
# to change the values in the dictionary
Months["Jan"]="janice"
print(Months["Jan"])
# to add new items to the dictionary
Months["year"]=2020
# another way to print keys and their corresponding items
for x,y in Months.items():
    print(x,y)
# to remove an item from the dictionary
Months.pop("Feb")
# to remove the last item in the dictionary
Months.popitem()
print(Months)
# to copy a dicitionary
months2= Months.copy()
months3=dict(Months)
# creating dictionaries in a dictionary
Patients= {
    "Patient 1":{"Name":"Marcus","Age":21},
    "Patient 2":{"Name":"Joan","Age":24},
    "Patient 3":{"Name":"Gabriel","Age":20}
}
# To get the value of the value
print(Patients.get("Patient 2").get("Age"))
# Alternatively
Patient_1={"Name":"Marcus","Age":21}
Patient_2={"Name":"Joan","Age":24}
Patient_3={"Name":"Gabriel","Age":20}
Pateints={"Patient 1":Patient_1,"Patient 2":Patient_2,"Patient 3":Patient_3}
print(Patients.get("Patient 2").get("Age"))
#Alternate way to create dictionaries
Colors=dict(light="Yellow",dark="Black",mixed="Green")
print(Colors["light"])
#to update your dictionary
Colors.update({"black":"grey"})
print(Colors)
#to check whether a key exists. If key don't exist, can add it as a new key.
Colors.setdefault("grey","ash grey")
print(Colors)

days=("mon","tues","wed","thurs","fri","sat","sun")
days1=("monday","tuesday","wednesday","thursday","friday","saturday","sunday")

















































































