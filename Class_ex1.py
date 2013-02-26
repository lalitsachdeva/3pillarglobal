	
class test :
	"""docstring for test will help in testing the required file"""
	arg = 0
	def __init__(self, arg):
		self.arg = arg

obj = test(3)
if hasattr(obj, 'arg'):
	print obj.arg

setattr(obj, 'arg' , 5)

a = getattr(obj, 'arg')
print  a
delattr(obj, 'arg')
print test.__dict__
print test.__name__
print test.__module__

class Point:
   def __init( self, x=0, y=0):
      self.x = x
      self.y = y
   def __del__(self):
      class_name = self.__class__.__name__
      print class_name, "destroyed"

pt1 = Point()
pt2 = pt1
pt3 = pt1
print id(pt1), id(pt2), id(pt3) # prints the ids of the obejcts
del pt1
del pt2
del pt3