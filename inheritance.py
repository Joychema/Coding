#library management system

#parent class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def displayinfo(self):
        return f"Title: {self.title}, Author: {self.author}"
#child class/derived class
class LibraryBook(Book):
    def __init__(self,title,author,isbn,copies_available):
        super().__init__(title,author)
        self.isbn = isbn
        self.copies_available = copies_available
    def borrow_book(self):
        if self.copies_available > 0:
            self.copies_available -= 1
            return f"{self.title} borrowed, copies left {self.copies_available}"
        else:
            return f"{self.title} not available"
    def return_book(self):
        self.copies_available +=1
        return f"{self.title} returned. Copies left {self.copies_available}"

book1=LibraryBook("The River and the Source","Marie Ongola","23465789872",10)
print(book1.displayinfo())
print(book1.borrow_book())
print(book1.return_book())
