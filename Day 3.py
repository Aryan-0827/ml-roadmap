class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Book: {self.title} by {self.author}, Pages: {self.pages}"


class EBook(Book):
    def __init__(self, title, author, pages, file_size, format):
        super().__init__(title, author, pages)
        self.file_size = file_size
        self.format = format

    def __str__(self):
        return f"{super().__str__()} | Format: {self.format} | Size: {self.file_size}"


b = Book("Atomic Habits", "James Clear", 320)
e = EBook("Atomic Habits", "James Clear", 320, "2MB", "PDF")

print(b)
print(e)