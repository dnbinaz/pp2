import csv
# Sample data
data = [
    ("John", "Doe", "1234567890"),
    ("Jane", "Smith", "09870056797"),
    ("Alice", "Johnson", "5576123055"),
    ("Asylniet", "Zhon", "1206785606"),
    ("Kim", "Duke", "9876504321"),
    ("Nate", "Rimson", "5243455751")
]

# File path to save the CSV file
filename = "data.csv"

# Writing data to the CSV file
with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["First Name", "Last Name", "Phone Number"])  # Writing header
    writer.writerows(data)  # Writing rows of data

print("CSV file created successfully:", filename)