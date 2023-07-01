"""
RAVIKANT
ravikantsinghsta@gmail.com
+919411603110
Senior Engineer - Amantya Technologies, Inc
(4 Year Experience)
"""

from datetime import datetime


class Car:
    def __init__(self, category, mileage):
        self.category = category
        self.mileage = mileage
        self.is_available = True


class CarRentalService:
    def __init__(self):
        self.cars = []
        self.bookings = []

    def add_car(self, category, mileage):
        car = Car(category, mileage)
        self.cars.append(car)

    def available_car(self, category):
        for car in self.cars:
            if car.category == category and car.is_available == True:
                return car
        return None

    def rent_car(self, customer_name, category, start_time, mileage):
        car = self.available_car(category)
        if car is not None:
            car.is_available = False
            booking_number = len(self.bookings) + 1
            rental = Rental(booking_number, customer_name, car, start_time, mileage)
            self.bookings.append(rental)
            return f"Car rented successfully.\nBooking number: {booking_number}"
        else:
            return f"No {category} car available for rent."

    def return_car(self, booking_number, return_time, mileage):
        rental = self.find_rental_by_booking_number(booking_number)
        if rental is not None:
            car = rental.car
            car.is_available = True
            rental.return_time = return_time
            rental.return_mileage = mileage
            rental.calculate_price()
            return rental.get_price_details()
        else:
            return "Invalid booking number"

    def find_rental_by_booking_number(self, booking_number):
        for rental in self.bookings:
            if str(rental.booking_number) == booking_number:
                return rental
        return None


class Rental:
    base_day_rental = 50
    kilometerPrice = 10

    def __init__(self, booking_number, customer_name, car, start_time, mileage):
        self.booking_number = booking_number
        self.customer_name = customer_name
        self.car = car
        self.start_time = start_time
        self.mileage = mileage
        self.return_time = None
        self.return_mileage = None
        self.price = None

    def calculate_price(self):
        rental_duration = self.return_time - self.start_time
        numberOfDays = rental_duration.days
        numberOfKilometers = self.return_mileage - self.mileage

        if self.car.category == "Compact":
            self.price = Rental.base_day_rental * numberOfDays
        elif self.car.category == "Premium":
            self.price = ((Rental.base_day_rental * numberOfDays * 1.2) + (Rental.kilometerPrice * numberOfKilometers))
        elif self.car.category == "Minivan":
            self.price = ((Rental.base_day_rental * numberOfDays * 1.7)+ (Rental.kilometerPrice * numberOfKilometers * 1.5))

    def get_price_details(self):
        return f"Booking Number: {self.booking_number}\nCustomer Name: {self.customer_name}\nRental Category: {self.car.category}\nRental Duration: {self.get_rental_duration()} days\nRental Price: {self.price} Rupees"

    def get_rental_duration(self):
        return (self.return_time - self.start_time).days


# Test Cases
if __name__ == "__main__":
    rental_service = CarRentalService()

    # Add cars
    rental_service.add_car("Compact", 5000)
    rental_service.add_car("Premium", 8000)
    rental_service.add_car("Minivan", 10000)


    #Rental registration
    Customername = "Ravikant"
    Carcategory = "Compact"
    start_time = datetime(2023, 7, 1, 10, 0, 0)
    Carmileage = 5000
    booking_number = rental_service.rent_car(Customername, Carcategory, start_time, Carmileage)
    print(booking_number)
    """
    Output :
    Car rented successfully. Booking number: 1
    """

    # Car Return
    # booking_number = 1
    return_time = datetime(2023, 7, 3, 12, 0, 0)
    Currentmileage = 5500
    price_details = rental_service.return_car(booking_number.split(": ")[1], return_time, Currentmileage)
    print(price_details)
    """
    Output :
    Booking number: 1
    Booking Number: 1
    Customer Name: Ravikant
    Rental Category: Compact
    Rental Duration: 2 days
    Rental Price: 100 Rupees
    """

