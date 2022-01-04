from  collections.abc import MutableSequence
class CrayonsBox(MutableSequence):

	def __init__(self, iterable):
		self._crayons = list(iterable)
	
	def __len__(self):
		return len(self._crayons)
	
	def __getitem__(self, index):
		return self._crayons[index]
	
	def __setitem__(self,obj, value):
		self._val = value
	
	def insert(self, value):
		self._val += value
		return self
	
	def __delitem__(self, value):
	   return self
