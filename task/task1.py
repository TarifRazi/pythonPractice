name = "Tarif Razi"
age = 23
city = "Dhaka"

a = 12
b = 5.5
fokir = True

print("Name:", name)
print("Age:", age)
print("City:", city)   

print(type(a))
print(type(b))
print(type(fokir))

Name = input("Enter your name: ")
Age = input("Enter your age: ")
City = input("Enter your city: ")  
Salary = input("Enter your salary: ")

if int(Age) > 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


if float(Salary) > 50000:
    fokir = False
print(Name, "Fokir status:", fokir)

if fokir == True:
    for i in range(5):
        print("Kam kor..!!")
