print("start code …") #Вадим

books = [
    {
        "title": "Волк и Козёл",
        "author": "Лев Толстой",
        "year": 1890
    },
    {
        "title": "Дом кота",
        "author": "Марк Твен",
        "year": 2009
    },
    {
        "title": "Война и мир",
        "author": "Лев Толстой",
        "year": 1869
    },
    {
        "title": "Преступление и наказание",
        "author": "Фёдор Достоевский",
        "year": 1866
    },
    {
        "title": "Мастер и Маргарита",
        "author": "Михаил Булгаков",
        "year": 1967
    }
]


for book in books:
    print(f"Название: {book['title']}")
    print(f"Автор: {book['author']}")
    print(f"Год: {book['year']}")
    print()

print("end code …")

