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




