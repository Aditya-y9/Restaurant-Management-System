class Book:
    """
    Information about the books in the library.
    """

    def __init__(self, title, author, price, publisher):
        """
        Create a new book with title, author, price, and publisher information.
        
        Args:
        - title (str): The title of the book.
        - author (list): A list of authors of the book.
        - price (float): The price of the book.
        - publisher (str): The publisher of the book.
        """
        self.title = title
        self.author = author[:]
        self.price = price
        self.publisher = publisher

    def number_of_authors(self):
        """
        Returns the number of authors of the book.
        
        Returns:
        - int: The number of authors.
        """
        return len(self.author)

    def print_price(self, abc):
        """
        Prints the cost of the book.
        
        Args:
        - abc (Book): The book object.
        """
        print(abc.price)

    def __str__(self):
        """
        Returns a human-readable output of the book.
        
        Returns:
        - str: The formatted string representation of the book.
        """
        return """Title: {0}
        Authors: {1}
        Price: {2}
        Publisher: {3}""".format(self.title, ",".join(self.author), self.price, self.publisher)

    def __eq__(self, other):
        """
        Returns True if the book and the other book have the same publisher.
        
        Args:
        - other (Book): The other book object.
        
        Returns:
        - bool: True if the books have the same publisher, False otherwise.
        """
        return self.publisher == other.publisher
	

python_book1 = Book('Python', ["ABC", "XYZ", "UVW"], 299, "THM")
print(python_book1)
		
print(Book.number_of_authors(python_book1))	
print(Book.print_price(python_book1))
print(python_book1.print_price())