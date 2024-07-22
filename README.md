# City Guessing Game

## Overview

The City Guessing Game is a simple Python-based game where the player tries to guess a randomly selected city from a predefined list of major cities in the USA. The game provides feedback on how far the guessed city is from the correct city, helping the player to make better guesses in subsequent attempts.

## How It Works

1. **Initialization**:
    - The game starts by initializing a list of major cities in the USA along with their geographical coordinates (latitude and longitude).

2. **Random City Selection**:
    - A city is randomly selected from the list to be the correct answer for that game session.

3. **User Interaction**:
    - The player is shown a list of possible city names to choose from.
    - The player is prompted to guess the city by entering the city name.

4. **Distance Calculation**:
    - If the guessed city is not the correct city, the game calculates the distance between the guessed city and the correct city using the Haversine formula.
    - The player is informed of the distance and can use this information to make more informed guesses.

5. **Game Continuation**:
    - The game continues until the player correctly guesses the city.





