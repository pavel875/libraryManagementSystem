def view_all_book(book_list):
    
    if not book_list:
        print("There is no book.")
    else:
        for book in book_list:
            print(f"Book Name: {book['title']} ||Author: {book['author']} ||ISBN: {book['isbn']} ||Publishing Year: {book['publishing_year']} ||Price: {book['price']} ||Quantity: {book['quantity']}\n"
              )