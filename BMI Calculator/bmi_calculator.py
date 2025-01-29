import json

# Data file to store BMI data
DATA_FILE = "bmi_data.json"

# Load existing data or initialize
try:
    with open(DATA_FILE, "r") as file:
        user_data = json.load(file)
except FileNotFoundError:
    user_data = {}

# Save data to file
def save_data():
    with open(DATA_FILE, "w") as file:
        json.dump(user_data, file)

# Calculate BMI
def calculate_bmi():
    try:
        weight = float(input("Enter your weight (in kg): "))
        height = float(input("Enter your height (in cm): ")) / 100  # Convert cm to meters
        bmi = round(weight / (height ** 2), 2)
        print(f"Your BMI: {bmi}")

        # Interpret BMI result
        if bmi < 18.5:
            interpretation = "Underweight"
        elif 18.5 <= bmi < 24.9:
            interpretation = "Normal weight"
        elif 25 <= bmi < 29.9:
            interpretation = "Overweight"
        else:
            interpretation = "Obesity"
        print(f"Category: {interpretation}")

        # Save data for the user
        username = input("Enter your username: ").strip()
        if username:
            if username not in user_data:
                user_data[username] = []
            user_data[username].append({"weight": weight, "height": height * 100, "bmi": bmi})
            save_data()
            print("BMI data saved successfully.")
        else:
            print("Error: Please enter a valid username.")
    except ValueError:
        print("Error: Please enter valid numbers for weight and height.")

# Show user history
def show_history():
    username = input("Enter your username to view history: ").strip()
    if username in user_data:
        history = user_data[username]
        print(f"BMI History for {username}:")
        for entry in history:
            print(f"  - Weight: {entry['weight']} kg, Height: {entry['height']} cm, BMI: {entry['bmi']}")
    else:
        print("No data found for this user.")

# Show BMI trend
def show_trend():
    import matplotlib.pyplot as plt

    username = input("Enter your username to view BMI trend: ").strip()
    if username in user_data:
        history = user_data[username]
        bmi_values = [entry['bmi'] for entry in history]
        timestamps = list(range(1, len(bmi_values) + 1))

        plt.figure(figsize=(8, 5))
        plt.plot(timestamps, bmi_values, marker="o", label="BMI")
        plt.title(f"BMI Trend for {username}")
        plt.xlabel("Record Number")
        plt.ylabel("BMI")
        plt.legend()
        plt.grid(True)
        plt.show()
    else:
        print("No data found for this user.")

# Main menu
def main_menu():
    while True:
        print("\n--- BMI Calculator ---")
        print("1. Calculate BMI")
        print("2. View History")
        print("3. Show BMI Trend")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            calculate_bmi()
        elif choice == "2":
            show_history()
        elif choice == "3":
            show_trend()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
