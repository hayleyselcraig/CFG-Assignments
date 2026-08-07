import requests

BASE_URL = "http://127.0.0.1:5000"

# GET ALL ACTIVITIES
def get_all_activities():
    try:
        # Send GET request to your Flask API
        response = requests.get(f"{BASE_URL}/activities")

        # Raise an error if request failed (e.g. 404, 500)
        response.raise_for_status()

        # Convert JSON response into Python dictionary
        data = response.json()

        print(f"\nRetrieved {data['count']} activities:\n")

        # Loop through each activity in the response
        for activity in data["data"]:
            print(
                f"{activity['activity_id']} - "
                f"{activity['activity_type']} on {activity['activity_date']}"
            )

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# GET ACTIVITY BY ID
def get_activity_by_id(activity_id):
    try:
        # Send GET request with the activity ID
        response = requests.get(f"{BASE_URL}/activities/{activity_id}")

        # Raise error if request failed
        response.raise_for_status()

        # Convert JSON response into Python dictionary
        data = response.json()

        activity = data["data"]

        print("\nActivity found:")
        print(
            f"{activity['activity_id']} - "
            f"{activity['activity_type']} on {activity['activity_date']}"
        )

    except requests.exceptions.HTTPError:
        print("Activity not found or invalid ID")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# CREATE NEW ACTIVITY
def create_activity():
    # Data we want to send to the API (must match database fields)
    new_activity = {
        "activity_type": "Training",
        "activity_date": "2026-05-26",
        "activity_description": "The process of teaching dogs specific skills and commands."
    }

    try:
        # Send POST request to API with JSON data
        response = requests.post(
            f"{BASE_URL}/activities",
            json=new_activity
        )

        # Raise error if something failed
        response.raise_for_status()

        # Convert response to dictionary
        data = response.json()

        print("\nActivity created successfully!")
        print(data)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def run():
    print("Welcome to Ellie’s Dog Care Tracker")

    get_all_activities()
    get_activity_by_id(2)
    create_activity()
    get_all_activities() # Function called again to show new activity has been added.


if __name__ == "__main__":
    run()