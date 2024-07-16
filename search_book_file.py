def search_book(book_list):
    print("Enter 1 for search by book Title or ISBN")
    print("Enter 2 for search by Author name.") 
    choice = input("Enter your choice: ")
    match choice:
        case "1":
            search_term = input("Enter the book Title or ISBN: ")
            for book in book_list:
                if search_term.lower() in book['title'].lower() or search_term in book['isbn']:
                    print(f"Found- {book['title']}-{book['author']}-{book['isbn']}-{book['publishing_year']}-{book['price']}-{book['quantity']}")
        case "2":
            search_term = input("Enter the author name: ")
            for book in book_list:
                if search_term.lower() in book['author'].lower():
                    print(f"Found- {book['title']}-{book['author']}-{book['isbn']}-{book['publishing_year']}-{book['price']}-{book['quantity']}")
        
       