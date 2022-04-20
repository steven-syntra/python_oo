class MyNumbers:

    def __iter__(self):
        self.a = 0
        return self

    def __next__(self):
        self.a += 1
        return self.a


mynumbers = MyNumbers()

# loop until 1000
for number in mynumbers:
    print(number)
    if number >= 1000:
        break

