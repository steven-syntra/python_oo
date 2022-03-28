# Create a Player class
class Player:
    SPEED = 10

    def __init__(self):
        self.position = 0
        # self.SPEED = Player.SPEED
        # self.SPEED = self.SPEED

    def increase(self):
        self.SPEED = 133


# Create a player p1
p1 = Player()
print("====== p1 =======")
print(f"SPEED: {p1.SPEED}")
print(f"properties: {p1.__dict__}")
print("")

# Create a player p2
p2 = Player()
p2.SPEED = 20
p2.whatever = 999

print("====== p2 =======")
print(f"SPEED: {p2.SPEED}")
print(f"whatever: {p2.whatever}")
print(f"properties: {p2.__dict__}")
print("")

print("====== p1 again =======")
print(f"SPEED: {p1.SPEED}")
print("")

# nu veranderen we de class property SPEED
Player.SPEED = 50

print("====== p2 after change to 50 =======")
print(f"SPEED: {p2.SPEED}")
print("")

print("====== p1 after change to 50 =======")
print(f"SPEED: {p1.SPEED}")
print("")

p3 = Player()
p3.increase()
print("====== p3 =======")
print(f"SPEED: {p3.SPEED}")
print(f"properties: {p3.__dict__}")
print("")

Player.SPEED = 1000

print("====== p3 =======")
print(f"SPEED: {p3.SPEED}")