def load_lender_from_csv(lender_list):
    lender_list.clear()
    with open("lender.csv", "rt+") as file:
        for line in file.readlines():
            line_splited = line.strip().split(",")

            lender = {
                'name' : line_splited[0],
                'number' : line_splited[1],
                'book' : line_splited[2],
                'author' : line_splited[3],
                'isbn' : line_splited[4],
                'publishing_year' : line_splited[5],

            }
            lender_list.append(lender)
    return lender_list