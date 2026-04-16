# 🎢 Assignment 2 – Disney Day Park Planner

## 📌 Overview

This project is a **console-based Python application** that creates a personalised Disney park day plan for the user.

The program interacts with a **free Disney API** to retrieve character information and combines it with user input to generate a customised experience. The final plan is displayed in the console and saved to a text file.

This project demonstrates the use of **APIs, functions, data structures, loops, and file handling** in Python.

---

## 🎯 Features

* Personalised Disney day planner based on user input
* Retrieves real character data from an API
* Generates a unique Disney username
* Displays a structured park plan (ride, character, show)
* Saves results to a text file for later use

---

## ✅ Assignment Requirements Met

- **API integration (Disney API)**  
  Example: `requests.get(url)` → `.json()`

- **Boolean + if/else logic**  
  Example: `if park_day == "magical"`

- **Data structures (dictionary & lists)**  
  Example: `parks = {"Magic Kingdom": ["Ride", "Character", "Show"]}`

- **Loop (while loop for validation)**  
  Example: `while not is_valid_day:`

- **Functions with return values**  
  Example: `return message`

- **String slicing**  
  Example: `name[:3]`

- **Built-in functions**  
  Example: `input()`, `print()`, `len()`

- **External modules**  
  Example: `requests` (API), `random` (username)

- **API comments included**  
  Example: explains setup + no API key needed

- **File handling (output to file)**  
  Example: `open("disney_day_plan.txt", "w")`
---

## 🌐 API Used

This project uses the free Disney API:

👉 https://api.disneyapi.dev/

### How it is used:

* Sends a **GET request** using the `requests` module
* Retrieves character data in **JSON format**
* Extracts:

  * Character name
  * Film appearance
  * Park attractions (if available)
* Converts this into a **user-friendly message**

No API key is required.

---

## 📦 Requirements

### Python Version

* Python 3.x

### Install Dependencies

The program uses the `requests` module (not built-in).

Install it using:

```bash
pip install requests
```

---

## ▶️ How to Run the Program

1. Open a terminal in the project folder
2. Run the program:

```bash
python3 disney_application.py
```

3. Follow the prompts:

   * Enter your name
   * Choose a Disney character
   * Select your preferred type of park day

---

## 📁 Project Structure

* `disney_application.py` → Main program file
* `disney_day_plan.txt` → Output file with saved results
* `requirements.txt` → Project dependencies

---

## 💾 Output

The program generates a file:

```
disney_day_plan.txt
```

This file includes:

* User details
* Character information from the API
* Selected park and plan
* Generated Disney username

---

## 🎨 Creativity

This project takes a creative approach by:

* Combining API data with a **theme park planning scenario**
* Generating a **fun, personalised Disney username**
* Providing an engaging and interactive user experience

---

## 📝 Notes

* Internet connection is required for API access
* If the API fails, the program handles errors gracefully
* Some characters may not have full data available

---

## 👩‍💻 Author

Hayley Selcraig

---
