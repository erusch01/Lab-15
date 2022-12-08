#Emily Rusch and Ellen Kevin
class Fabric:
    def __init__(self, countryOfOrigin, color):
        self.countryOfOrigin = countryOfOrigin
        self.color = color

    def __str__(self):
        return self.countryOfOrigin + "(" + str(self.color) + ")"

p1 = Fabric("Italy", "green")

print(p1)
