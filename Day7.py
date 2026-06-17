import csv

# writing some student data to a csv file
students = [
    ["name", "age", "grade", "score"],
    ["Aryan",  19, "A", 92],
    ["Priya",  20, "B", 78],
    ["Rohan",  18, "A", 95],
    ["Sneha",  21, "C", 61],
    ["Karan",  19, "B", 83],
    ["Divya",  20, "A", 88],
    ["Amit",   22, "C", 55],
    ["Pooja",  18, "B", 74],
    ["Vikram", 21, "A", 91],
    ["Meera",  19, "C", 48],
]

with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(students)

print("students.csv created")


# reading it back
with open("students.csv", "r") as f:
    reader = csv.reader(f)
    all_rows = list(reader)

header = all_rows[0]
data = all_rows[1:]

print("\nall students:")
for row in data:
    print(row)


# filtering - only keep students who scored 80 or above
is_high_scorer = lambda row: int(row[3]) >= 80
high_scorers = [row for row in data if is_high_scorer(row)]

print(f"\nhigh scorers ({len(high_scorers)} found):")
for row in high_scorers:
    print(row)


# saving the filtered results to a new file
with open("high_scorers.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(high_scorers)

print("\nhigh_scorers.csv created")