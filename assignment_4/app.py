# app.py = Flask server / API
# This file defines the endpoints.
# Example:
# GET /activities
# GET /activities/<id>
# POST /activities

# ========================================================
# APP STRUCTURE
# ========================================================
# This file is currently being used to build the Flask API
# structure and organise the required endpoints.
# Endpoints will be tested using Postman/browser first to
# confirm they work correctly before connecting to the
# MySQL database and client-side main.py file.
# Database queries will be added after endpoint testing.
# ========================================================

# ========================================================
# ENDPOINT PLAN
# ========================================================
# GET /activities
# Retrieves all dog care activity records from the database
# and returns them as a list (walks, feeding, grooming etc).
#
# GET /activities/1
# Retrieves one specific activity using its activity_id.
# Example: /activities/1 returns the record with ID 1.
#
# POST /activities
# Sends new activity data to the API and inserts a new
# record into the database. Returns a success message
# once the activity has been added.
#
# GET /activities → SELECT * FROM database
# This means the endpoint will later use an SQL SELECT query
# to read all saved activity records from the MySQL database,
# because the information is stored there permanently rather
# than hard-coded inside the Python file.
# ========================================================