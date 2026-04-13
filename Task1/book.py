class Book(object):#book 类 图书

    def __init__(self,book_id,name,author,category="General",status=1): #默认其未借出
        self.book_id=book_id
        self.name=name
        self.author=author
        self.category=category
        self.status=status

    def __str__(self):
        if self.status == 1:
            status = "Not on loan"
        elif self.status == 0:
            status = "On loan"
        else:
            status= "Status Error"
        return 'ID: {}, Name:《{}》, Author: {}, Category: {}, Status: <{}>'.format(self.book_id, self.name, self.author, self.category, status)
    
    def to_dict(self):
        return {
            'book_id': self.book_id,
            'name': self.name,
            'author': self.author,
            'category': self.category,
            'status': self.status
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            book_id=data['book_id'],
            name=data['name'],
            author=data['author'],
            category=data.get('category', 'General'),
            status=data['status']
        )