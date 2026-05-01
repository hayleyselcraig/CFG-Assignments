# Assignment 4 | Ellie’s Dog Care Tracker API

A Python Flask API connected to a MySQL database that stores daily dog care activities such as walks, feeding, grooming, and vet visits.

---

## Meet Ellie 🐶

<p align="center">
  <img src="images/ellie.jpg" width="300">
</p>

This project was inspired by my dog Ellie. I wanted a simple way to keep track of her daily care routine, including walks, training, and vet visits. This API simulates how a real system could help dog owners monitor their pet’s activities and ensure consistent care.

---

## Technologies Used

* Python
* Flask
* Requests
* MySQL
* Postman (for API testing)

---

## About Flask

Flask is a lightweight Python web framework used to build the API in this project. It allows us to create endpoints that handle HTTP requests such as GET and POST.

In this application, Flask is used to:

* Retrieve data from the MySQL database (GET requests)
* Insert new activity data into the database (POST requests)
* Return responses in JSON format so they can be used by a client

---

## Project Files

* `app.py` – Flask API with endpoints
* `main.py` – Client-side script to interact with the API
* `db_utils.py` – Database connection and queries
* `config_example.py` – Database configuration example
* `dog_tracker.sql` – SQL file to create the database and table
* `images/ellie.jpg` – Image used in README

---

## Features

* View all activities
* View one activity by ID
* Add a new activity

---

## Testing with Postman

Postman was used to test the API endpoints during development.

It allowed manual testing of:

* GET requests to retrieve activities
* POST requests to add new activities

Example endpoints tested:

* GET http://127.0.0.1:5000/activities
* POST http://127.0.0.1:5000/activities

This helped confirm that the API was working correctly before implementing the client-side script.

---

## Client-Side Behaviour

The client-side is implemented in `main.py` using the Python `requests` library.

The client simulates user interaction with the API by:

* Sending requests to retrieve data
* Sending requests to create new activities
* Displaying results in the terminal

The activity data is currently hardcoded in the script rather than entered by the user. This approach was used to simulate API interaction as required by the assignment brief.

In a real-world application, this data would typically be entered through a user interface such as a web form.

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd assignment_4
```

---

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Mac
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Set up the database

* Open MySQL
* Run the SQL file:

```sql
SOURCE dog_tracker.sql;
```

---

### 5. Configure database connection

Copy `config_example.py` and rename it to `config.py`, then update it with your own database details:

```python
db_config = {
    "host": "localhost",
    "user": "your_username",
    "password": "your_password",
    "database": "dog_tracker"
}
```

---

## Running the Application

### Step 1: Start the Flask API

```bash
python app.py
```

This will run the API at:

http://127.0.0.1:5000

---

### Step 2: Run the client-side script

Open a new terminal and run:

```bash
python main.py
```

---

## Example Output

* Retrieves all activities
* Retrieves one activity by ID
* Adds a new activity
* Displays updated list of activities

---

## API Endpoints

| Method | Endpoint         | Description         |
| ------ | ---------------- | ------------------- |
| GET    | /activities      | Get all activities  |
| GET    | /activities/<id> | Get one activity    |
| POST   | /activities      | Create new activity |

---

## Notes

* The `config.py` file is not included in the repository for security reasons. A `config_example.py` file is provided instead.
* This project demonstrates API creation, database integration, and client-server interaction using Python.

---

