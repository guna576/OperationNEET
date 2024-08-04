from book import Book
from book_formatter import BookFormatter
from price_calculator import PriceCalculator

def main():
    book = Book("The Great Gatsby", "F. Scott Fitzgerald", 20.0)
    print(book.get_author())
    formatter = BookFormatter()
    print(formatter.format_details(book))

    calculator = PriceCalculator()
    calculator.apply_discount(book, 10)
    print(formatter.format_details(book))

main()