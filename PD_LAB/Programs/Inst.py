class Inst:
    """
    A class for Institute/University.
    """

    def __init__(self, name, id_number, email_id):
        """
        Constructor for the Inst class.

        Parameters:
        - name (str): The name of the institute.
        - id_number (int): The ID number of the institute.
        - email_id (str): The email ID of the institute.
        """
        self.name = name
        self.id_number = id_number
        self.email_id = email_id

    def __str__(self):
        """
        Returns a string representation of the Inst object.

        Returns:
        - str: A formatted string containing the name, ID number, and email ID of the institute.
        """
        return '{}\n{}\n{}'.format(self.name, self.id_number, self.email_id)

# Inheritance
class Faculty(Inst):
	"""
	Creating the information for the faculty members of the institute
	"""
	
	def __init__(self, name, id_number, email_id, salary):
		"""
		Information about the faculty of the institute
		"""
		
		super().__init__(name, id_number, email_id)
		self.salary = salary

# Inheritance
class Student(Inst):
	"""
	Creating the information for the students members of the institute
	"""
	
	def __init__(self, name, id_number, email_id, perc):
		"""
		Information about the students of the institute
		"""
		Inst.__init__(self, name, id_number, email_id)
		self.perc = perc
		self.gy = 2022

sandeep = Faculty('Sandeep Udmale', 1659, 'ssudmale@gmail.com', 100)
print(sandeep.name, sandeep.salary)

aditya = Student('Aditya Yedurkar', 221080076, 'aditya.yedurkar@gmail.com', 100)
print(aditya.name, aditya.perc, aditya.gy)
		
