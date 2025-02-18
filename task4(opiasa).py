class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        """Displays the details of the book."""
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year Published: {self.year_published}")
        print("-" * 30)

# Create three Book objects
book1 = Book(title="The Notebook ", author="Nicholas Sparks ", year_published=1996)
book2 = Book(title="Me Before You", author="Jojo Moyes", year_published=2012)
book3 = Book(title="The Alchemist", author=" Paulo Coelho ", year_published=1988)

# Display the details of each book
book1.describe()
book2.describe()
book3.describe()
