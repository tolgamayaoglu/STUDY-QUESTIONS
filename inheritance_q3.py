# Inheritance Q3

class A(object):
  def one(self):
    return 'A'

  def two(self):
    return 'B'
 
class B(A):
  def two(self):
    return self.one()

obj1 = A()
obj2 = B()

print(obj1.two(), obj2.two())

# Obj1 uses its two() function. Therefore it returns B. Obj2 also uses its two() function and calls the parent class's one() function; therefore, it returns A, and we don't see any errors.