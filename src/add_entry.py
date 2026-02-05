import csv
from datetime import date

def add_entry():
    mood = input("Enter your mood (Happy/Neutral/Sad): ")
    study_hours = input("Enter study hours: ")
    sleep_hours = input("Enter sleep hours: ")

    today = date.today()

    with open("data/mood_data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([today, mood, study_hours, sleep_hours])

    print("✅ Entry added successfully!")

add_entry()
