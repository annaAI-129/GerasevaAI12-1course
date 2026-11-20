books = [
    "Преступление и наказание",
    "Война и мир",
    "Маленький принц",
    "Гарри Поттер",
    "Хоббит",
    "Марсианские хроники"
    "Рапунцель"
    "Красавица и чудовище"
    "Колобок"
]

def show_menu():
    print("\n=== ЧИТАТЕЛЬСКИЙ ДНЕВНИК ===")
    print("1 - Добавить книгу")
    print("2 - Показать все книги")
    print("3 - Найти книгу")
    print("4 - Заменить название по номеру")
    print("5 - Последние 5 прочитанных книг")
    print("6 - Статистика")
    print("0 - Выход")

def add_books():
    name = input("Введите название книги: ")
    books.append(name)
    print("Книга была добавлена!")

def show_books():
    if not books:
        print("Список книг пуст.")
    else:
        for i in range(len(books)):
            print(f"{i + 1}. {books[i]}")

def search_book():
    name = input("Введите название книги: ")
    if name in books:
        print("Книга найдена!")
    else:
        print("Книга не найдена!")

def mark_book():
    
    name = input("Введите название книги, которую нужно заменить: ").strip()
    if name in books:
        new_name = input("Введите новое название: ").strip()
        books[books.index(name)] = new_name
        print(f"Книга '{name}' Заменена!")
       
    else:
        print("Книга не найдена")

def last_5_books():
    
    if not books:
        print("Дневник пуст.")
    else:
        print("Последние 5 книг:")
        last_books = books[-5:]
        for i in range(len(last_books)):
            print(f"{i + 1}. {last_books[i]}")

def show_statistics():
   
    if not books:
        print("Дневник пуст.")
    else:
        print(f"Всего прочитано книг: {len(books)}")
        print(f"Первая книга: {books[0]}")
        print(f"Последняя книга: {books[-1]}")
while True:
    show_menu()
    choice = input("Выберите пункт меню: ").strip()

    if choice == "1":
        add_books()
    elif choice == "2":
        show_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        mark_book()
    elif choice == "5":
        last_5_books()
    elif choice == "6":
        show_statistics()
    elif choice == "0":
        print("Выход. До свидания!")
        break
    else:
        print("Ошибка: такого пункта меню нет.")