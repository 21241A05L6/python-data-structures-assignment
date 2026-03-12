import numpy as np

marks = np.array([78, 85, 90, 66, 72, 88, 95, 60])

sorted_marks = np.sort(marks)

print("Sorted:", sorted_marks)

print("25th percentile:", np.percentile(marks, 25))
print("50th percentile:", np.percentile(marks, 50))
print("75th percentile:", np.percentile(marks, 75))

average = np.mean(marks)

above_average = marks[marks > average]

print("Students above average:", len(above_average))