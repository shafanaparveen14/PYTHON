#OOPS:
class Employee:
    def set_data(self,name,salary):
        self.name=name
        self.salary=salary
    def show(self):
        print(self.name,self.salary)
#Self point to current instance(object) of class
        
#Object Creation:
e1=Employee()
e2=Employee()

e1.set_data("A",10000)
e2.set_data("B",20000)
e1.show()
e2.show()
