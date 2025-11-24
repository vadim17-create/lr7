print("start code …") #Вадим
import json

def search_skill():
    try:
        with open('dump.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
    except:
        print("Ошибка загрузки файла!")
        return
    
    # Ввод кода
    skill_code = input("Введите код квалификации: ").strip()
    
    # Поиск
    found = False
    for item in data:
        if (item.get('model') == 'data.skill' and 
            item.get('fields', {}).get('code') == skill_code):
            print("\n" + "="*15 + "Найдено" + "="*15)
            fields = item['fields']
            print(f"Код: {fields['code']}")
            print(f"Название: {fields['title']}")
            found = True
            break
    
    if not found:
        print("\n" + "="*15 + "Не найдено" + "="*13)

# Запуск поиска
search_skill()
print("end code …")
