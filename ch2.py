class student:
    def __init__(self,name,x,y,z):
        self.name=name
        self.m1=x
        self.m2=y
        self.m3=z
    def average(self):
        a=self.m1+self.m2+self.m3
        k=a/3
        print(self.name ," average is: ",k) 
s1=student("sricharan",46,45,46) 
s1.name="kishan"
s1.average()           
        