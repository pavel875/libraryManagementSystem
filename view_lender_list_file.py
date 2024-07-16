def view_lender_list(lender_list):
    if not lender_list:
        print("No book lended at this time.")
    else:
        for index,lender in enumerate(lender_list):
            print(f"{index+1}. Name : {lender['name']} || Number : {lender['number']} || Book : {lender['book']} || Author : {lender['author']} || ISBN : {lender['isbn']} || Published Year : {lender['publishing_year']}")