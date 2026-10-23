def plus(x, y):
    return x + y

def minus(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ошибка: деление на 0"
    return x / y

x = int(input("Введите аргумент>>>"))
op = input("Введите оператор>>>")
y = int(input("Введите аргумент>>>"))

if op == '+':
    print(plus(x, y))
    
elif op == '-':
    print(minus(x, y))
    
elif op == '/':
    print(divide(x, y))
    
elif op == '*':
    print(multiply(x, y))
else:
    print("Ошибка: неизвестный оператор")