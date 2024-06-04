class Book:
    def __init__(self, title, author,copies):
        self.title = title
        self.author = author 
        self.copies = copies

    def borrow(self):
        if self.copies > 0:
            self.copies -= 1
            print(f"Borrowed one copy of {self.title}. Copies left: {self.copies}")
        else: 
            print(f"No copies of {self.title} left")

    def return_book(self):
        self.copies + 1
        print(f"Returned one copy of {self.title}. Total copies: {self.copies}") 
    
    def __str__(self):
        return f"Title: {self.title}, author: {self.author}, copies: {self.copies}"
    
new_book = Book("1984", "George Orwell", 5)
new_book1 = Book("suicide", "Berntsen", 3)
new_book.borrow()
new_book.borrow()
new_book.return_book()
print(new_book1)
print(new_book)







