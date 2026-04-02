# This program creates a personalised Disney Day Park Planner for the user.

# This program uses the built-in 'random' module to generate a random number.
# The random number is used to make each Disney username unique. 
# No installation is required as 'random' is included with Python.
import random 

# The requests module is used to send HTTP requests to the Disney API. 
# To install it, run: python3 -m pip install requests 
import requests 

# --------------------------------------------------
# FUNCTION: Get character information from API
# --------------------------------------------------
# This function uses the free Disney API to retrieve information about the user's chosen character. 
# It transforms the JSON response into a simple, user-friendly message. 
# No API key is required.
def get_character_info(character_name):

    # Create the API URL by inserting the user's character into the query
    url = f"https://api.disneyapi.dev/character?name={character_name}"

    try:
        # Send a GET request to the API and store the response
        response = requests.get(url)

        # Convert the JSON response into a Python dictionary so we can access the data
        api_data = response.json()

        # Check if the API returned any results
        # The "data" key contains a list of matching characters
        if "data" in api_data and len(api_data["data"]) > 0:

            # Select the first character from the results list
            # (the API may return multiple matches)
            character = api_data["data"][0]

            # Store the character's name
            name = character["name"]

            # Check if the character has any films listed
            # If yes, take the first one, otherwise use fallback text
            if character["films"]:
                film = character["films"][0]
            else:
                film = "a Disney film"

            # Start building a personalised message for the user
            message = (
                f"Good choice! {name} is a fun character!\n"
                f"They also appear in {film}.\n"
            )

            # Check if the character appears in any park attractions
            if character["parkAttractions"]:
                attraction = character["parkAttractions"][0]

                # Add attraction information to the message
                message += f"You will find them at this attraction in the park: {attraction}.\n"
            else:
                # If no attractions exist, provide a fallback message
                message += "No additional park information found in the API.\n"

        else:
            # If the API returned no matching characters
            message = "No information found for this character.\n"

    except Exception:
        # If there is an error connecting to the API (e.g. no internet)
        message = "Error retrieving data from the API.\n"

    # Display the message to the user
    print("\n" + message)

    # Return the message so it can also be saved to a file later
    return message


# --------------------------------------------------
# FUNCTION: Create a Disney username
# --------------------------------------------------
# This function generates a unique username using:
# - part of the user's name (string slicing)
# - a themed word based on their chosen park
# - a random number for uniqueness
def create_username(name, selected_park):

    # Take the first 3 letters of the user's name
    # .capitalize() ensures the first letter is uppercase
    name_part = name[:3].capitalize()

    # Select a themed word depending on the chosen park
    if selected_park == "Magic Kingdom":
        fun_word = "Magic"
    elif selected_park == "Animal Kingdom":
        fun_word = "Explorer"
    elif selected_park == "Epcot":
        fun_word = "Dreamer"
    elif selected_park == "Hollywood Studios":
        fun_word = "Hero"

    # Generate a random number between 1 and 99
    # This ensures each username is slightly different
    number = random.randint(1, 99)

    # Combine all parts into one string
    return name_part + fun_word + str(number)


# --------------------------------------------------
# FUNCTION: Display park plan
# --------------------------------------------------
# This function takes the selected park and dictionary of parks,
# retrieves the activities, and displays them clearly to the user.
def display_plan(selected_park, parks):

    # Access the list of activities using the park name as the key
    activities = parks[selected_park]

    # Display each activity using list indexes:
    # [0] = ride, [1] = character, [2] = show
    print("\nYour plan for " + selected_park + ":")
    print("Ride:", activities[0])
    print("Character meet & greet:", activities[1])
    print("Show:", activities[2])


# --------------------------------------------------
# MAIN PROGRAM
# --------------------------------------------------

# Dictionary storing each Disney park with a ride, character, and show
# This acts as a simple data structure to organise park information
parks = {
    "Magic Kingdom": ["Seven Dwarfs Mine Train", "Mickey Mouse", "Happily Ever After Fireworks"],
    "Animal Kingdom": ["Expedition Everest", "Rafiki", "Festival of the Lion King"],
    "Epcot": ["Soarin' Around the World", "Moana", "The American Adventure"],
    "Hollywood Studios": ["The Twilight Zone Tower of Terror", "Buzz Lightyear", "Fantasmic Nighttime Spectacular"]
}

# Welcome message to introduce the program
print("Welcome to the Disney Day Park Planner!")

# Ask the user for their name
name = input("What is your name? ")

# Ask for favourite character (with suggestions for better API results)
fav_character = input("What is your favourite Disney character? (Try: Stitch, Simba, Olaf, Moana)\n")

# Call the API function and store the returned message
# This allows reuse later when writing to a file
character_info = get_character_info(fav_character)

# Ask what type of Disney day the user wants
park_day = input("What kind of Disney park day do you want?\n- magical\n- adventurous\n- relaxing\n- fun\n")

# Convert input to lowercase to make comparisons consistent
park_day = park_day.lower()

# List of valid options for input validation
valid_choices = ["magical", "adventurous", "relaxing", "fun"]

# Boolean variable used to check if input is valid
is_valid_day = park_day in valid_choices

# Loop continues until user enters a valid option
while not is_valid_day:
    print("Invalid choice, please try again.")
    park_day = input("What kind of Disney park day do you want?\n- magical\n- adventurous\n- relaxing\n- fun\n").lower()

    # Update boolean after new input
    is_valid_day = park_day in valid_choices

# Set a default value to ensure the variable always has data
selected_park = "Magic Kingdom"

# Use selection (if/elif) to match user choice to a park
if park_day == "magical":
    selected_park = "Magic Kingdom"
elif park_day == "adventurous":
    selected_park = "Animal Kingdom"
elif park_day == "relaxing":
    selected_park = "Epcot"
elif park_day == "fun":
    selected_park = "Hollywood Studios"

# Generate a unique Disney username
disney_username = create_username(name, selected_park)

# Display results back to the user
print("\nHello", name)
print("Your favourite character is", fav_character)
print("You chose this type of day:", park_day)
print("Your chosen park is:", selected_park)
print("Your Disney username is:", disney_username)

# Display the final park plan
display_plan(selected_park, parks)

# --------------------------------------------------
# FILE OUTPUT
# --------------------------------------------------
# Save the results to a text file so the user can access it later
with open("disney_day_plan.txt", "w") as file:

    # Write headings and user details
    file.write("Disney Day Park Planner\n")
    file.write("-----------------------\n")
    file.write(f"Name: {name}\n")
    file.write(f"Favourite character: {fav_character}\n\n")

    # Write API information
    file.write("Character Information:\n")
    file.write(character_info + "\n")

    # Write park and username details
    file.write(f"Chosen day type: {park_day}\n")
    file.write(f"Chosen park: {selected_park}\n")
    file.write(f"Disney username: {disney_username}\n\n")

    # Write the park plan
    file.write(f"Plan for {selected_park}:\n")
    file.write(f"Ride: {parks[selected_park][0]}\n")
    file.write(f"Character meet & greet: {parks[selected_park][1]}\n")
    file.write(f"Show: {parks[selected_park][2]}\n")

# Confirm file creation to the user
print("\nYour Disney plan has been saved to disney_day_plan.txt")