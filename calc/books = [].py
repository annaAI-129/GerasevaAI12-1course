def show_menu():
 while True:
    print("\n===+ ЧИТАТЕЛЬСКИЙ ДНЕВНИК +===")
    print("1 - добавить книгу")
    print("2 - показать все книги")
    print("3 - показать последние 5 прочитанных")
    print("4 - Заменить название по номеру")
    print("5 - Поиск по названию")
    print("6 - Статистика")
    print("0 - Выход")

    choice = input("Выберите пункт меню: ").strip()

   
    if not choice.isdigit():
        print("Ошибка: введите номер пункта цифрами.")
        continue

    if choice == "0":
        print("Выход. до свидания!")
        break

   
    elif choice == "1":
        title = input("Введите название книги: ").strip()
        if not title: 
            print("Ошибка: название не может быть пустым.")
        else:
            books.append(title)

   
    elif choice == "2":
        if not books:  
            print("Преступление и наказание")
            print("Война и мир")
            print("Алхимик")
            print("Анна Каренина")
            print("Сто лет одиночества")
            print("Тихий Дон")
            print("Гари потер")
            print("Рапунцль")
        else:
            for i in range(len(books)):
                print(f"{i + 1}. {books[i]}")

    
    elif choice == "3":
        if not books:
            print("Дневник пуст")
        else:
            
            last_books = books[-5:]
            
            start_number = len(books) - len(last_books) + 1
            
            for i in range(len(last_books)):
                
                print(f"{start_number + i}. {last_books[i]}")

    
    elif choice == "4":
        num_str = input("Введите номер книги для замены: ").strip()
        
        
        if not num_str.isdigit():
            print("Ошибка: номер должен быть положительным целым числом.")
            continue
            
        num = int(num_str)
        
        
        if num < 1 or num > len(books):
            print("Ошибка: книги с таким номером нет.")
            continue
            
        new_title = input("Введите новое название: ").strip()
        if not new_title:
            print("Ошибка: название не может быть пустым.")
        else:
            books[num - 1] = new_title  

    
    elif choice == "5":
        if not books:
            print("Преступление и наказание")
            print("Война и мир")
            print("Алхимик")
            print("Анна Каренина")
            print("Сто лет одиночества")

        else:
            query = input("Введите слово или часть названия: ").strip().lower()
            found = False
            
            for i in range(len(books)):
                
                if query in books[i].lower():
                    print(f"{i + 1}. {books[i]}")
                    found = True
                    
            if not found:
                print("Ничего не найдено")

    
    elif choice == "6":
        if not books:
            print("Дневник пуст")
        else:
            print(f"Всего прочитано книг: {len(books)}")
            print(f"Первая книга: {books[0]}")
            print(f"Последняя книга: {books[-1]}")

    else:
        print("Ошибка: такого пункта меню нет.")