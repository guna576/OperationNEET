from book import Book 


class PriceCalculator:
    def apply_discount(self, book: Book, discounted_percentage: float):
        book.price *= (1-discounted_percentage)/100

