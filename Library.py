from Book import Book,BookAlreadyCheckedOutException,BookAlreadyReservedException,BookNotCheckedOutException,LibraryException

class Library():
    def __init__(self):
        self.__catalog = []
        self.__checked_out_books =[]

    def add_book_to_catalog(self, book):
        if isinstance(book, Book):  
            self.__catalog.append(book)
        else:
            raise InvalidBookObjectError()
        
    def delete_book_from_catalog(self, book):
        if book in self.__catalog:
            self.__catalog.remove(book)
            print(f"book {book.get_item_id()} has been deleted.")
        elif book in self.__checked_out_books:
            self.__checked_out_books.remove(book)
            print(f"book {book.get_item_id()} has been deleted.")
        else:
            raise BookNotFoundException()
        
    def modify_book_from_catalog(self,book1,key,modification):
        for book in self.__catalog:
            if book1.get_item_id() == book.get_item_id(): 
                book1.modify(key, modification)
                return  
        raise BookNotFoundException()



    def overdue_books(self):
        for book in self.__checked_out_books:
            if book.is_overdue():
                 print(f"Book '{book.get_item_id()}' is overdue. Due date: {book.due_date}. Member: {book.get_checked_out_by().get_name()}")
   
    def print_checked_out_books(self):
        if not self.__checked_out_books:  
            print("There are no currently checked-out books.")
            return
        print("Currently Checked Out Books:")
        for book in self.__checked_out_books:
            print(f"  - Title: {book.get_title()}")  
            print(f"    Author: {book.get_author()}")  
            print(f"    Member: {book.get_checked_out_by().get_name()}")  
            print()  

    def checked_out_book(self,book1,member):
        for book in self.__catalog:
            if book1.get_item_id() == book.get_item_id():
                try:
                    book1.issue(member)
                    self.__catalog.remove(book1) 
                    self.__checked_out_books.append(book1)  
                    book1.send_notification(member)
                    return
                except  BookAlreadyCheckedOutException :
                     raise BookAlreadyCheckedOutException()
        raise BookNotFoundException()

    def reserve_book(self,book1,member):
        for book in self.__catalog:
            if book1.get_item_id() ==  book.get_item_id():
                try:
                    book1.reserve(member)
                    return
                except BookAlreadyReservedException :
                    raise BookAlreadyReservedException() 
        raise BookNotFoundException()

    def return_book(self,book1,member):
        for book in self.__catalog:
            if book1.get_item_id() ==  book.get_item_id():
                try:
                    book1.return_item()
                    self.__checked_out_books.remove(book1)
                    self.__catalog.append(book1)
                    if not book.is_overdue():
                        print("Just pay $10")
                    else:
                        print("You need to pay $10 + $5 for being late")
                    return
                except BookNotCheckedOutException :
                    raise BookNotCheckedOutException()   
        raise BookNotFoundException()

    def search_book(self, search_type, value):
        found_books = []
        if search_type == "title":
            for book in self.__catalog:
                if book.get_title() == value:
                    found_books.append(book)
        elif search_type == "author":
            for book in self.__catalog:
                if book.get_author() == value:
                    found_books.append(book)
        elif search_type == "subject":
            for book in self.__catalog:
                if book.get_subject() == value:
                    found_books.append(book)
        elif search_type == "publication_date":
            for book in self.__catalog:
                if book.get_publication_date() == value:
                    found_books.append(book)
        return found_books

class BookNotFoundException(LibraryException):
    def __init__(self):
        self.message = "Book not found."
        super().__init__(self.message)


class InvalidBookObjectError(LibraryException):
    def __init__(self):
        self.message = "Invalid book object. Please provide a Book instance."
        super().__init__(self.message)    
