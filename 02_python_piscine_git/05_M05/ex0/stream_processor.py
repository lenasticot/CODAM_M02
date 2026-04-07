from abc import ABC, abstractmethod
from typing import Any

class DataProcessor(ABC):
	@abstractmethod
	def validate(self, data: Any) -> bool:
		# will check whether the input data are appropriate for the current data process
		pass
	@abstractmethod
	def ingest(self, data: Any) -> tuple [int, str]:
		# will process the input data
		pass
	def output(self):
		# will extract the oldest piece of data stored internally in the data processor,
		# along with the associated processing rank within the data processor
		# to check what type of data to print accordingly the thing
		# probably an if statement
		# use ingest data to print accordingly
		pass

class NumericProcessor(DataProcessor):
	# ingest int, floats, and lists of both types (including mixed-type lists)
	# it then converts the data into strings and stores it internally,
	# waiting to be extracted using the output method.
	# the overriding ingest method signature must reflect the accepted types
	def validate(self, data: Any):
		print(f"trying to validate input '{data}': ", end="")
		try:
			check = int(data)
		except: 
			return False
		return True
	def ingest(self, data: Any):
		# need to add a check that validate() has been called before calling this one
		# raising an error if it occurs
		# if not 
		# converts the data into strings and stores it internally
		if self.validate == True: 
			print("ok we're good")
		else:
			print("What are you trying to do?")

class TextProcessor(DataProcessor):
	# ingest str and lists of strings.
	
	def validate(self, data: Any):
		print(f"Trying to validate input {data}: ", end="")
		if isinstance(data, str):
			return True
		elif isinstance(data, list):
			return True
		else:
			return False
	def ingest(self, data: Any):
		# stores the data internally, waiting to be extracted
		#  it stores the data internally, waiting to be extracted using the output method.
	# The overriding ingest method signature must reflect the accepted types
		pass


class LogProcessor(DataProcessor):
	# ingest a dict of string key-value pairs, and lists of that type.
	
	def validate(self, data: Any):
		print(f"Trying to validate input {data}: ", end="")
		if isinstance(data, list):
			#need to check inside if its a dict
			return True
		else:
			return False
	def ingest(self, data: Any):
		# it then converts the data into strings and stores it internally, waiting to be extracted using the output method
	# The overriding ingest method signature must reflect the accepted types
		pass

def main():
	# In case the user
	# does not validate the data before calling ingest, and provides invalid data, an
	# exception must be raised.
	print("=== CODE NEXUS - DATA PROCESSOR ===\n")
	print("Testing Numeric Processor ...")
	test_1 = NumericProcessor()
	print(test_1.validate(42))
	print(test_1.validate("oui"))
	print(test_1.validate(1.5))
	print(test_1.ingest(42))

	test_2 = TextProcessor()
	print("Testing Text Processor")
	print(test_2.validate(42))
	print(test_2.validate("oui"))
	print(test_2.validate(["oui", "oui", "oui"]))
	test_3 = LogProcessor()
	print("Testing Log Processor")
	print(test_3.validate(42))
	print(test_3.validate("oui"))
	print(test_3.validate(["oui", "oui", "oui"]))
	print(test_3.validate([{'log_level': 'NOTICE', 'log_message': 'Connection to server'}, {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]))


main()

