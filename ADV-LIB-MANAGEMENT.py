library = []

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    book_id = input("Enter book ID: ")
    
    book = {
        "title": title,
        "author": author,
        "id": book_id,
        "available": True
    }
    
    library.append(book)
    print("Book added successfully!\n")

def view_books():
    if not library:
        print("No books in library\n")
        return
    
    for book in library:
        status = "Available" if book["available"] else "Issued"
        print(book["id"], "-", book["title"], "-", status)
    print()

def search_book():
    search = input("Enter title or author: ")
    for book in library:
        if search.lower() in book["title"].lower() or search.lower() in book["author"].lower():
            print("Found:", book["title"], "-", book["author"])
            return
    print("Book not found\n")

def issue_book():
    book_id = input("Enter book ID: ")
    for book in library:
        if book["id"] == book_id:
            if book["available"]:
                book["available"] = False
                print("Book issued successfully\n")
            else:
                print("Book already issued\n")
            return
    print("Book not found\n")

def return_book():
    book_id = input("Enter book ID: ")
    days = int(input("Enter days late: "))
    
    for book in library:
        if book["id"] == book_id:
            book["available"] = True
            fine = days * 2  # ₹2 per day
            print("Book returned. Fine =", fine, "\n")
            return
    print("Book not found\n")

while True:
    print("1.Add Book  2.View  3.Search  4.Issue  5.Return  6.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        issue_book()
    elif choice == "5":
        return_book()
    elif choice == "6":
        break
    else:
        print("Invalid choice\n")
