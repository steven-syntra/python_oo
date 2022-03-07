class Parent:
    def talk(self):
        print("Parent talking!")

class Child(Parent):
    def talk(self):
        print("Child talking!")

class TalkativeChild(Parent):
    def talk(self):
        print("TalkativeChild talking!")
        Parent.talk(self)


p, c, tc = Parent(), Child(), TalkativeChild()

for obj in (p, c, tc):
    obj.talk()