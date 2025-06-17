import re
from collections import Counter

def text_analyzer(file_path):
    """Анализирует текст в файле и выводит статистику."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read().lower()  # Чтение файла
        
        # Подсчёт символов (без пробелов и переносов строк)
        chars = [char for char in text if char.isalpha()]
        char_stats = Counter(chars)
        
        # Подсчёт слов (игнорируем знаки препинания)
        words = re.findall(r'\b\w+\b', text)
        word_stats = Counter(words)
        
        # Вывод результатов
        print(f"\n📊 Анализ файла: {file_path}")
        print(f"📝 Всего слов: {len(words)}")
        print(f"🔤 Уникальных слов: {len(word_stats)}")
        print(f"📜 Всего символов (без пробелов): {len(chars)}")
            
        print("\n🔠 Частота символов:")
        for char, count in char_stats.most_common(5):
            print(f"'{char}': {count} раз")
    
    except FileNotFoundError:
        print("❌ Ошибка: файл не найден!")
    except Exception as e:
        print(f"❌ Произошла ошибка: {e}")

# Пример использования
if __name__ == "__main__":
    file_path = input("Введите путь к файлу (.txt): ")
    text_analyzer(file_path)



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