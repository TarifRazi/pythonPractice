def sum(a, b):
    return (a + b)

total = sum(int(input("a = ")), int(input("b = ")))

print("total =", total)

def greet(name):
    print("Hello", name)

greet(input("Enter your name: "))

def numCheck(num):
    if num > 0:
        print(num, "is a positive number")
    elif num < 0:
        print(num, "is a negative number")
    else:
        print("The number is zero")

numCheck(int(input("Enter a number: ")))
