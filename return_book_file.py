def return_book(book_list,lender_list):
    returner_name = input("Enter name to match with lender:")
    returner_number = input("Enter number to match with lender:")
    lended_book_title = input("Enter the title of the book you want to return: ")
    lended_book_author = input("Enter the author of the book you want to return: ")
    lended_book_isbn = input("Enter the ISBN no of the book you want to return: ")

    for outer_index,book in enumerate(lender_list):
        if book['name'] in returner_name and book['number'] in returner_number and book['book'] in lended_book_title and book['author'] in lended_book_author and book['isbn'] in lended_book_isbn:
            for index,bk_list in enumerate(book_list):
                if book['book'] in bk_list['title'] and book['isbn'] in bk_list['isbn']:
                    increse_book = int(book_list[index]['quantity'])
                    increse_book += 1
                    lender_list.pop(outer_index)
                    book_list[index]['quantity'] = increse_book
                    print("Book collected from lender successfully")
                    return book_list,lender_list

