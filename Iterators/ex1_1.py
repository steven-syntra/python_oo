class MyNumbers:

    def __iter__(self):
        self.a = 0
        return self

    def __next__(self):
        self.a += 1
        return self.a


mynumbers = MyNumbers()
myiter = iter(mynumbers)

print(next(myiter))
print(next(myiter))
print(next(myiter))
