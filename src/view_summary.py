import csv

def view_summary():
    total_study = 0
    total_sleep = 0
    count = 0

    with open("data/mood_data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                total_study += float(row[2])
                total_sleep += float(row[3])
                count += 1

    if count == 0:
        print("No data available.")
    else:
        print("📊 Weekly Summary")
        print("Average Study Hours:", total_study / count)
        print("Average Sleep Hours:", total_sleep / count)

view_summary()
