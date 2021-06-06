#CGI script that displays list of books from file
#Author: Anthony Narlock
#Date: 12/1/2020
#Prof: Lisa Minogue
#Class: CSCI 2061.70

import cgi

def main():
    #HTML:
    print("Content-Type: text/html")
    print()
    print("<doctype html><head><title>Book List</title></head>")

    #Reads books from the file
    try:
        file = open("book_list.txt","r")
        books = file.readlines()
        file.close()
    except:
        print("<h1>External Error: Unable to read file, file may not exist</h1>")
        print("<a href=\"/saveForm.html\">Enter Another Book</a> or")
        print("<a href=\"/cgi-bin/list_books.py\">List Books</a>")
        return

    print("<body><h1>Book List</h1>")

    #Prints the books:
    for book in books:
        print("<p>{}</p>".format(book))

    print("<a href=\"/saveForm.html\">Enter Another Book</a> or")
    print("<a href=\"/cgi-bin/list_books.py\">List Books</a>")
    print("</body></html>")

if __name__ == "__main__":
    main()
