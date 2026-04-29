# app.py = Flask server / API
# This file defines the API endpoints for the Dog Care Tracker.
# It receives requests from the main.py and calls functions
# from db_utils.py, and returns database results in a JSON-friendly format.

from flask import Flask
from db_utils import get_activities

app = Flask(__name__)


# GET /activities
# Retrieves all dog care activity records from the MySQL database.
@app.route("/activities", methods=["GET"])
def activities():
    activities_list = get_activities()

    formatted_activities = []

    # Convert each database row into a dictionary so it is easier to read as JSON.
    for row in activities_list:
        activity = {
            "activity_id": row[0],
            "activity_type": row[1],
            "activity_date": str(row[2]),
            "activity_description": row[3]
        }

        formatted_activities.append(activity)

    return formatted_activities


# GET /activities/<id>
# Retrieves one specific activity using its activity_id.
# Example: /activities/2 returns the activity with ID 2.
@app.route("/activities/<int:id>", methods=["GET"])
def activity_by_id(id):
    activity_row = get_activities(id)

    # get_activities(id) returns a list containing one row, so [0] selects that row.
    row = activity_row[0]

    activity = {
        "activity_id": row[0],
        "activity_type": row[1],
        "activity_date": str(row[2]),
        "activity_description": row[3]
    }

    return activity


# Runs the Flask development server when this file is run directly.
if __name__ == "__main__":
    app.run(debug=True)