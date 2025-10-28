class Book:
    def __init__(self, title, authors, publication_year):
        self.title = title
        self.authors = authors
        self.publication_year = publication_year

    def __str__(self):
        auth = ' & '.join(self.authors)
        return f'{auth}: {self.title} ({self.publication_year})'

    def num_authors(self):
        return len(self.authors)

books = Book('Introduction to Algorithms (3rd ed.)',
            ['Cormen', 'Leiserson', 'Rivest', 'Stein'],
            2009)
print(books) 

books = [Book('Introduction to Algorithms (3rd ed.)',
            ['Cormen', 'Leiserson', 'Rivest', 'Stein'],
            2009), ('1984', 'George', 1995)]