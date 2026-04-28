## Import mysql connector so python can connect to MySQL database.
import mysql.connector

## Import database login details from config file
## (host, user, password and database name)
from config import db_config


## Function to connect to the dog tracker database
def connect_to_database():

    ## Set variables to None first
    ## This prevents errors later in the finally block of code
    db = None
    cursor = None

    try:
        ## Let user know connection is starting
        print("Connecting to database...")

        ## Connect python to MySQL using details from config file
        db = mysql.connector.connect(
            host=db_config["host"],
            user=db_config["user"],
            password=db_config["password"],
            database=db_config["database"]
        )

        ## Cursor allows us to run SQL commands
        cursor = db.cursor()

        print("Connected to database.")

        return db, cursor

    except mysql.connector.Error as err:
        print("Failed to connect to database.")
        print(err)

    finally:
        ## This section can be used later for closing connection if needed
        pass

if __name__ == "__main__":
        connect_to_database()
