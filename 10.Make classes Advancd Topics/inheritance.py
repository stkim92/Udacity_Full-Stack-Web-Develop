class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor called")
        self.lastname = last_name
        self.eye_color = eye_color
    def show_info(self):
        print("Last name is -" + self.lastname)
        print("eye_color is -" + self.eye_color)

class Child(Parent):
    def __init__(self, last_name, eye_color, toy):
        print("Child Constructor called")
        Parent.__init__(self,last_name, eye_color)
        self.toyNum = toy
    def show_info(self):
        print("Last name is -" + self.lastname)
        print("eye_color is -" + self.eye_color)
        print("toy - " + str(self.toyNum))

Tom = Parent("KIM","black")
#print(Tom.lastname)

tom = Child("KIM","black",100)
print(tom.lastname)
print(tom.toyNum)
tom.show_info()
