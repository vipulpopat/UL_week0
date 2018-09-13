class Pigeon:
    def __init__(self, name, color, speed):
      self.name = name
      self.color = color
      self.speed = speed

    def __str__(self):
      return "Pigeon : " + self.name + ", color = " + self.color + ", speed = " + str(self.speed)

p = Pigeon("test", "blue", 1234)
print("Pigeon : " + str(p))
