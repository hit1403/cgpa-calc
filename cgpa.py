import tkinter as tk

# Create a window
window = tk.Tk()
window.title("CGPA Calculator")

# Create a label for instructions
label = tk.Label(window, text="Enter the grades for each course and click Calculate")
label.pack()

# Define fixed credits for each semester
semester_credits = {
    1: [4, 4, 4, 4, 3, 2, 2, 2],
    2: [4, 4, 4, 3, 3, 2, 2, 2],
    3: [4, 4, 4, 4, 3, 2, 2, 2],
    4: [4, 3, 4, 4, 3, 2, 2, 2],
    5: [3, 4, 4, 3, 2, 2, 2, 4]
}

# Create a function to calculate the CGPA
def calculate():
    # Initialize the sum of GPA and total credits
    sum_gpa = 0
    total_credits = 0

    # Loop through the entries for each semester
    for semester, entries in zip(range(1, 6), [entries1, entries2, entries3, entries4, entries5]):
        # Initialize the sum of grade points for each semester
        sum_gp = 0

        # Loop through the entries for each course
        for entry, credit in zip(entries, semester_credits[semester]):
            # Get the grade from the entry
            grade = float(entry[0].get())

            # Calculate the grade point for each course
            gp = grade * credit

            # Add the grade point to the sum for each semester
            sum_gp += gp

        # Calculate the GPA for each semester
        gpa = sum_gp / sum(semester_credits[semester])

        # Add the GPA and credit to the sum for the CGPA
        sum_gpa += gpa * sum(semester_credits[semester])
        total_credits += sum(semester_credits[semester])

    # Calculate the CGPA
    cgpa = sum_gpa / total_credits

    # Display the CGPA in the result label
    result_label.config(text=f"CGPA = {cgpa:.2f}")

# Create frames for each semester and pack them horizontally
frames = []
for semester in range(1, 6):
    frame = tk.Frame(window)
    frame.pack(side="left", padx=10)
    frames.append(frame)

    # Create labels and entries for each semester
    label_semester = tk.Label(frame, text=f"Semester {semester}")
    label_semester.grid(row=0, column=0, columnspan=2)

    label_grade = tk.Label(frame, text="Grade")
    label_grade.grid(row=1, column=0)

    # Create a list to store the entries for each semester
    entries = []

    # Create entries for each course in the semester
    for i, credit in enumerate(semester_credits[semester]):
        entry_grade = tk.Entry(frame, width=5)
        entry_grade.grid(row=i + 2, column=0)
        # Append the entry to the list
        entries.append((entry_grade, credit))

    # Append the entries for each semester to the corresponding list
    if semester == 1:
        entries1 = entries
    elif semester == 2:
        entries2 = entries
    elif semester == 3:
        entries3 = entries
    elif semester == 4:
        entries4 = entries
    elif semester == 5:
        entries5 = entries

# Create a button to calculate the CGPA
button = tk.Button(window, text="Calculate", command=calculate)
button.pack()

# Create a label to show the result
result_label = tk.Label(window, text="CGPA = ")
result_label.pack()

# Start the main loop
window.mainloop()
