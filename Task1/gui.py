import tkinter as tk
from tkinter import ttk, messagebox
from library import Library
from book import Book
import datetime

class LibraryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1000x700")
        self.root.configure(bg="#f0f0f0")
        
        self.library = Library()
        
        # 创建主框架 / Create main frame
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 创建标题 / Create title
        self.title_label = ttk.Label(self.main_frame, text="Library Management System", font=("Arial", 24, "bold"))
        self.title_label.pack(pady=20)
        
        # 创建选项卡 / Create notebook
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # 图书管理选项卡 / Book management tab
        self.book_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.book_tab, text="Book Management")
        
        # 借阅管理选项卡 / Borrow management tab
        self.borrow_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.borrow_tab, text="Borrow Management")
        
        # 统计分析选项卡 / Statistics tab
        self.stats_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.stats_tab, text="Statistics")
        
        # 借阅记录选项卡 / Borrow records tab
        self.records_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.records_tab, text="Borrow Records")
        
        # 初始化各个选项卡 / Initialize tabs
        self.init_book_tab()
        self.init_borrow_tab()
        self.init_stats_tab()
        self.init_records_tab()
    
    def init_book_tab(self):
        # 创建添加图书区域 / Create add book area
        add_frame = ttk.LabelFrame(self.book_tab, text="Add Book", padding="10")
        add_frame.pack(fill=tk.X, pady=10)
        
        # 添加图书表单 / Add book form
        ttk.Label(add_frame, text="Book ID:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.book_id_entry = ttk.Entry(add_frame, width=20)
        self.book_id_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(add_frame, text="Book Name:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.book_name_entry = ttk.Entry(add_frame, width=40)
        self.book_name_entry.grid(row=1, column=1, padx=5, pady=5, columnspan=2)
        
        ttk.Label(add_frame, text="Author:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.author_entry = ttk.Entry(add_frame, width=40)
        self.author_entry.grid(row=2, column=1, padx=5, pady=5, columnspan=2)
        
        ttk.Label(add_frame, text="Category:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.category_entry = ttk.Entry(add_frame, width=20)
        self.category_entry.grid(row=3, column=1, padx=5, pady=5)
        self.category_entry.insert(0, "General")
        
        ttk.Button(add_frame, text="Add Book", command=self.add_book).grid(row=4, column=1, padx=5, pady=10)
        
        # 创建搜索和删除区域 / Create search and delete area
        search_frame = ttk.LabelFrame(self.book_tab, text="Search & Delete", padding="10")
        search_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(search_frame, text="Search by:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.search_option = tk.StringVar()
        search_options = ["ID", "Name", "Author", "Category"]
        ttk.Combobox(search_frame, textvariable=self.search_option, values=search_options, width=15).grid(row=0, column=1, padx=5, pady=5)
        self.search_option.set("ID")
        
        ttk.Label(search_frame, text="Keyword:").grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)
        self.search_entry = ttk.Entry(search_frame, width=30)
        self.search_entry.grid(row=0, column=3, padx=5, pady=5)
        
        ttk.Button(search_frame, text="Search", command=self.search_books).grid(row=0, column=4, padx=5, pady=5)
        ttk.Button(search_frame, text="Delete Book", command=self.delete_book).grid(row=1, column=4, padx=5, pady=5)
        
        # 创建图书列表 / Create book list
        list_frame = ttk.LabelFrame(self.book_tab, text="Book List", padding="10")
        list_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # 创建树形视图 / Create treeview
        columns = ("id", "name", "author", "category", "status")
        self.book_tree = ttk.Treeview(list_frame, columns=columns, show="headings")
        
        # 设置列标题 / Set column headings
        self.book_tree.heading("id", text="ID")
        self.book_tree.heading("name", text="Name")
        self.book_tree.heading("author", text="Author")
        self.book_tree.heading("category", text="Category")
        self.book_tree.heading("status", text="Status")
        
        # 设置列宽 / Set column widths
        self.book_tree.column("id", width=50)
        self.book_tree.column("name", width=200)
        self.book_tree.column("author", width=150)
        self.book_tree.column("category", width=100)
        self.book_tree.column("status", width=100)
        
        # 添加滚动条 / Add scrollbar
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.book_tree.yview)
        self.book_tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.book_tree.pack(fill=tk.BOTH, expand=True)
        
        # 加载图书数据 / Load book data
        self.load_books()
    
    def init_borrow_tab(self):
        # 创建借阅区域 / Create borrow area
        borrow_frame = ttk.LabelFrame(self.borrow_tab, text="Borrow Book", padding="10")
        borrow_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(borrow_frame, text="Book ID:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.borrow_id_entry = ttk.Entry(borrow_frame, width=20)
        self.borrow_id_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(borrow_frame, text="Borrower Name:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.borrower_entry = ttk.Entry(borrow_frame, width=40)
        self.borrower_entry.grid(row=1, column=1, padx=5, pady=5, columnspan=2)
        
        ttk.Button(borrow_frame, text="Borrow Book", command=self.borrow_book).grid(row=2, column=1, padx=5, pady=10)
        
        # 创建归还区域 / Create return area
        return_frame = ttk.LabelFrame(self.borrow_tab, text="Return Book", padding="10")
        return_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(return_frame, text="Book ID:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.return_id_entry = ttk.Entry(return_frame, width=20)
        self.return_id_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Button(return_frame, text="Return Book", command=self.return_book).grid(row=1, column=1, padx=5, pady=10)
        
        # 创建借阅状态区域 / Create borrow status area
        status_frame = ttk.LabelFrame(self.borrow_tab, text="Borrow Status", padding="10")
        status_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # 创建树形视图 / Create treeview
        columns = ("id", "name", "borrower", "borrow_date", "return_date")
        self.borrow_tree = ttk.Treeview(status_frame, columns=columns, show="headings")
        
        # 设置列标题 / Set column headings
        self.borrow_tree.heading("id", text="Book ID")
        self.borrow_tree.heading("name", text="Book Name")
        self.borrow_tree.heading("borrower", text="Borrower")
        self.borrow_tree.heading("borrow_date", text="Borrow Date")
        self.borrow_tree.heading("return_date", text="Return Date")
        
        # 设置列宽 / Set column widths
        self.borrow_tree.column("id", width=80)
        self.borrow_tree.column("name", width=200)
        self.borrow_tree.column("borrower", width=150)
        self.borrow_tree.column("borrow_date", width=150)
        self.borrow_tree.column("return_date", width=150)
        
        # 添加滚动条 / Add scrollbar
        scrollbar = ttk.Scrollbar(status_frame, orient=tk.VERTICAL, command=self.borrow_tree.yview)
        self.borrow_tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.borrow_tree.pack(fill=tk.BOTH, expand=True)
        
        # 加载借阅记录 / Load borrow records
        self.load_borrow_records()
    
    def init_stats_tab(self):
        # 创建统计区域 / Create statistics area
        stats_frame = ttk.LabelFrame(self.stats_tab, text="Book Statistics", padding="10")
        stats_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # 总体统计 / Overall statistics
        total_frame = ttk.Frame(stats_frame)
        total_frame.pack(fill=tk.X, pady=10)
        
        self.total_books_label = ttk.Label(total_frame, text="Total Books: ", font=("Arial", 12))
        self.total_books_label.pack(side=tk.LEFT, padx=20)
        
        self.available_books_label = ttk.Label(total_frame, text="Available Books: ", font=("Arial", 12))
        self.available_books_label.pack(side=tk.LEFT, padx=20)
        
        self.borrowed_books_label = ttk.Label(total_frame, text="Borrowed Books: ", font=("Arial", 12))
        self.borrowed_books_label.pack(side=tk.LEFT, padx=20)
        
        # 分类统计 / Category statistics
        category_frame = ttk.LabelFrame(stats_frame, text="Category Statistics", padding="10")
        category_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # 创建树形视图 / Create treeview
        columns = ("category", "total", "available", "borrowed")
        self.category_tree = ttk.Treeview(category_frame, columns=columns, show="headings")
        
        # 设置列标题 / Set column headings
        self.category_tree.heading("category", text="Category")
        self.category_tree.heading("total", text="Total")
        self.category_tree.heading("available", text="Available")
        self.category_tree.heading("borrowed", text="Borrowed")
        
        # 设置列宽 / Set column widths
        self.category_tree.column("category", width=150)
        self.category_tree.column("total", width=80)
        self.category_tree.column("available", width=80)
        self.category_tree.column("borrowed", width=80)
        
        # 添加滚动条 / Add scrollbar
        scrollbar = ttk.Scrollbar(category_frame, orient=tk.VERTICAL, command=self.category_tree.yview)
        self.category_tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.category_tree.pack(fill=tk.BOTH, expand=True)
        
        # 加载统计数据 / Load statistics
        self.load_statistics()
    
    def init_records_tab(self):
        # 创建借阅记录区域 / Create borrow records area
        records_frame = ttk.LabelFrame(self.records_tab, text="Borrow Records", padding="10")
        records_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # 创建树形视图 / Create treeview
        columns = ("id", "book_name", "borrower", "borrow_date", "return_date")
        self.records_tree = ttk.Treeview(records_frame, columns=columns, show="headings")
        
        # 设置列标题 / Set column headings
        self.records_tree.heading("id", text="Record ID")
        self.records_tree.heading("book_name", text="Book Name")
        self.records_tree.heading("borrower", text="Borrower")
        self.records_tree.heading("borrow_date", text="Borrow Date")
        self.records_tree.heading("return_date", text="Return Date")
        
        # 设置列宽 / Set column widths
        self.records_tree.column("id", width=80)
        self.records_tree.column("book_name", width=200)
        self.records_tree.column("borrower", width=150)
        self.records_tree.column("borrow_date", width=150)
        self.records_tree.column("return_date", width=150)
        
        # 添加滚动条 / Add scrollbar
        scrollbar = ttk.Scrollbar(records_frame, orient=tk.VERTICAL, command=self.records_tree.yview)
        self.records_tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.records_tree.pack(fill=tk.BOTH, expand=True)
        
        # 加载借阅记录 / Load borrow records
        self.load_all_records()
    
    def add_book(self):
        try:
            book_id = int(self.book_id_entry.get())
            name = self.book_name_entry.get()
            author = self.author_entry.get()
            category = self.category_entry.get()
            
            if not name or not author:
                messagebox.showerror("Error", "Book name and author are required")
                return
            
            # 检查图书ID是否已存在
            if self.library.find_book_by_id(book_id):
                messagebox.showerror("Error", f"Book with ID {book_id} already exists")
                return
            
            book = Book(book_id, name, author, category)
            result = self.library.add_book(book)
            messagebox.showinfo("Success", result)
            
            # 清空表单
            self.book_id_entry.delete(0, tk.END)
            self.book_name_entry.delete(0, tk.END)
            self.author_entry.delete(0, tk.END)
            self.category_entry.delete(0, tk.END)
            self.category_entry.insert(0, "General")
            
            # 刷新图书列表
            self.load_books()
            self.load_statistics()
        except ValueError:
            messagebox.showerror("Error", "Book ID must be a number")
    
    def search_books(self):
        option = self.search_option.get()
        keyword = self.search_entry.get()
        
        if not keyword:
            messagebox.showerror("Error", "Please enter a keyword")
            return
        
        # 清空树形视图
        for item in self.book_tree.get_children():
            self.book_tree.delete(item)
        
        # 搜索图书
        if option == "ID":
            try:
                book_id = int(keyword)
                book = self.library.find_book_by_id(book_id)
                if book:
                    self.book_tree.insert("", tk.END, values=(
                        book.book_id, book.name, book.author, book.category,
                        "Available" if book.status == 1 else "Borrowed"
                    ))
                else:
                    messagebox.showinfo("Search Result", f"No book found with ID {book_id}")
            except ValueError:
                messagebox.showerror("Error", "Book ID must be a number")
        elif option == "Name":
            books = self.library.find_books_by_name(keyword)
            if books:
                for book in books:
                    self.book_tree.insert("", tk.END, values=(
                        book.book_id, book.name, book.author, book.category,
                        "Available" if book.status == 1 else "Borrowed"
                    ))
            else:
                messagebox.showinfo("Search Result", f"No books found with name containing '{keyword}'")
        elif option == "Author":
            books = self.library.find_books_by_author(keyword)
            if books:
                for book in books:
                    self.book_tree.insert("", tk.END, values=(
                        book.book_id, book.name, book.author, book.category,
                        "Available" if book.status == 1 else "Borrowed"
                    ))
            else:
                messagebox.showinfo("Search Result", f"No books found by author '{keyword}'")
        elif option == "Category":
            books = self.library.find_books_by_category(keyword)
            if books:
                for book in books:
                    self.book_tree.insert("", tk.END, values=(
                        book.book_id, book.name, book.author, book.category,
                        "Available" if book.status == 1 else "Borrowed"
                    ))
            else:
                messagebox.showinfo("Search Result", f"No books found in category '{keyword}'")
    
    def delete_book(self):
        selected_item = self.book_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a book to delete")
            return
        
        item = selected_item[0]
        book_id = int(self.book_tree.item(item, "values")[0])
        
        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete book with ID {book_id}?"):
            result = self.library.delete_book(book_id)
            messagebox.showinfo("Result", result)
            self.load_books()
            self.load_statistics()
    
    def borrow_book(self):
        try:
            book_id = int(self.borrow_id_entry.get())
            borrower = self.borrower_entry.get()
            
            if not borrower:
                messagebox.showerror("Error", "Borrower name is required")
                return
            
            result = self.library.borrow_book(book_id, borrower)
            messagebox.showinfo("Result", result)
            
            # 清空表单
            self.borrow_id_entry.delete(0, tk.END)
            self.borrower_entry.delete(0, tk.END)
            
            # 刷新借阅记录和图书列表
            self.load_books()
            self.load_borrow_records()
            self.load_statistics()
            self.load_all_records()
        except ValueError:
            messagebox.showerror("Error", "Book ID must be a number")
    
    def return_book(self):
        try:
            book_id = int(self.return_id_entry.get())
            result = self.library.return_book(book_id)
            messagebox.showinfo("Result", result)
            
            # 清空表单
            self.return_id_entry.delete(0, tk.END)
            
            # 刷新借阅记录和图书列表
            self.load_books()
            self.load_borrow_records()
            self.load_statistics()
            self.load_all_records()
        except ValueError:
            messagebox.showerror("Error", "Book ID must be a number")
    
    def load_books(self):
        # 清空树形视图
        for item in self.book_tree.get_children():
            self.book_tree.delete(item)
        
        # 加载所有图书
        books = self.library.list_all_book()
        for book in books:
            self.book_tree.insert("", tk.END, values=(
                book.book_id, book.name, book.author, book.category,
                "Available" if book.status == 1 else "Borrowed"
            ))
    
    def load_borrow_records(self):
        # 清空树形视图
        for item in self.borrow_tree.get_children():
            self.borrow_tree.delete(item)
        
        # 加载未归还的借阅记录
        records = self.library.get_borrow_records()
        for record in records:
            if record['return_date'] is None:
                self.borrow_tree.insert("", tk.END, values=(
                    record['book_id'], record['book_name'], record['borrower'],
                    record['borrow_date'], "Not returned"
                ))
    
    def load_all_records(self):
        # 清空树形视图
        for item in self.records_tree.get_children():
            self.records_tree.delete(item)
        
        # 加载所有借阅记录
        records = self.library.get_borrow_records()
        for i, record in enumerate(records, 1):
            self.records_tree.insert("", tk.END, values=(
                i, record['book_name'], record['borrower'],
                record['borrow_date'], record['return_date'] or "Not returned"
            ))
    
    def load_statistics(self):
        # 获取统计数据
        stats = self.library.get_book_statistics()
        
        # 更新总体统计
        self.total_books_label.config(text=f"Total Books: {stats['total_books']}")
        self.available_books_label.config(text=f"Available Books: {stats['available_books']}")
        self.borrowed_books_label.config(text=f"Borrowed Books: {stats['borrowed_books']}")
        
        # 清空分类统计
        for item in self.category_tree.get_children():
            self.category_tree.delete(item)
        
        # 加载分类统计
        for category, data in stats['category_stats'].items():
            self.category_tree.insert("", tk.END, values=(
                category, data['total'], data['available'], data['borrowed']
            ))

def main():
    root = tk.Tk()
    app = LibraryGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
