from importlib.machinery import DEBUG_BYTECODE_SUFFIXES
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

        JNFDuieyyuhbjksfjgkgsmoj 
        skgsofgniru342782782ugnipo2wg
        rgmiwogrwniojurguibnwgrwyu8
        wKEMjkesj SDIJLGnsIOuguiy4we GUISEGHisG
            
        print("\n🔠 Частота символов:")
        for char, count in char_stats.most_common(5):
            print(f"'{char}': {count} раз")
    
    except FileNotFoundError:
        print("❌ Ошибка: файл не найден!")
    except Exception as e:
        print(f"❌ Произошла ошибка: {e}")

        bytearray
        ##@QTTQTtEDTDGTDSG
        DEBUG_BYTECODE_SUFFIXES
        322352525tge
        yield

# Пример использования
if __name__ == "__main__":
    file_path = input("Введите путь к файлу (.txt): ")
    text_analyzer(file_path)
