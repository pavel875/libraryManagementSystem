def lend_book(book_list,lender_list):
    print("Enter 1 for search book by Title to lend.")
    print("Enter 2 for search Author by name to lend.")
    choice = input("Enter your choice: ")
    flag = False
    match choice:

        case "1":
            search_term = input("Enter the book Title: ")
            for index,book in enumerate(book_list):
                if search_term.lower() in book['title'].lower():
                    flag = True
                    print(f"{index+1}. {book['title']}-{book['author']}-{book['isbn']}-{book['publishing_year']}-{book['price']}-{book['quantity']}")
            if flag != False:
                selected_index = input("Enter the index number of the book to lend: ")
                selected_index = int(selected_index)
                decrese = int(book_list[selected_index-1]['quantity'])
                if decrese>0:
                    lender_name = input("Enter the lender name:")
                    lndr_number = input("Enter the number of lender: ")
                    lender_book = book_list[selected_index-1]['title']
                    lender_book_autor = book_list[selected_index-1]['author']
                    lender_book_isbn= book_list[selected_index-1]['isbn']
                    lender_book_publishingYear = book_list[selected_index-1]['publishing_year']
                    lender ={
                        'name' : lender_name,
                        'number':lndr_number,
                        'book' : lender_book,
                        'author':lender_book_autor,
                        'isbn' : lender_book_isbn,
                        'publishing_year':lender_book_publishingYear,
                    }
                    lender_list.append(lender)
                    with open("lender.csv",'a') as fp:
                        line = f"{lender['name']},{lender['number']},{lender['book']},{lender['author']},{lender['isbn']},{lender['publishing_year']}\n"
                        fp.write(line)
                    decrese -=1
                    book_list[selected_index-1]['quantity'] = decrese
                    print("\nBook lended")
                else:
                    print("Not enough Books available to lend")
                
            else:
                print("No book Found")
            return book_list,lender_list
            
        case "2":
            search_term = input("Enter the author name: ")
            for index,book in enumerate(book_list):
                if search_term.lower() in book['author'].lower():
                    flag = True
                    print(f"{index+1}. {book['title']}-{book['author']}-{book['isbn']}-{book['publishing_year']}-{book['price']}-{book['quantity']}")
            if flag != False:
                selected_index = input("Enter the index number of the book to lend: ")
                selected_index = int(selected_index)
                decrese = int(book_list[selected_index-1]['quantity'])
                if decrese>0:
                    lender_name = input("Enter the lender name:")
                    lndr_number = input("Enter the number of lender: ")
                    lender_book = book_list[selected_index-1]['title']
                    lender_book_autor = book_list[selected_index-1]['author']
                    lender_book_isbn= book_list[selected_index-1]['isbn']
                    lender_book_publishingYear = book_list[selected_index-1]['publishing_year']
                    lnder ={
                        'name' : lender_name,
                        'number':lndr_number,
                        'book' : lender_book,
                        'author':lender_book_autor,
                        'isbn' : lender_book_isbn,
                        'publishing_year':lender_book_publishingYear,
                    }
                    lender_list.append(lnder)
                    with open("lender.csv",'a') as fp:
                        line = f"{lender['name']},{lender['number']},{lender['book']},{lender['author']},{lender['isbn']},{lender['publishing_year']}\n"
                        fp.write(line)
                    decrese -=1
                    book_list[selected_index-1]['quantity'] = decrese
                    print("\nBook lended")
                else:
                    print("Not enough Books available to lend")                
            else:
                print("No book Found")
            return book_list,lender_list
