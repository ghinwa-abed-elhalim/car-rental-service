class vehicle: 
    def __init__(self, brand, model, year, rental_price_per_days):
        self.brand = brand
        self.model = model
        self.year = year
        self.rental_price_per_days = rental_price_per_days

    def display_info(self):
        print(f"vehicle {self.brand} {self.model}, year: {self.year}, rental price: {self.rental_price_per_days}")

    def rental_cost(self, days):
     return self.rental_price_per_days * days
    
    def get_rental_price_per_days(self):
        return self.rental_price_per_days
    
    def set_rental_price_per_days(self, new_price):
       self.rental_price_per_days = new_price

class car(vehicle):
    def __init__(self, brand, model, year, rental_price_per_days, seating_capacity):
      super().__init__(brand, model, year, rental_price_per_days)
      self.seating_capacity = seating_capacity
    def display_info(self):
       print(f"vehicle {self.brand} {self.model}, year: {self.year}, rental price: {self.get_rental_price_per_days}, seating capacity: {self.seating_capacity}")

class bike(vehicle):
    def __init__(self, brand, model, year, rental_price_per_days, engine_capacity):
      super().__init__(brand, model, year, rental_price_per_days)
      self.engine_capacity = engine_capacity
    def display_info(self): 
       print(f"vehicle {self.brand} {self.model}, year: {self.year}, rental price: {self.rental_price_per_days}, engine capacity: {self.engine_capacity}")
       
    def show_vehicle_info(vehicle):
     vehicle.display_info()



car = car("Toyota","Corolla", 2020, 50, 5)

car.display_info()

bike = bike("Yamaha", "R1", 2019, 30, 998)
bike.display_info()


print(f"\nrental cost for Toyota Corolla for 3 days: ${car.rental_cost(3)}")
print(f"\nrental cost for Yamaha R1 for 5 days: ${bike.rental_cost(5)}")


car.set_rental_price_per_days(55)
print(f"modified rental price for Toyota Corolla: ${car.set_rental_price_per_days(55)}")
