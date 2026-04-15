from book import Book
import json
import os

#管理图书类 / Library management class
class Library(object):
    def __init__(self, data_file="library_data.json"):
        self.books = []
        self.borrow_records = []
        self.data_file = data_file
        self.load_data()
        
    def add_book(self, book):
        self.books.append(book)
        self.save_data()
        return f"Book added: {book.name}"

    def find_book_by_id(self, book_id):
        for book in self.books:
            if book_id == book.book_id:
                return book
        return None
    
    def find_books_by_name(self, name):
        result = []
        for book in self.books:
            if name.lower() in book.name.lower():
                result.append(book)
        return result
    
    def find_books_by_author(self, author):
        result = []
        for book in self.books:
            if author.lower() in book.author.lower():
                result.append(book)
        return result
    
    def find_books_by_category(self, category):
        result = []
        for book in self.books:
            if category.lower() in book.category.lower():
                result.append(book)
        return result
    
    def delete_book(self, book_id):
        book = self.find_book_by_id(book_id)
        if book:
            self.books.remove(book)
            self.save_data()
            return f"Book deleted: {book.name}"
        else:
            return f"Delete unsuccessful: Book ID {book_id} not found"
    
    def borrow_book(self, book_id, borrower_name):
        book = self.find_book_by_id(book_id)
        if book:
            if book.status == 1:
                book.status = 0
                # 添加借阅记录 / Add borrow record
                import datetime
                record = {
                    'book_id': book_id,
                    'book_name': book.name,
                    'borrower': borrower_name,
                    'borrow_date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'return_date': None
                }
                self.borrow_records.append(record)
                self.save_data()
                return f"Borrow successful: {book.name}"
            else:
                return f"Borrow unsuccessful: {book.name} is already on loan"
        else:
            return f"Borrow unsuccessful: Book ID {book_id} not found"
        
    def return_book(self, book_id):
        book = self.find_book_by_id(book_id)
        if book:
            if book.status == 0:
                book.status = 1
                # 更新借阅记录 / Update borrow record
                for record in self.borrow_records:
                    if record['book_id'] == book_id and record['return_date'] is None:
                        import datetime
                        record['return_date'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        break
                self.save_data()
                return f"Return successful: {book.name}"
            else:
                return f"Return unsuccessful: {book.name} is not on loan"
        else:
            return f"Return unsuccessful: Book ID {book_id} not found"
        
    def list_all_book(self):
        return self.books
    
    def get_book_statistics(self):
        total_books = len(self.books)
        available_books = sum(1 for book in self.books if book.status == 1)
        borrowed_books = sum(1 for book in self.books if book.status == 0)
        
        # 按分类统计 / Statistics by category
        category_stats = {}
        for book in self.books:
            if book.category not in category_stats:
                category_stats[book.category] = {'total': 0, 'available': 0, 'borrowed': 0}
            category_stats[book.category]['total'] += 1
            if book.status == 1:
                category_stats[book.category]['available'] += 1
            else:
                category_stats[book.category]['borrowed'] += 1
        
        return {
            'total_books': total_books,
            'available_books': available_books,
            'borrowed_books': borrowed_books,
            'category_stats': category_stats
        }
    
    def get_borrow_records(self):
        return self.borrow_records
    
    def save_data(self):
        data = {
            'books': [book.to_dict() for book in self.books],
            'borrow_records': self.borrow_records
        }
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def load_data(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.books = [Book.from_dict(book_data) for book_data in data.get('books', [])]
                    self.borrow_records = data.get('borrow_records', [])
            except Exception as e:
                print(f"Error loading data: {e}")
        # 如果没有数据文件，添加一些初始图书 / If no data file, add some initial books
        if not self.books:
            self.add_book(Book(1, "Python Programming", "Jack", "Computer Science", 1))
            self.add_book(Book(2, "Data Structures", "Li", "Computer Science", 1))
            self.add_book(Book(3, "Algorithms", "He", "Computer Science", 1))
            self.add_book(Book(4, "Introduction to Physics", "Smith", "Science", 1))
            self.add_book(Book(5, "World History", "Johnson", "History", 1))

