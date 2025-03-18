class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_car_info(self):
        return f"{self.year} {self.make} {self.model}"

# 2. Owner Class
class Owner:
    def __init__(self, name):
        self.name = name
        self.cars_owned = []

    def purchase_car(self, car):
       self.cars_owned.append(car)
       print(f"{self.name} just purchased a {car.get_car_info()}")

    def show_owned_cars(self):
       if not self.cars_owned:
           print(f"{self.name} doesn't own any cars yet.")
       else:
           print(f"{self.name} owns the following cars: ")
           index = 1
           for car in self.cars_owned:
               print(f"{index}. {car.get_car_info()}")
               index += 1
           


# 3. Main Demonstration Function
def main():
    owners = {}

    while True:
        name = input("Enter the owner's name (or 'done' to finish): ")
        if name == "done":
            break
        if name not in owners:
            owners[name] = Owner(name)

        car = Car(input("Enter car make: "), input("Enter car model: "), input("Enter car year: "))
        owners[name].purchase_car(car)
        print()

    print("Final list of owners and their cars: ")
    for owner in owners.values():
        owner.show_owned_cars()
        print()




# 4. Execution
if __name__ == "__main__":
    main()
