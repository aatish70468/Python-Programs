class Parent1:

    def method1(self):
        print("Parent1 Class")

class Parent2:

    def method2(self):
        print("Parent2 Class")

class Child(Parent1, Parent2):

    def method3(self):
        print("Child Class")


c1 = Child()
c1.method1()
c1.method2()
c1.method3()
