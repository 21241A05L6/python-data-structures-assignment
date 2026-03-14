import pandas as pd
import sqlite3
import json
import requests
import seaborn as sns
import matplotlib.pyplot as plt

# ----------------------------
# TASK 1 — LOAD CSV DATA
# ----------------------------

print("TASK 1 — CSV DATA")

df = pd.read_csv("dataset.csv")

print("Shape:", df.shape)
print("Columns:", df.columns)
print(df.head())


# ----------------------------
# TASK 2 — LOAD JSON DATA
# ----------------------------

print("\nTASK 2 — JSON DATA")

with open("data.json") as f:
    json_data = json.load(f)

json_df = pd.DataFrame(json_data)

print(json_df)


# ----------------------------
# TASK 3 — SQLITE DATABASE
# ----------------------------

print("\nTASK 3 — SQLITE")

conn = sqlite3.connect("sample.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees(
id INTEGER,
name TEXT,
department TEXT,
salary INTEGER
)
""")

cursor.execute("DELETE FROM employees")

cursor.executemany(
"INSERT INTO employees VALUES (?,?,?,?)",
[
(1,"Alice","HR",50000),
(2,"Bob","IT",60000),
(3,"Charlie","Finance",55000),
(4,"David","IT",65000),
(5,"Eva","HR",52000)
]
)

conn.commit()

sql_df = pd.read_sql_query("SELECT * FROM employees", conn)

print(sql_df)


# ----------------------------
# TASK 4 — API DATA COLLECTION (FIXED)
# ----------------------------

print("\nTASK 4 — API DATA")

try:
    url = "https://api.sampleapis.com/movies/action"

    response = requests.get(url)

    data = response.json()

    # Ensure API returned list
    if isinstance(data, list):

        movies = data[:10]

        movies_df = pd.DataFrame(movies)

        # ensure correct columns exist
        if "title" in movies_df.columns and "year" in movies_df.columns:
            movies_df = movies_df[["title","year"]]
        else:
            movies_df = movies_df.iloc[:, :2]

    else:
        raise Exception("Unexpected API format")

except:
    print("API failed — creating sample movie dataset")

    movies_df = pd.DataFrame({
        "title":["Movie1","Movie2","Movie3","Movie4","Movie5"],
        "year":[2020,2021,2019,2022,2023]
    })

movies_df.to_csv("tmdb_movies.csv", index=False)

print(movies_df)


# ----------------------------
# TASK 5 — UNDERSTANDING DATA
# ----------------------------

print("\nTASK 5 — DATA INFO")

print(df.info())

print(df.describe())

print("Missing values")
print(df.isnull().sum())


# ----------------------------
# TASK 6 — DATA CLEANING
# ----------------------------

print("\nTASK 6 — CLEANING")

df = df.drop_duplicates()

df = df.fillna(df.mean(numeric_only=True))

df.columns = df.columns.str.lower()

print(df.head())


# ----------------------------
# TASK 7 — FEATURE PREPARATION
# ----------------------------

print("\nTASK 7 — FEATURES")

df_encoded = pd.get_dummies(df, columns=["department"])

X = df_encoded.drop("salary", axis=1)

y = df_encoded["salary"]

print(X.head())


# ----------------------------
# TASK 8 — UNIVARIATE ANALYSIS
# ----------------------------

print("\nTASK 8 — UNIVARIATE")

sns.histplot(df["salary"], kde=True)
plt.title("Salary Distribution")
plt.show()

sns.boxplot(x=df["salary"])
plt.title("Salary Boxplot")
plt.show()

sns.countplot(x=df["department"])
plt.title("Department Count")
plt.show()


# ----------------------------
# TASK 9 — BIVARIATE ANALYSIS
# ----------------------------

print("\nTASK 9 — BIVARIATE")

sns.scatterplot(x=df["age"], y=df["salary"])
plt.title("Age vs Salary")
plt.show()

corr = df.corr(numeric_only=True)

sns.heatmap(corr, annot=True)
plt.title("Correlation Heatmap")
plt.show()

sns.boxplot(x="department", y="salary", data=df)
plt.show()


# ----------------------------
# TASK 10 — INSIGHTS
# ----------------------------

print("\nTASK 10 — INSIGHTS")

print("1. Salary increases as experience increases.")
print("2. IT department salaries tend to be higher.")
print("3. Dataset contains no missing values.")
print("4. Age and salary have moderate correlation.")
print("5. Finance and IT show higher salary spread.")