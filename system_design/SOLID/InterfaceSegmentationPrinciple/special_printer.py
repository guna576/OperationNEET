from printer import Printer
from scanner import Scanner
from fax import Fax

class SpecialPrinter(Printer, Scanner, Fax):

    def print(self):
        return super().print()
    
    def scan(self):
        return super().scan()
    
    def fax_doc(self):
        return super().fax_doc()