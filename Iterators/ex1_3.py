class MyNumbers:

    def __iter__(self):
        self.a = 0
        return self

    def __next__(self):
        self.a += 1
        # loop until 1000
        if self.a > 1000:
            raise StopIteration

        return self.a


mynumbers = MyNumbers()

for number in mynumbers:
    print(number)

print("Iteration finished")