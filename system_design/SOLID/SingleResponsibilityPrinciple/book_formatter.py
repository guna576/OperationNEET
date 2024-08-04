from book import Book

class BookFormatter:
    def format_details(self, book1: Book):
        return f"Title: {book1.get_title()}, Author: {book1.get_author()}, Price: ${book1.get_price()}"
    

