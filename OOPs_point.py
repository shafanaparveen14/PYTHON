#Point class
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
 #Show Method
    def show(self):
         print("Point:",self.x,self.y)
#Change coordinates
    def change(self,x,y):
        self.x=x
        self.y=y
#Distance Between 2 Points
    def dist(self,other):
        d=((self.x-other.x)**2+(self.y-other.y)**2)**0.5
        return d
#Create 3 Points
p1=Point(1,2)
p2=Point(4,5)
p3=Point(0,0)
#Access Method
p1.show()
p2.show()

p1.change(2,3)
p1.show()
print("Distance p1 and p2",p1.dist(p2))
print("Distance p2 and p3",p2.dist(p3))
        
        
