def add_book(book_list):
    print("Note down here all the information of the book that you want to add.\n")
    title = input("Enter the title of the book: ")
    author = input("Enter the author name: ")
    isbn = input("Enter the ISBN number : ")
    publishing_year = input("Enter the publishing year: ")
    price = input("Enter the price of the book: ")
    quantity = input("Enter the quantity of the book: ")

    book = {
        'title' : title,
        'author' : author,
        'isbn' : isbn,
        'publishing_year' : publishing_year,
        'price' : price,
        'quantity' : quantity,
    }
    book_list.append(book)
    with open("books.csv", "at+") as file_pointer:
        line = f"{book['title']},{book['author']},{book['isbn']},{book['publishing_year']},{book['price']},{book['quantity']}\n"
        file_pointer.write(line)
    print("Book added successfully")
    return book_list