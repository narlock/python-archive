#CGI script that will process a book
#Author: Anthony Narlock
#Date: 12/1/2020
#Prof: Lisa Minogue
#Class: CSCI 2061.70

import cgi

def main():
    #Gets information from the form
    form = cgi.FieldStorage()

    #Initializations
    title = form.getvalue('title')
    author = form.getvalue('author')
    year_published = form.getvalue('year_published')
    pages = form.getvalue('pages')
    genre = form.getvalue('genre')

    #HTML:
    print("Content-Type: text/html")
    print()
    print("<doctype html><head><title>Book saved!</title></head>")

    #Input validation for form inputs
    try:
        #Pages and year must be an integer
        val = int(pages)
        val = int(year_published)
        #The title and author must exist
        if not title or not author:
            raise TypeError
    except ValueError:
        print("<h1>External Error: year and pages were entered incorrectly</h1>")
        print("<a href=\"/saveForm.html\">Enter Another Book</a> or")
        print("<a href=\"/cgi-bin/list_books.py\">List Books</a>")
        return
    except TypeError:
        print("<h1>External Error: All parts of the form must be completed</h1>")
        print("<a href=\"/saveForm.html\">Enter Another Book</a> or")
        print("<a href=\"/cgi-bin/list_books.py\">List Books</a>")
        return

    #Displays book to the page
    print("<body><h1>Book Saved Successfully:</h1><br>")
    print("<h2> {} by: {}</h2><br><br>".format(title,author))
    print("<p><b>Book Information:</b></p><br>")
    print("<p>Year Published: {}</p><br>".format(year_published))
    print("<p>Number of Pages: {}</p><br>".format(pages))
    print("<p>Genre: {}</p><br>".format(genre))
    print("<a href=\"/saveForm.html\">Enter Another Book</a> or")
    print("<a href=\"/cgi-bin/list_books.py\">List Books</a>")
    print("</body></html>")

    #Adds book to file
    try:
        book = {"title": title, "author": author, "year": year_published, "pages": pages, "genre": genre}
        file = open("book_list.txt","a+")
        file.write(str(book) + "\n")
        file.close()
    except:
        return


if __name__ == '__main__':
    main()
