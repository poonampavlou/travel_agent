# Hotel costs include a standard cost for all countries and is multiplied by the number of nights chosen by the user.
def hotel_cost(num_nights):
    total_hotel_cost = num_nights * 100
    print(f"For {num_nights} nights at {city_flight} your total hotel cost will be £{total_hotel_cost}")
    return total_hotel_cost


# Rather than an if/elif statement, I found dictionaries a more efficient way to write the code
# for obtaining a price for the plane ticket. It would also allow for future flexibility if needing to add
# more flight prices to the dictionary rather than if/elif which would generate additional lines of coding.
def plane_cost(city_flight):
    plane_price_dict = {"Paris": 100, "London": 80, "Toronto": 700, "Goa": 800, "Nepal": 650, "Tokyo": 1000}
    plane_price = plane_price_dict[city_flight]
    print(f"For a trip to {city_flight} your plane ticket will be £{plane_price}")
    return plane_price


# Same as plane_cost comment but with rental_days instead. I chose to also vary the figures based on country.
def car_rental(rental_days):
    rental_price_dict = {"Paris": 50, "London": 50, "Toronto": 70, "Goa": 35, "Nepal": 30, "Tokyo": 90}
    rental_price = rental_price_dict[city_flight]
    total_car_rental = rental_price * rental_days
    print(f"Renting a car in {city_flight} for {rental_days} days will cost you £{total_car_rental}")
    return total_car_rental


# As the functions return a figure, within the holiday_cost function the outputs of the functions are summed together.
def holiday_cost(hotel_cost, plane_cost, car_rental):
    total_holiday_cost = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
    print(f"The total cost of your holiday is £{total_holiday_cost}")
    return total_holiday_cost


# List of cities created, so they can be nicely displayed for the user.
# This allows for future additions/amendments to the cities list to be done easily.
cities = ["Paris", "London", "Toronto", "Goa", "Nepal", "Tokyo"]

# The initial questions are within a while loop to allow for error handling.
while True:
    print("Please confirm your destination from the following options:")
    for i in range(len(cities)):
        print(cities[i])
    city_flight = input("Please enter your choice here: ").capitalize()
    if city_flight not in cities:
        print("Invalid input, please try again")
        continue
    else:
        break

# Same as above but the below is intended to spot any errors in relation to value errors or if the user enters
# that they wish to rent a car for longer than the stay of their holiday.
while True:
    try:
        num_nights = int(input(f"Please confirm how many nights you will be staying at {city_flight}: "))
        rental_days = int(input("Please confirm how many days you plan on hiring a car during your trip: "))
    except ValueError:
        print("Invalid input, please try again")
        continue
    if rental_days > num_nights:
        print(f"You are renting a dar for {rental_days} days but are only going to {city_flight} for "
              f"{num_nights} days; please try again")
    else:
        break

holiday_cost(hotel_cost, plane_cost, car_rental)
