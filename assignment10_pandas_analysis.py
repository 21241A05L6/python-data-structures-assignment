import pandas as pd

# -----------------------------
# Task 1: Pandas Series Basics
# -----------------------------

marks = [78, 85, 90, 66, 72]

series = pd.Series(marks)

print("Series values:")
print(series.values)

print("Index:")
print(series.index)

print("Data type:")
print(series.dtype)

print("First element:")
print(series.iloc[0])

print("Last two elements:")
print(series.iloc[-2:])


# --------------------------------------
# Task 2: Mathematical Operations
# --------------------------------------

print("Add 5 marks:")
print(series + 5)

print("Subtract 2 marks:")
print(series - 2)

print("Multiply by 1.05:")
print(series * 1.05)

print("Divide by 2:")
print(series / 2)


# --------------------------------------
# Task 3: Python Functionalities
# --------------------------------------

print("Maximum:", series.max())
print("Minimum:", series.min())
print("Sum:", series.sum())
print("Mean:", series.mean())

passed = series.apply(lambda x: x >= 70)

print("Passed students:")
print(passed)

print("Number of students passed:")
print(passed.sum())


# --------------------------------------
# Task 4: Create DataFrame
# --------------------------------------

students = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks': [78, 85, 90, 66, 72],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}

df = pd.DataFrame(students)

print("First 3 rows:")
print(df.head(3))

print("Last 2 rows:")
print(df.tail(2))

print("Shape:", df.shape)
print("Columns:", df.columns)


# --------------------------------------
# Task 5: DataFrame Functions
# --------------------------------------

print("Info:")
print(df.info())

print("Describe:")
print(df.describe())

print("Head:")
print(df.head())

print("Tail:")
print(df.tail())

sorted_df = df.sort_values(by="Marks", ascending=False)

print("Sorted by marks:")
print(sorted_df)

sorted_df = sorted_df.reset_index(drop=True)

print("After resetting index:")
print(sorted_df)


# --------------------------------------
# Task 6: Filtering
# --------------------------------------

print("Marks > 75")
print(df[df["Marks"] > 75])

print("Subject = Math")
print(df[df["Subject"] == "Math"])

print("Marks > average")
print(df[df["Marks"] > df["Marks"].mean()])

print("Failed students")
print(df[df["Marks"] < 70])


# --------------------------------------
# Task 7: Grouping
# --------------------------------------

print("Average marks per subject")
print(df.groupby("Subject")["Marks"].mean())

print("Students per subject")
print(df.groupby("Subject")["Name"].count())

print("Max marks per subject")
print(df.groupby("Subject")["Marks"].max())


# --------------------------------------
# Task 8: Simple Plotting
# --------------------------------------

df.plot(x="Name", y="Marks", kind="bar", title="Marks by Student")

df["Marks"].plot(kind="line", title="Marks Line Graph")

df["Marks"].plot(kind="hist", title="Marks Distribution")


# --------------------------------------
# Task 9: Sales Data Analysis
# --------------------------------------

sales = {
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    'Revenue': [1200, 1500, 900, 2000, 1800]
}

sales_df = pd.DataFrame(sales)

print("Total revenue:", sales_df["Revenue"].sum())

print("Average revenue:", sales_df["Revenue"].mean())

print("Day with highest revenue:")
print(sales_df.loc[sales_df["Revenue"].idxmax()])

print("Revenue > average:")
print(sales_df[sales_df["Revenue"] > sales_df["Revenue"].mean()])

sales_df.plot(x="Day", y="Revenue", kind="line", title="Revenue vs Day")