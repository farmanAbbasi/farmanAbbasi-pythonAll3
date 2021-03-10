class Computer:
    def __init__(self,x):
        self.x=x
        
        
    def config(self):
        print(self.x)
obj1=Computer(20)
obj2=Computer(30)

obj1.config()
obj2.config()
