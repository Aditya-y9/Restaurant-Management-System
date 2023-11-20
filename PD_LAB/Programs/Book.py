class Book:
	"""
	Information about the books in library
	"""
	
	def number_of_authors(self):
		"""
		(Book) -> int
		Returns the number of authors of the book
		"""

		return len(self.autlhor)

# Python has dynamic attributes which are defined at runtime.	
python_book1 = Book()
python_book1.title = 'Python'
python_book1.author = ["ABC", "XYZ", "UVW"]

python_book1.price = 299
python_book1.publisher = "THM"
print(python_book1.title, python_book1.author, python_book1.price, python_book1.publisher)

# The name must be same as file name.
# In Terminal:
   # 1) import Book
   # 2) dir(Book)