# Простой калькулятор
print("💻 Простой калькулятор")

while True:
    print("\nВыберите операцию:")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("5. Выход")

    choice = input("Ваш выбор (1-5): ")

    if choice == '5':
        print("Выход из программы...")
        break

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            
            if choice == '1':
                print(f"Результат: {num1} + {num2} = {num1 + num2}")
            elif choice == '2':
                print(f"Результат: {num1} - {num2} = {num1 - num2}")
            elif choice == '3':
                print(f"Результат: {num1} * {num2} = {num1 * num2}")
            elif choice == '4':
                if num2 == 0:
                    print("Ошибка: деление на ноль!")
                else:
                    print(f"Результат: {num1} / {num2} = {num1 / num2}")
        except ValueError:
            print("Ошибка: введите числа корректно!")
    else:
        print("Неверный ввод. Попробуйте снова.")