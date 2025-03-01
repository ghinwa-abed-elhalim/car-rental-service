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


