# Rahul-2500031051

import csv
import os
import matplotlib.pyplot as plt

FILE = "data/students.csv"


class Student:

    def __init__(self):
        os.makedirs("data", exist_ok=True)

        if not os.path.exists(FILE):
            with open(FILE, "w", newline="") as f:
                csv.writer(f).writerow(
                    ["id", "name", "class", "s1", "s2", "s3", "s4", "s5", "avg", "grade", "cgpa"]
                )

    def get_student_data(self, sid=None):
        if not sid:
            sid = input("ID: ")

        name = input("Name: ")
        cls = input("Class: ")

        marks = []
        for i in range(1, 6):
            marks.append(float(input(f"S{i}: ")))

        avg = sum(marks) / 5

        if avg >= 75:
            grade = "A"
        elif avg >= 50:
            grade = "B"
        else:
            grade = "C"

        cgpa = round(avg / 10, 2)

        return [sid, name, cls] + marks + [avg, grade, cgpa]
# leela abhay-2500031075
    def add_student(self):
        with open(FILE, "a", newline="") as f:
            csv.writer(f).writerow(self.get_student_data())
        print("Added!")
# sahithi-2500031089
    def display_students(self):
        with open(FILE, "r") as f:
            reader = csv.reader(f)
            data = list(reader)

        if len(data) <= 1:
            print("No records found")
            return

        header = data[0]
        rows = data[1:]

        widths = [len(h) for h in header]

        for row in rows:
            for i in range(len(row)):
                widths[i] = max(widths[i], len(str(row[i])))

        def format_row(row):
            return " | ".join(str(row[i]).ljust(widths[i]) for i in range(len(row)))

        print("\n" + format_row(header))
        print("-" * (sum(widths) + 3 * (len(widths) - 1)))

        for row in rows:
            print(format_row(row))
# akhil-2500031036
    def search_student(self):
        sid = input("ID: ")

        with open(FILE, "r") as f:
            reader = csv.reader(f)
            next(reader)

            for row in reader:
                if row[0] == sid:
                    print("\nRecord Found:")
                    print(",".join(row))
                    return

        print("Not found")

    def delete_student(self):
        sid = input("ID: ")
        rows = []

        with open(FILE, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] != sid:
                    rows.append(row)

        with open(FILE, "w", newline="") as f:
            csv.writer(f).writerows(rows)

        print("Deleted!")
# leela abhay-2500031075
    def update_student(self):
        sid = input("Enter ID: ")
        rows = []
        found = False

        with open(FILE, "r") as f:
            reader = csv.reader(f)
            header = next(reader)
            rows.append(header)

            for row in reader:
                if row[0] == sid:
                    print("Enter new details:")
                    rows.append(self.get_student_data(sid))
                    found = True
                else:
                    rows.append(row)

        if not found:
            print("Student not found")
            return

        with open(FILE, "w", newline="") as f:
            csv.writer(f).writerows(rows)

        print("Updated!")
# Rahul-2500031051
    def visualize_data(self):
        names = []
        avgs = []
        cgpas = []
        grades = {"A": 0, "B": 0, "C": 0}

        with open(FILE, "r") as f:
            reader = csv.reader(f)
            next(reader)

            for row in reader:
                names.append(row[1])
                avgs.append(float(row[8]))
                grades[row[9]] += 1
                cgpas.append(float(row[10]))

        if not names:
            print("No data found")
            return
            
        plt.figure(figsize=(10, 5))
        plt.bar(names, avgs)
        plt.title("Average Marks")
        plt.xlabel("Students")
        plt.ylabel("Average")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        
        plt.figure(figsize=(6, 6))
        plt.pie(
            grades.values(),
            labels=grades.keys(),
            autopct="%1.1f%%",
            startangle=90
        )
        plt.title("Grade Distribution")
        plt.show()

        
        plt.figure(figsize=(10, 5))
        plt.plot(names, cgpas, marker="o")
        plt.title("CGPA Report")
        plt.xlabel("Students")
        plt.ylabel("CGPA")
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        plt.show()
