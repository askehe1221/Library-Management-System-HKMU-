class Book(object):#book book class

    def __init__(self,book_id,name,author,status=1): #Not currently on loan
        self.book_id=book_id
        self.name=name
        self.author=author
        self.status=status


    def __str__(self):
        if self.status == 1:
            status = "Not on loan"
        elif self.status == 0:
            status = "On loan"
        else:
            status= "Status Error"

        return 'Name:《{}》,Author:{},Status:<{}>'.format(self.name,self.author,status)
