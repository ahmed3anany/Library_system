
from datetime import datetime, timedelta
from member import Member
from Library import Library

class BookItem():
    time = 0
    def __init__(self, barcode):
        self.__barcode = barcode
       
    def barcode(self):
        return self.__barcode
    
    
class Book(BookItem):
    def __init__(self, item_id, barcode , title, author, subject, publication_date, rack_number):
        super().__init__( barcode)
        self.__item_id = item_id
        self.__title = title
        self.__author = author
        self.__subject = subject
        self.__publication_date = publication_date
        self.__rack_number = rack_number
        self.__is_reserved = False
        self.__is_reserved_by = None
        self.__is_checked_out = False
        self.__checked_out_by = None
        self.due_date = None

    def item_id(self):
        return self.__item_id    
    
    def title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_subject(self):
        return self.__subject
    
    def get_publication_date(self):
        return self.__publication_date

    def get_rack_number(self):
        return self.__rack_number
    
    def get_is_reserved_by(self):
        return self.__is_reserved_by
    
    def get_checked_out_by (self):
        return self.__checked_out_by 
    
    def issue(self, member):
        if self.__is_checked_out:
            if not self.__is_reserved:
               print("you can reserve it.") 
               return False
            raise BookAlreadyCheckedOutException()
        elif not self.__is_reserved:
            self.__is_checked_out = True
            self.__checked_out_by = member
            self.due_date = datetime.now() + timedelta(days=10)  # Due in 10 days
            self.time = datetime.now()
        else:
            raise BookAlreadyReservedException()
        
    def send_notification(self, member):
        if self.is_overdue():
            print(f"Notification: Book '{self.get_title()}' is overdue. Member: {member.get_name()}") 

    def is_overdue(self):
        if self.due_date >= self.time + 10:
           return True
        return False
    
    def reserve(self,member):
        if self.__is_reserved :
            raise BookAlreadyReservedException()
        self.__is_reserved = True
        self.__is_reserved_by = member
        return True
    
    def return_item(self):
        if not self.is_checked_out:
             raise BookNotCheckedOutException()
        self.__is_checked_out = False
        self.__checked_out_by = None
        self.due_date = None
        return True
    
    def modify(self,key,modification):
        if key == "title":
            self.__title = modification
        elif key == "author":
            self.__title = modification
        elif key == "subject":
            self.__title = modification
        elif key == "publication_date":
           self.__title = modification

class LibraryException(Exception):
    pass

class BookAlreadyCheckedOutException(LibraryException):
    def __init__(self):
        self.message = "The book is already checked out."
        super().__init__(self.message)

class BookAlreadyReservedException(LibraryException):
    def __init__(self):
        self.message = "This book is already reserved."
        super().__init__(self.message)


class BookNotCheckedOutException(LibraryException):
    def __init__(self):
        self.message = "Book is not checked out."
        super().__init__(self.message)