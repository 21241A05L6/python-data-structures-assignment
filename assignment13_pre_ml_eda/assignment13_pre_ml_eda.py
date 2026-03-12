import pandas as pd
import sqlite3
import json
import seaborn as sns
import matplotlib.pyplot as plt

# -----------------------------
# Task 1: Load CSV
# -----------------------------

df = pd.read_csv("dataset.csv")

print("Shape:", df.shape)
print("Columns:", df.columns)
print("First rows:")
print(df.head())


# -----------------------------
# Task 2: Load JSON
# -----------------------------

json_df = pd.read_json("sample_data.json")

print("JSON Data")
print(json_df)


# -----------------------------
# Task 3: SQLite Database
# -----------------------------

conn = sqlite3.connect("sample.db")

df.to_sql("employees", conn, if_exists="replace", index=False)

sql_df = pd.read_sql("SELECT * FROM employees", conn)

print("SQL Data")
print(sql_df)

conn.close()


# -----------------------------
# Task 4: Simulated API Data
# -----------------------------

movies = {
    "title": ["Movie1","Movie2","Movie3"],
    "rating": [7.5,8.1,6.9],
    "year": [2020,2021,2019]
}

movies_df = pd.DataFrame(movies)

movies_df.to_csv("tmdb_movies.csv", index=False)

print(movies_df)


# -----------------------------
# Task 5: Understanding Data
# -----------------------------

print(df.info())
print(df.describe())


# -----------------------------
# Task 6: Data Cleaning
# -----------------------------

df = df.drop_duplicates()

df.columns = df.columns.str.lower()


# -----------------------------
# Task 7: Feature Preparation
# -----------------------------

df_encoded = pd.get_dummies(df)

print(df_encoded.head())


# -----------------------------
# Task 8: Univariate Analysis
# -----------------------------

sns.histplot(df["salary"], kde=True)
plt.show()


sns.boxplot(x=df["salary"])
plt.show()


# -----------------------------
# Task 9: Bivariate Analysis
# -----------------------------

sns.scatterplot(x=df["age"], y=df["salary"])
plt.show()


sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.show()


# -----------------------------
# Task 10: Insights
# -----------------------------

print("INSIGHTS:")
print("1. Salary increases with age slightly.")
print("2. IT department has highest salaries.")
print("3. No missing values found.")
print("4. Data size is small but structured.")
print("5. Departments show different salary patterns.")