
from member import Member 
from Library import Library
from Book import LibraryException

class System(Library,Member):
    def __init__(self):
        super().__init__() 
        self.__members = []

    def get_members(self):
        return self.__members
    
    def Register_new_account(self, name, barcode):
        member = Member(name, barcode)
        self.__members.append(member)
        print(f"Member {member.get_name()} has been added.")

    def delete_member(self, member):
        if member in self.__members:
            self.__members.remove(member)
            print(f"Member {member.get_name()} has been deleted.")
        else:
            raise MemberNotFound()

    def search_catalog(self, search_type, value):
        return super.search_book( search_type, value)

    def Add_Book(self,book):
        super.add_book_to_catalog(book)

    def Remove_Book(self,book):
        super.delete_book_from_catalog(book)

    def Modify_book(self,book,key,modification):
        super.modify_book_from_catalog(book,key,modification)

    def Check_out_book(self,book,member):
        super.checked_out_book(book,member)

    def Reserve_book(self,book,member):
        super.reserve_book(book,member)

    def Return_book(self,book,member):
        super.return_book(book,member)

    def Renew_book(self,book,member):
        self.return_book(book,member)
        self.checked_out_book(book,member)

class MemberNotFound(LibraryException):
    def __init__(self):
        self.message = "member not found"
        super().__init__(self.message)
