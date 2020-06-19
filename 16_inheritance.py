class Parent:

    def parent_method(self):
        print("Parent class")

class Child(Parent):

    def child_method(self):
        print("Child class")

c1 = Child()
c1.parent_method()
c1.child_method()
