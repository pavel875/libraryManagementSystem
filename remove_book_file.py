
def remove_book(book_list):
    print("Enter 1 for search by book Title to Delete.")
    print("Enter 2 for search by Author name to Delete.")
    print("Enter 3 for search by ISBN number to Delete.")
    choice = input("Enter your choice: ")
    match choice:

        case "1":
            search_term = input("Enter the book Title: ")
            for index,book in enumerate(book_list):
                if search_term.lower() in book['title'].lower():
                    print(f"{index+1}. {book['title']}-{book['author']}-{book['isbn']}-{book['publishing_year']}-{book['price']}-{book['quantity']}")
            selected_index = input("Enter the index number of the item to remove: ")
            selected_index = int(selected_index)
            book_list.pop(selected_index-1)
            print("Book removed successfully")
            with open("books.csv", "w") as file_pointer:
                line = f"{book['title']},{book['author']},{book['isbn']},{book['publishing_year']},{book['price']},{book['quantity']}\n"
                file_pointer.write(line)

            return book_list

        case "2":
            search_term = input("Enter the author name: ")
            for index,book in enumerate(book_list):
                if search_term.lower() in book['author'].lower():
                    print(f"{index+1}. {book['title']}-{book['author']}-{book['isbn']}-{book['publishing_year']}-{book['price']}-{book['quantity']}")
            selected_index = input("Enter the index number of the item to remove: ")
            selected_index = int(selected_index)
            book_list.pop(selected_index-1)
            print("Book removed successfully")
            return book_list

        case "3":
            search_term = input("Enter the ISBN number: ")
            for index,book in enumerate(book_list):
                if search_term in book['isbn']:
                    print(f"{index+1}. {book['title']}-{book['author']}-{book['isbn']}-{book['publishing_year']}-{book['price']}-{book['quantity']}")
            selected_index = input("Enter the index number of the item to remove: ")
            selected_index = int(selected_index)
            book_list.pop(selected_index-1)
            print("Book removed successfully")
            return book_list
        







        