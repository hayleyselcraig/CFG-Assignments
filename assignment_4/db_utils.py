# Import mysql connector so Python can connect to a MySQL database
import mysql.connector

# Import database connection details from config file
# db_config is a dictionary containing host, user, password, database name
from config import db_config


# =========================
# DATABASE CONNECTION
# =========================
def connect_to_database():
    """
    Creates a connection to the MySQL database
    and returns both the connection (db) and cursor.
    The cursor is used to execute SQL queries.
    """

    # Initialise variables (helps avoid errors if something fails later)
    db = None
    cursor = None

    try:
        # Print message to terminal to show connection attempt
        print("Connecting to database...")

        # Create connection using values stored in db_config
        db = mysql.connector.connect(
            host=db_config["host"],        # database server (usually localhost)
            user=db_config["user"],        # MySQL username
            password=db_config["password"],# MySQL password
            database=db_config["database"] # database name (dog_tracker)
        )

        # Create a cursor object which allows us to run SQL commands
        cursor = db.cursor()

        print("Connected to database.")

        # Return both connection and cursor so other functions can use them
        return db, cursor

    except mysql.connector.Error as err:
        # If connection fails, print error and return None values
        print("Failed to connect to database.")
        print(err)
        return None, None


# =========================
# GET ACTIVITIES
# =========================
def get_activities(id=None):
    """
    Retrieves activities from the database.
    - If an ID is provided → return one activity
    - If no ID → return all activities
    """

    db = None
    cursor = None

    try:
        # Open database connection
        db, cursor = connect_to_database()

        # If connection failed, stop the function early
        if not db or not cursor:
            return None

        # If an ID is provided, filter the query
        if id is not None:
            cursor.execute(
                "SELECT * FROM activities WHERE activity_id = %s",
                (id,)  # tuple format required for SQL parameters
            )
        else:
            # Otherwise, return all records
            cursor.execute("SELECT * FROM activities")

        # Fetch all results returned from the query
        # Results will be a list of tuples
        results = cursor.fetchall()

        return results

    except mysql.connector.Error as err:
        # Handle any errors during query execution
        print("Failed to retrieve activities")
        print(err)
        return None

    finally:
        # Always close cursor and database connection
        if cursor:
            cursor.close()
        if db:
            db.close()


# =========================
# ADD NEW ACTIVITY
# =========================
def add_activity(activity_type, activity_date, activity_description):
    """
    Inserts a new activity into the database.
    Returns the ID of the newly created record.
    """

    db = None
    cursor = None

    try:
        # Open database connection
        db, cursor = connect_to_database()

        # If connection failed, stop execution
        if not db or not cursor:
            return None

        # SQL INSERT query (adds new record to table)
        query = """
        INSERT INTO activities (activity_type, activity_date, activity_description)
        VALUES (%s, %s, %s)
        """

        # Values to insert into the query
        values = (activity_type, activity_date, activity_description)

        # Execute the query using the values provided
        cursor.execute(query, values)

        # Commit saves the changes to the database
        db.commit()

        # Get the ID of the newly inserted row
        new_id = cursor.lastrowid

        print(f"Activity added successfully with ID {new_id}")

        # Return the new ID so it can be used in app.py
        return new_id

    except mysql.connector.Error as err:
        # Handle any database errors
        print("Failed to add activity")
        print(err)
        return None

    finally:
        # Always close cursor and connection after use
        if cursor:
            cursor.close()
        if db:
            db.close()