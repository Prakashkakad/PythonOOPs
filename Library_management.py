class Library:
    def __init__(self):
        self.no_of_Books = 0
        self.Books = []

    def AddBooks(self,Books):
        self.Books.append(Books)
        self.no_of_Books= len(self.Books)

    def ShowDetails(self):
        print(f"The Library has {self.no_of_Books} Books.The books name is ")
        for Books in self.Books:
            print(Books)

li = Library()
li.AddBooks("Prakash Kakad1")
li.AddBooks("Prakash Kakad2")
li.AddBooks("Prakash Kakad3")
li.ShowDetails()

