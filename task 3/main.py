print("start code …") #Вадим
# Список для хранения записей о звёздах (in-memory)
stars = []
next_id = 1  # Автоматический ID

# Функция для добавления новой звезды
def add_star():
    global next_id
    try:
        name = input("Введите общее название звезды: ").strip()
        if not name:
            print("Название звезды не может быть пустым.")
            return
        constellation = input("Введите название созвездия: ").strip()
        if not constellation:
            print("Название созвездия не может быть пустым.")
            return
        is_visible_str = input("Можно ли увидеть звезду без телескопа? (y/n): ").strip().lower()
        is_visible = True if is_visible_str == 'y' else False
        radius = float(input("Введите солнечный радиус звезды: ").strip())
        if radius <= 0:
            print("Солнечный радиус должен быть положительным.")
            return
        
        star = {
            'id': next_id,
            'name': name,
            'constellation': constellation,
            'is_visible': is_visible,
            'radius': radius
        }
        stars.append(star)
        next_id += 1
        print("Звезда добавлена успешно!")
    except ValueError:
        print("Ошибка ввода: солнечный радиус должен быть числом.")

# Функция для просмотра всех звёзд
def view_all_stars():
    if not stars:
        print("Нет записей о звёздах.")
        return
    print("\nВсе звёзды:")
    for star in stars:
        visible_status = "Да" if star['is_visible'] else "Нет"
        print(f"ID: {star['id']}, Название: {star['name']}, Созвездие: {star['constellation']}, "
              f"Видна без телескопа: {visible_status}, Солнечный радиус: {star['radius']}")

# Функция для поиска звезды по ID
def find_star_by_id():
    try:
        star_id = int(input("Введите ID звезды: ").strip())
        for star in stars:
            if star['id'] == star_id:
                visible_status = "Да" if star['is_visible'] else "Нет"
                print(f"Найдено: ID: {star['id']}, Название: {star['name']}, Созвездие: {star['constellation']}, "
                      f"Видна без телескопа: {visible_status}, Солнечный радиус: {star['radius']}")
                return
        print("Звезда с таким ID не найдена.")
    except ValueError:
        print("Неверный ID (должен быть числом).")

# Функция для удаления звезды по ID
def delete_star():
    try:
        star_id = int(input("Введите ID звезды для удаления: ").strip())
        for i, star in enumerate(stars):
            if star['id'] == star_id:
                confirm = input(f"Удалить '{star['name']}' ({star['constellation']})? (y/n): ").strip().lower()
                if confirm == 'y':
                    stars.pop(i)
                    print("Звезда удалена успешно!")
                else:
                    print("Удаление отменено.")
                return
        print("Звезда с таким ID не найдена.")
    except ValueError:
        print("Неверный ID (должен быть числом).")

# Основное меню
def main():
    while True:
        print("\n=== Программа хранения записей о звёздах (In-Memory) ===")
        print("1. Добавить звезду")
        print("2. Просмотреть все звёзды")
        print("3. Найти звезду по ID")
        print("4. Удалить звезду по ID")
        print("5. Выход")
        
        choice = input("Выберите опцию (1-5): ").strip()
        
        if choice == '1':
            add_star()
        elif choice == '2':
            view_all_stars()
        elif choice == '3':
            find_star_by_id()
        elif choice == '4':
            delete_star()
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

# Запуск программы
if __name__ == "__main__":
    main()

print("end code …")