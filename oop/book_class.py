# This class is called Book
class Book:
	# Here We use a constructor 110 make a new book
	def __init__ (self, title, author, year):
		self.title=title
		self.author=author
		self.year=year

	# Here we print it. It's when print(book) is called?
	def __str__(self):
		return f"{self.title} by {self.author}, published in {self.year}"

	# To demonstrate recreating the object (instancing?)
	def __repr__(self):
		return f"Book('{self.title}', '{self.author}', {self.year})"

	# Deleting a book instance
	def __del__(self):
		print (f"Deleting {self.title}")
