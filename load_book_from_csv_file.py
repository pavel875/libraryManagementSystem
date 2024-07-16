def load_books_from_csv(book_list):
    book_list.clear()
    with open("books.csv","rt+") as file_pointer:
        for line in file_pointer.readlines():
            line_splited = line.strip().split(",")
            book = {
                "title": line_splited[0],
                "author" : line_splited[1],
                "isbn" : line_splited[2],
                "publishing_year" :line_splited[3],
                "price" : line_splited[4],
                "quantity" : line_splited[5],
            }
            book_list.append(book)
    return book_list