# Import all the Functions
import add_book_file
import view_all_book_file
import load_book_from_csv_file
import search_book_file
import remove_book_file
import lend_book_file
import load_lender_from_csv_file
import view_lender_list_file
import return_book_file

# Initialize the list
book_list = [] 
lender_list = []


# Main Program 
print("Welcome to the library!")
book_list = load_book_from_csv_file.load_books_from_csv(book_list)              #Loading all data from CSV file
lender_list = load_lender_from_csv_file.load_lender_from_csv(lender_list)       #Loading all data from CSV file

menu = """
Your options:
1. Add a book
2. View all book
3. Search book
4. Remove book
5. Lend book
6. See all lender
7. Return book
0. Exit
"""

while True:
    print(menu)
    choice = input("Enter Your Choice: ")
    if choice == "1":
        book_list = add_book_file.add_book(book_list)       #User can add book from here
    elif choice == "2":
        view_all_book_file.view_all_book(book_list)         #User can see all book here
    elif choice == "3":
        search_book_file.search_book(book_list)             #User can search any book here
    elif choice == "4":
        book_list = remove_book_file.remove_book(book_list) #User can remove any book here
    elif choice == "5":
        book_list,lender_list = lend_book_file.lend_book(book_list,lender_list)  #User can lend any book here
    elif choice == "6":
        view_lender_list_file.view_lender_list(lender_list)        #User can see who lend the book here
    elif choice == "7":
        book_list,lender_list = return_book_file.return_book(book_list,lender_list) #user can give back the book that he lend
    elif choice == "0":
        break
    else:
        print("\n Enter the correct key.")


 



