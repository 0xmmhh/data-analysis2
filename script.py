import csv

red_team = []
blue_team = []

with open('data.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        first_key = next(iter(row.keys()))
        if first_key.startswith('r'):
            red_team.append(row)
        elif first_key.startswith('b'):
            blue_team.append(row)

print("Red Team Data:")
for row in red_team:
    for key in row.keys():
        print(f"{key}: {row[key]}")
    print("-" * 20)

print("Blue Team Data:")
for row in blue_team:
    for key in row.keys():
        print(f"{key}: {row[key]}")
    print("-" * 20)
