def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

print("select an action")
print("add")
print("subtraction")

choice = input("select an action: ")

num1 = int(input("add: "))
num2 = int(input("subtraction: "))

if choice == '1':
    print(f"res: {num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"res: {num1} - {num2} = {subtract(num1, num2)}")
else:
    print("entered incorrectly!")