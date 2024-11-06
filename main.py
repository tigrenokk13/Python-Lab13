import csv
import json

# (Стешенко Станіслав КН-31.1)
# Функція для створення CSV-файлу з даними про країни
def create_csv_file():
    data = [
        # Площа в тис. кв. км, населення в млн
        {"country": "Україна", "area": 603.6, "population": 41},      
        {"country": "Америка", "area": 9833.5, "population": 331},
        {"country": "Японія", "area": 377.9, "population": 126}
    ]

    try:
        with open('countries.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["country", "area", "population"])
            writer.writeheader()
            writer.writerows(data)
        print("CSV файл 'countries.csv' успішно створено.")
    except Exception as e:
        print(f"Помилка при створенні CSV-файлу: {e}")

# (Стешенко Станіслав КН-31.1)
# Функція для конвертації CSV у JSON
def csv_to_json():
    try:
        data = []

        # Читання CSV файлу
        with open('countries.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['area'] = float(row['area'])         # Площа в тис. кв. км (float)
                row['population'] = int(row['population'])  # Населення в млн (int)
                data.append(row)

        # Запис у JSON файл
        with open('countries.json', mode='w') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)  # ensure_ascii=False для збереження кирилиці
        print("JSON файл 'countries.json' успішно створено.")

    except FileNotFoundError:
        print("Помилка: Файл 'countries.csv' не знайдено.")
    except json.JSONDecodeError:
        print("Помилка: Не вдалося декодувати JSON.")
    except Exception as e:
        print(f"Невідома помилка: {e}")

# Виконання
create_csv_file()
csv_to_json()