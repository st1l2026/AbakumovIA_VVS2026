x = int(input("Введите 1 число>>>"))
op = input("Введите оператор>>>")
y = int(input("Введите 2 число>>>"))

if op == '+':
    print(x + y)
    
elif op == '-':
    print(x - y)
    
elif op == '/':
    if y != 0:
        print(x / y)
    else:
        print("Ошибка: деление на 0")

elif op == '*':
    print(x * y)

else:
    print("Ошибка ввода: неизвестный оператор")
