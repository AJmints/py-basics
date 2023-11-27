class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print("Moves along...")

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")

my_car = Vehicle("Jeep", "Patriot")

my_car.get_make_model()
my_car.moves()


class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print("Flies along...")

class Truck(Vehicle):
    def moves(self):
        print("Rumbles along...")

class GolfCart(Vehicle):
    pass

my_plane = Airplane("Cessna", "Skyhawk", "23-42")
truck = Truck("Mack", "Pinnacle")
golf_wagon = GolfCart("Yamaha", "Super100")

my_plane.get_make_model()
my_plane.moves()

truck.get_make_model()
truck.moves()

golf_wagon.get_make_model()
golf_wagon.moves()

print("\n\n")

# Polymorphism example, OOP, oh yeah!
for v in (my_car, my_plane, truck, golf_wagon):
    v.get_make_model()
    v.moves()
