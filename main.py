import random
from geopy.distance import geodesic

# List of cities with their coordinates
cities = {
    "New York": (40.7128, -74.0060),
    "Los Angeles": (34.0522, -118.2437),
    "Chicago": (41.8781, -87.6298),
    "Houston": (29.7604, -95.3698),
    "Phoenix": (33.4484, -112.0740),
    "Philadelphia": (39.9526, -75.1652),
    "San Antonio": (29.4241, -98.4936),
    "San Diego": (32.7157, -117.1611),
    "Dallas": (32.7767, -96.7970),
    "San Jose": (37.3382, -121.8863)
}

# Choose a random city
correct_city = random.choice(list(cities.keys()))
correct_coords = cities[correct_city]

print("Guess the city! Here are your options:")
for city in cities.keys():
    print(city)

while True:
    guess = input("\nEnter the name of a city: ")
    
    if guess not in cities:
        print("Invalid city. Please choose from the list.")
        continue
    
    guess_coords = cities[guess]
    
    distance = geodesic(correct_coords, guess_coords).miles
    
    if guess == correct_city:
        print(f"Congratulations! You've guessed the correct city: {correct_city}.")
        break
    else:
        print(f"That's not the correct city. You are {distance:.2f} miles away from the correct city.")

