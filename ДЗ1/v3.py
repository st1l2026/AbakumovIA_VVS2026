def plus(x, y):
    return x + y

def minus(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ошибка: деление на ноль"
    return x / y

def calc(x, op, y):
    if op == '+':
        print(plus(x, y))
        
    elif op == '-':
        print(minus(x, y))
        
    elif op == '/':
        print(divide(x, y))
        
    elif op == '*':
        print(multiply(x, y))

fl = 1
while fl == 1:
    fl = int(input("Если хотите закончить, введите 0, иначе - 1>>>"))
    if fl == 0: 
        break
    x = int(input("Введите 1 число>>>"))
    op = input("Введите оператор>>>")
    y = int(input("Введите 2 число>>>"))
    calc(x, op, y)
