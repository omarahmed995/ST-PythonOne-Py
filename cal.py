class cal():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

    def sub(self):
        return self.a - self.b


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
cal1=cal(a,b)
result=cal1.add()
result1=cal1.sub()
result2=cal1.div()
result3=cal1.mul()
print(result)
print(result1)
print(result2)
print(result3)
