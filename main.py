from System import System 
from Book import Book
from member import Member 
from Library import Library

def main():
    # Create a library
    library = Library()

    # Add some books to the library catalog
    book1 = Book(101, 10001, "Introduction to Python", "John Smith", "Programming", "2022-01-01", "A101")
    book2 = Book(102, 10002, "Data Structures and Algorithms", "Alice Johnson", "Computer Science", "2022-01-15", "B102")
    library.add_book_to_catalog(book1)
    library.add_book_to_catalog(book2)

    # Create some members
    member1 = Member(1, "Alice", 20001)
    member2 = Member(2, "Bob", 20002)

    # Issue some books to members
    member1.issue_item(book1)
    member2.issue_item(book2)

    # Print overdue books
    library.overdue_books()

    # Print checked out books
    library.print_checked_out_books()

    # Return books
    member1.return_item(book1)
    member2.return_item(book2)

    # Search the catalog
    found_books = library.search_book("title", "Introduction to Python")
    print("Found Books:")
    for book in found_books:
        print(book.title)

    # Test System class
    system = System(library)
    system.Register_new_account("Charlie", 20003)
    system.Check_out_book(book1, member1)
    system.Reserve_book(book2, member2)

if __name__ == "__main__":
    main()
