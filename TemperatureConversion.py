class Temperature:
    def __init__(self,temp):
       self.temp=temp
       
    def toCelsius(self):
        a=(self.temp-32)*5/9
        return a
        
    def tofahrenheit(self):
        b=(self.temp+32)*9/5
        return b
        
temp1=Temperature(20)
temp2=Temperature(37)
print(temp1.toCelsius())
print(temp2.tofahrenheit())