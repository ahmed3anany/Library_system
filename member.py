from Book import Book,LibraryException
from member import Member 
from Library import Library

class LibraryMember():
    def __init__(self,barcode):
        self.__barcode = barcode

    def get_barcode(self):
        return self.__barcode
    

class Member(LibraryMember,Library):
    __MAX_BOOKS_ISSUED = 5
    __MAX_DAYS_ALLOWED = 10

    def __init__(self, member_id, name, barcode):
        super().__init__(barcode) 
        self.__member_id = member_id
        self.__name = name
        self.__books_issued = []
        
    def get_name(self):
        return self.__name
    def get_member_id(self):
        return self.__member_id

    def issue_item(self, book):
        if len(self.__books_issued) >= self.__MAX_BOOKS_ISSUED:
            raise MaxBooksIssuedException()
        Library.__books_issued.append(book)
        Library.__checked_out_book(book,self)
        return True

    def return_item(self, book):
        if book in self.__books_issued:
            try:
                Library.return_book(book, self)
                self.__books_issued.remove(book)
                return True
            except Exception:  
                raise LibraryOperationError()

        else:
            raise BookNotIssuedException()
        
class MaxBooksIssuedException(LibraryException):
    def __init__(self):
        self.message = "Maximum limit reached. Cannot issue more items."
        super().__init__(self.message)


class BookNotIssuedException(LibraryException):
    def __init__(self):
        self.message = "Item not issued to this member. Cannot return."
        super().__init__(self.message)


class LibraryOperationError(LibraryException):
    def __init__(self):
        self.message = f"An error occurred while returning the book"
        super().__init__(self.message)