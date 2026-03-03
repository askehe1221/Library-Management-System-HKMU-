from book import Book
  
#管理图书类
class Library(object):
    def __init__(self):
        self.books =[]
    def add_book(self,book):
        self.books.append(book)
        print(f"Book added:{book.name}")

    def find_book_by_id(self,book_id):
        for book in self.books:
            if book_id == book.book_id:
                return book
        return None
    
    def borrow_book(self,book_id):
        book = self.find_book_by_id(book_id)
        if book:
            if book.status == 1:
                book.status = 0
                print(f"Borrow Sucessful:{book.name}")
                return True
            else:
                print(f"Borrow Unsucessful:{book.name}")
                return False
        else:
            print(f"Borrow Unsucessful the id  {book_id} is not found")
            return False
        
    def return_book(self,book_id):
        book=self.find_book_by_id(book_id)
        if book:
            if book.status == 0:
                book.status=1
                print(f"Return Sucessful:{book.name}")
                return True
            else:
                print(f"Return Unsucessful:{book.name}")
        else:
            print(f"Retuen Unsucessful id {book_id}is not found")
        
    def list_all_book(self):
        print("All BOOKS")
        for book in self.books:
            print(book)


    
