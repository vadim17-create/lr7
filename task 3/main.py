print("start code …") #Вадим,вариант 3
import json
import os

# Имя файла для хранения данных
FILE_NAME = "stars.json"
# Счетчик операций
operation_count = 0

def load_stars_from_file():
    """Загружает данные о звездах из JSON файла"""
    global stars
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r', encoding='utf-8') as file:
            stars = json.load(file)
    else:
        # Предварительно заполненные 5 записей
        stars = [
            {"id": 1, "name": "Сириус", "constellation": "Большой Пес", "is_visible": True, "radius": 1.71},
            {"id": 2, "name": "Полярная", "constellation": "Малая Медведица", "is_visible": True, "radius": 45},
            {"id": 3, "name": "Бетельгейзе", "constellation": "Орион", "is_visible": True, "radius": 887},
            {"id": 4, "name": "Антарес", "constellation": "Скорпион", "is_visible": True, "radius": 680},
            {"id": 5, "name": "Вега", "constellation": "Лира", "is_visible": True, "radius": 2.78}
        ]
        save_stars_to_file()

def save_stars_to_file():
    """Сохраняет данные о звездах в JSON файл"""
    with open(FILE_NAME, 'w', encoding='utf-8') as file:
        json.dump(stars, file, ensure_ascii=False, indent=2)

def show_all_stars():
    """Выводит все записи о звездах"""
    global operation_count
    operation_count += 1
    
    print("\nВсе записи о звездах:")
    if not stars:
        print("Нет записей о звёздах.")
    else:
        for i, star in enumerate(stars, 1):
            visible_status = "Да" if star['is_visible'] else "Нет"
            print(f"{i}. ID: {star['id']}, Название: {star['name']}, Созвездие: {star['constellation']}, "
                  f"Видна без телескопа: {visible_status}, Солнечный радиус: {star['radius']}")

def show_star_by_field():
    """Выводит запись по полю ID и её позицию"""
    global operation_count
    operation_count += 1
    
    try:
        star_id = int(input("Введите ID звезды для поиска: ").strip())
        found = False
        
        for position, star in enumerate(stars, 1):
            if star['id'] == star_id:
                visible_status = "Да" if star['is_visible'] else "Нет"
                print(f"\nЗапись найдена!")
                print(f"Позиция в списке: {position}")
                print(f"ID: {star['id']}")
                print(f"Название: {star['name']}")
                print(f"Созвездие: {star['constellation']}")
                print(f"Видна без телескопа: {visible_status}")
                print(f"Солнечный радиус: {star['radius']}")
                found = True
                break
        
        if not found:
            print(f"Предупреждение: Звезда с ID {star_id} не найдена.")
            
    except ValueError:
        print("Ошибка: ID должен быть целым числом.")

def add_star():
    """Добавляет новую запись о звезде"""
    global operation_count, stars
    operation_count += 1
    
    try:
        # Находим максимальный ID для генерации нового
        max_id = max(star['id'] for star in stars) if stars else 0
        new_id = max_id + 1
        
        name = input("Введите общее название звезды: ").strip()
        if not name:
            print("Ошибка: Название звезды не может быть пустым.")
            return
            
        constellation = input("Введите название созвездия: ").strip()
        if not constellation:
            print("Ошибка: Название созвездия не может быть пустым.")
            return
        
        is_visible_input = input("Можно ли увидеть звезду без телескопа? (y/n): ").strip().lower()
        is_visible = True if is_visible_input == 'y' else False
        
        radius = float(input("Введите солнечный радиус звезды: ").strip())
        if radius <= 0:
            print("Ошибка: Солнечный радиус должен быть положительным числом.")
            return
        
        # Создаем новую запись
        new_star = {
            "id": new_id,
            "name": name,
            "constellation": constellation,
            "is_visible": is_visible,
            "radius": radius
        }
        
        # Добавляем в список
        stars.append(new_star)
        
        # Сохраняем в файл
        save_stars_to_file()
        
        print(f"Запись успешно добавлена с ID: {new_id}")
        
    except ValueError:
        print("Ошибка: Неверный формат данных. Солнечный радиус должен быть числом.")

def delete_star_by_field():
    """Удаляет запись по полю ID"""
    global operation_count, stars
    operation_count += 1
    
    try:
        star_id = int(input("Введите ID звезды для удаления: ").strip())
        found = False
        
        for i, star in enumerate(stars):
            if star['id'] == star_id:
                print(f"Найдена звезда: {star['name']} ({star['constellation']})")
                confirm = input("Вы уверены, что хотите удалить эту запись? (y/n): ").strip().lower()
                
                if confirm == 'y':
                    deleted_star = stars.pop(i)
                    
                    # Сохраняем в файл
                    save_stars_to_file()
                    
                    print(f"Запись с ID {star_id} успешно удалена.")
                else:
                    print("Удаление отменено.")
                
                found = True
                break
        
        if not found:
            print(f"Предупреждение: Звезда с ID {star_id} не найдена.")
            
    except ValueError:
        print("Ошибка: ID должен быть целым числом.")

def exit_program():
    """Завершает выполнение программы с выводом статистики"""
    global operation_count
    print(f"\nПрограмма завершена.")
    print(f"Количество выполненных операций с записями: {operation_count}")
    return False

def show_menu():
    """Отображает главное меню программы"""
    print("\n=== Программа хранения записей о звёздах ===")
    print("1. Вывести все записи")
    print("2. Вывести запись по полю (id)")
    print("3. Добавить запись")
    print("4. Удалить запись по полю (id)")
    print("5. Выйти из программы")

def main():
    """Основная функция программы"""
    global stars
    load_stars_from_file()
    
    running = True
    
    while running:
        show_menu()
        
        choice = input("Выберите пункт меню (1-5): ").strip()
        
        if choice == '1':
            show_all_stars()
        elif choice == '2':
            show_star_by_field()
        elif choice == '3':
            add_star()
        elif choice == '4':
            delete_star_by_field()
        elif choice == '5':
            running = exit_program()
        else:
            print("Ошибка: Неверный выбор. Пожалуйста, введите число от 1 до 5.")

# Запуск программы
if __name__ == "__main__":
    main()

print("end code …")