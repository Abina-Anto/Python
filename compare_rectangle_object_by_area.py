class Rectangle:
        def _init_(self):
            self.length=int(input("Enter the length:"))
            self.breadth=int(input("Enter the breadth:"))
        def area(self):
            self.a=self.length*self.breadth
            print("Area of rectangle:",self.a)
            return self.a
        def perimeter(self):
            self.p=2*(self.length+self.breadth)
            print("Perimeter of rectangle:",self.p,"\n")
            
x=Rectangle()
print("\n_Rectangle 1_")
x._init_()
a1=x.area()
x.perimeter()

y=Rectangle()
print("\n_Rectangle 2_")
y._init_()
b1=y.area()
y.perimeter()

if a1>b1:
    print("Rectangle 1 is bigger")
    
elif a1==b1:
    print("Both rectangles are of same area")
else:
    print("Rectangle 2 is bigger")
