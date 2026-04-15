from library import Library
from book import Book

class LibraryMenu:
    def __init__(self):
        self.library = Library()
        # Add some books
        self.library.add_book(Book(1, "Python1", "Jack", 1))
        self.library.add_book(Book(2, "Python2", "Li", 1))
        self.library.add_book(Book(3, "Python3", "HE", 1))

    def show_menu(self):
        print("\n" + "="*40)
        print("       Library Management System")
        print("="*40)
        print("1. Add books")
        print("2. Borrow books")
        print("3. Retuen books")
        print("4. Check all the books")
        print("5. Find books by id")
        print("6. Exit System")
        print("="*40)

    def get_user_choice(self):
        while True:
            try:
                choice = int(input("Input numbers (1-6): "))
                if 1 <= choice <= 6:
                    return choice
                else:
                    print("Invaild numbers,Please enter the numbers between 1~6.")
            except ValueError:
                print("Invaild numbers,Please enter numbers.")

    def add_book_menu(self):
        print("\n--- Add Books ---")
        try:
            book_id = int(input("Please enter book ID: "))
            name = input("Please enter book name: ")
            author = input("Please enter the author: ")
            new_book = Book(book_id, name, author, 1)
            self.library.add_book(new_book)
        except ValueError:
            print("Input error,Book ID must be number.")

    def borrow_book_menu(self):
        print("\n--- Borrow Books ---")
        try:
            book_id = int(input("Enter ID: "))
            self.library.borrow_book(book_id)
        except ValueError:
            print("Input error,Book ID must be number.")

    def return_book_menu(self):
        print("\n--- Return Books ---")
        try:
            book_id = int(input("Enter ID: "))
            self.library.return_book(book_id)
        except ValueError:
            print("Input error,Book ID must be number.")

    def find_book_menu(self):
        print("\n--- Search Book ---")
        try:
            book_id = int(input("Enter ID: "))
            book = self.library.find_book_by_id(book_id)
            if book:
                print("Find:")
                print(book)
            else:
                print(f"The id {book_id}  is not found.")
        except ValueError:
            print("Input error,Book ID must be number.")

    def run(self):
        while True:
            self.show_menu()
            choice = self.get_user_choice()

            if choice == 1:
                self.add_book_menu()
            elif choice == 2:
                self.borrow_book_menu()
            elif choice == 3:
                self.return_book_menu()
            elif choice == 4:
                self.library.list_all_book()
            elif choice == 5:
                self.find_book_menu()
            elif choice == 6:
                print("Thank for your using!!!")
                break

            input("\nEnter enter to continue...")

