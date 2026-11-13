while True:
    print("\n"+"="*30)
    print(" МЕНЮ КАЛЬКУЛЯТОРА")
    print("="*30)
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("0. Выход")
    print("="*30)

    choice = input("Выберите операцию (0-5): ")

    if choice == "0":
        print("До скорой встречи!")
        break

    if choice not in ["1", "2", "3", "4", "5"]:
        print("Такой цифры нет, попробуйте снова!")
        continue

    
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    
    if choice == "1":
        result = num1 + num2
        print(f"Результат: {num1} + {num2} = {result}")
        
    elif choice == "2":
        result = num1 - num2
        print(f"Результат: {num1} - {num2} = {result}")
        
    elif choice == "3":
        result = num1 * num2
        print(f"Результат: {num1} * {num2} = {result}")
        
    elif choice == "4":
        if num2 == 0:
            print("Ошибка: на ноль делить нельзя!")
        else:
            result = num1 / num2
            print(f"Результат: {num1} / {num2} = {result}")
            
    elif choice == "5":
        result = num1 ** num2
        print(f"Результат: {num1} в степени {num2} = {result}")