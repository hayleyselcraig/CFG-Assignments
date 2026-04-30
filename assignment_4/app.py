# Import Flask (used to create the API) and jsonify (used to return JSON responses)
from flask import Flask, jsonify, request

# Import the function that gets data from the database
from db_utils import get_activities, add_activity

# Create the Flask application
app = Flask(__name__)


# Helper function to convert one database row into a dictionary (JSON-friendly format)
def format_activity_response(activity_row):
    """Format one database row into a JSON-friendly dictionary."""

    # If no data is returned, return nothing
    if not activity_row:
        return None

    # Convert tuple from database into a dictionary
    return {
        "activity_id": activity_row[0],
        "activity_type": activity_row[1],
        "activity_date": str(activity_row[2]),  # Convert date to string so it can be returned as JSON
        "activity_description": activity_row[3]
    }


# =========================
# GET ALL ACTIVITIES
# =========================
# Endpoint: /activities
# This returns all dog care activities from the database
@app.route("/activities", methods=["GET"])
def activities():

    # Print message to user
    print("GET /activities - Retrieve all dog care activities")

    # Call function from db_utils.py to get all rows from database
    activities_list = get_activities()

    # Create empty list to store formatted results
    formatted_activities = []

    # Loop through each row returned from database
    for row in activities_list:

        # Convert each row into dictionary format using helper function
        activity = format_activity_response(row)

        # Only add if data exists
        if activity:
            formatted_activities.append(activity)

    # Return a structured JSON response using jsonify()
    return jsonify({
        "status": "success",
        "message": f"Retrieved {len(formatted_activities)} activities",
        "data": formatted_activities,
        "count": len(formatted_activities)
    }), 200   # 200 = success


# =========================
# GET ONE ACTIVITY BY ID
# =========================
# Endpoint: /activities/<id>
# Example: /activities/2
@app.route("/activities/<int:id>", methods=["GET"])
def activity_by_id(id):

    # Print message showing which ID is being requested
    print(f"GET /activities/{id} - Retrieve one dog care activity")

    # Call database function and pass the ID
    activity_row = get_activities(id)

    # If no result found, return error message
    if not activity_row:
        return jsonify({
            "status": "error",
            "message": "Activity ID not found"
        }), 404   # 404 = not found

    # get_activities(id) returns a list, so take the first item
    row = activity_row[0]

    # Convert row into dictionary format
    activity = format_activity_response(row)

    # Return formatted result
    return jsonify({
        "status": "success",
        "message": "Retrieved activity",
        "data": activity
    }), 200

# =========================
# CREATE NEW ACTIVITY
# =========================
# Endpoint: /activities
# Method: POST
# This receives new dog care activity data and adds it to the database.
@app.route("/activities", methods=["POST"])
def create_activity():
    print("Creating new activity")

    data = request.get_json()

    if not data:
        return jsonify({
            "status": "error",
            "message": "No JSON data received"
        }), 400

    required_fields = ["activity_type", "activity_date", "activity_description"]

    for field in required_fields:
        if field not in data:
            return jsonify({
                "status": "error",
                "message": f"Missing required field: {field}"
            }), 400

    activity_type = data["activity_type"]
    activity_date = data["activity_date"]
    activity_description = data["activity_description"]

    # Add the new activity to the database and store the new ID
    new_id = add_activity(activity_type, activity_date, activity_description)

    # If the database insert failed (no ID returned), return a server error response
    if not new_id:
        return jsonify({
            "status": "error",
            "message": "Failed to add activity"
        }), 500  # 500 = internal server error

    return jsonify({
        "status": "success",
        "message": "Activity added successfully",
        "data": {
            "activity_id": new_id
        }
    }), 201

# =========================
# RUN THE APP
# =========================
# This runs the Flask server when the file is executed
if __name__ == "__main__":
    app.run(debug=True)  # debug=True shows errors and auto-restarts server