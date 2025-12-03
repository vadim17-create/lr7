 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Главный файл программы
Запуск: python main.py
"""

# Добавим текущую папку в путь Python для корректных импортов
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Импортируем функции из пакета collision
from collision.task2 import isCorrectRect
from collision.task3 import isCollisionRect
from collision.task4 import intersectionAreaRect
from collision.task5 import intersectionAreaMultikect
from collision.errors import RectCorrectError

def print_separator():
    print("=" * 60)

def main():
    """Главная функция программы"""
    print_separator()
    print("ПРОГРАММА ДЛЯ РАБОТЫ С ПРЯМОУГОЛЬНИКАМИ")
    print_separator()
    
    while True:
        print("\nМЕНЮ:")
        print("1. Проверить корректность прямоугольника")
        print("2. Проверить пересечение двух прямоугольников")
        print("3. Вычислить площадь пересечения")
        print("4. Тестирование всех функций")
        print("5. Выход")
        
        choice = input("Выберите действие (1-5): ").strip()
        
        if choice == '1':
            try:
                print("\nВведите координаты прямоугольника:")
                x1 = float(input("x1 (левая граница): "))
                y1 = float(input("y1 (нижняя граница): "))
                x2 = float(input("x2 (правая граница): "))
                y2 = float(input("y2 (верхняя граница): "))
                
                rect = [(x1, y1), (x2, y2)]
                result = isCorrectRect(rect)
                
                print(f"\nПрямоугольник: {rect}")
                print(f"Результат: {'✓ КОРРЕКТНЫЙ' if result else '✗ НЕКОРРЕКТНЫЙ'}")
                
            except ValueError:
                print("Ошибка! Введите числа.")
        
        elif choice == '2':
            try:
                print("\n=== ПЕРВЫЙ ПРЯМОУГОЛЬНИК ===")
                x1 = float(input("x1: "))
                y1 = float(input("y1: "))
                x2 = float(input("x2: "))
                y2 = float(input("y2: "))
                rect1 = [(x1, y1), (x2, y2)]
                
                print("\n=== ВТОРОЙ ПРЯМОУГОЛЬНИК ===")
                x3 = float(input("x1: "))
                y3 = float(input("y1: "))
                x4 = float(input("x2: "))
                y4 = float(input("y2: "))
                rect2 = [(x3, y3), (x4, y4)]
                
                result = isCollisionRect(rect1, rect2)
                
                print(f"\nПрямоугольник 1: {rect1}")
                print(f"Прямоугольник 2: {rect2}")
                print(f"Результат: {'✓ ПЕРЕСЕКАЮТСЯ' if result else '✗ НЕ ПЕРЕСЕКАЮТСЯ'}")
                
            except RectCorrectError as e:
                print(f"Ошибка: {e}")
            except ValueError:
                print("Ошибка! Введите числа.")
        
        elif choice == '3':
            try:
                print("\n=== ПЕРВЫЙ ПРЯМОУГОЛЬНИК ===")
                x1 = float(input("x1: "))
                y1 = float(input("y1: "))
                x2 = float(input("x2: "))
                y2 = float(input("y2: "))
                rect1 = [(x1, y1), (x2, y2)]
                
                print("\n=== ВТОРОЙ ПРЯМОУГОЛЬНИК ===")
                x3 = float(input("x1: "))
                y3 = float(input("y1: "))
                x4 = float(input("x2: "))
                y4 = float(input("y2: "))
                rect2 = [(x3, y3), (x4, y4)]
                
                area = intersectionAreaRect(rect1, rect2)
                
                print(f"\nПрямоугольник 1: {rect1}")
                print(f"Прямоугольник 2: {rect2}")
                print(f"Площадь пересечения: {area:.2f}")
                
            except Exception as e:
                print(f"Ошибка: {e}")
        
        elif choice == '4':
            print_separator()
            print("ТЕСТИРОВАНИЕ ВСЕХ ФУНКЦИЙ")
            print_separator()
            
            # Тест 1: isCorrectRect
            print("\n1. Тест isCorrectRect:")
            tests = [
                ([(1, 1), (4, 4)], True),
                ([(4, 4), (1, 1)], False),
                ([(-3.4, 1), (9.2, 10)], True),
                ([(-7, 9), (3, 6)], False),
            ]
            
            for rect, expected in tests:
                result = isCorrectRect(rect)
                status = "✓" if result == expected else "✗"
                print(f"   {status} {rect} -> {result}")
            
            # Тест 2: isCollisionRect
            print("\n2. Тест isCollisionRect:")
            rect_a = [(-3.4, 1), (9.2, 10)]
            rect_b = [(-7.4, 0), (13.2, 12)]
            rect_c = [(1, 1), (2, 2)]
            rect_d = [(3, 0), (13, 1)]
            
            try:
                result1 = isCollisionRect(rect_a, rect_b)
                print(f"   [(-3.4,1),(9.2,10)] и [(-7.4,0),(13.2,12)] -> {result1} (True)")
            except Exception as e:
                print(f"   Ошибка: {e}")
            
            try:
                result2 = isCollisionRect(rect_c, rect_d)
                print(f"   [(1,1),(2,2)] и [(3,0),(13,1)] -> {result2} (False)")
            except Exception as e:
                print(f"   Ошибка: {e}")
            
            # Тест 3: intersectionAreaRect
            print("\n3. Тест intersectionAreaRect:")
            area = intersectionAreaRect(rect_a, rect_b)
            print(f"   Площадь пересечения примеров выше: {area:.2f}")
            
            # Тест 4: intersectionAreaMultikect
            print("\n4. Тест intersectionAreaMultikect:")
            rectangles = [
                [(-3, 1), (9, 10)],
                [(-7, 0), (13, 12)],
                [(0, 0), (5, 5)],
                [(2, 2), (7, 7)]
            ]
            
            try:
                total = intersectionAreaMultikect(rectangles)
                print(f"   Общая площадь 4 прямоугольников: {total:.2f}")
            except Exception as e:
                print(f"   Ошибка: {e}")
        
        elif choice == '5':
            print("\nВыход из программы...")
            break
        
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
