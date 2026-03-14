import pandas as pd
import sqlite3
import json
import requests
import seaborn as sns
import matplotlib.pyplot as plt
import kagglehub
import os

# ------------------------------------------------
# TASK 1 — LOAD DATA FROM KAGGLE CSV
# ------------------------------------------------

print("Downloading Kaggle dataset...")

path = kagglehub.dataset_download("spscientist/students-performance-in-exams")

print("Dataset downloaded at:", path)

csv_file = os.path.join(path, "StudentsPerformance.csv")

df = pd.read_csv(csv_file)

print("Shape:", df.shape)
print("Columns:", df.columns)
print(df.head())

# ------------------------------------------------
# TASK 2 — LOAD DATA FROM JSON
# ------------------------------------------------

print("\nTASK 2 — JSON DATA")

json_data = [
 {"id":1,"name":"Alice","department":"HR","salary":50000},
 {"id":2,"name":"Bob","department":"IT","salary":60000},
 {"id":3,"name":"Charlie","department":"Finance","salary":55000},
 {"id":4,"name":"David","department":"IT","salary":65000},
 {"id":5,"name":"Eva","department":"HR","salary":52000}
]

json_df = pd.DataFrame(json_data)

print(json_df)

# ------------------------------------------------
# TASK 3 — SQLITE DATABASE
# ------------------------------------------------

print("\nTASK 3 — SQLITE DATABASE")

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

# ------------------------------------------------
# TASK 4 — API DATA COLLECTION (TMDB CSV)
# ------------------------------------------------

print("\nTASK 4 — API DATA")

try:
    url = "https://api.sampleapis.com/movies/action"

    response = requests.get(url)

    data = response.json()

    if isinstance(data, list):

        movies = data[:10]

        movies_df = pd.DataFrame(movies)

        if "title" in movies_df.columns and "year" in movies_df.columns:
            movies_df = movies_df[["title","year"]]
        else:
            movies_df = movies_df.iloc[:, :2]

    else:
        raise Exception("Unexpected format")

except:

    print("API failed, creating sample movie dataset")

    movies_df = pd.DataFrame({
        "title":["Movie1","Movie2","Movie3","Movie4","Movie5"],
        "year":[2020,2021,2019,2022,2023]
    })

movies_df.to_csv("tmdb_movies.csv", index=False)

print(movies_df)

# ------------------------------------------------
# TASK 5 — UNDERSTANDING DATA
# ------------------------------------------------

print("\nTASK 5 — DATA INFO")

print(df.info())
print(df.describe())
print(df.isnull().sum())

# ------------------------------------------------
# TASK 6 — DATA CLEANING
# ------------------------------------------------

print("\nTASK 6 — CLEANING")

df = df.drop_duplicates()
df.columns = df.columns.str.lower()

print(df.head())

# ------------------------------------------------
# TASK 7 — FEATURE PREPARATION
# ------------------------------------------------

print("\nTASK 7 — FEATURES")

df_encoded = pd.get_dummies(df)

print(df_encoded.head())

# ------------------------------------------------
# TASK 8 — UNIVARIATE ANALYSIS
# ------------------------------------------------

print("\nTASK 8 — UNIVARIATE")

numeric_cols = df.select_dtypes(include=['int64','float64']).columns

for col in numeric_cols:

    sns.histplot(df[col], kde=True)
    plt.title(f"{col} distribution")
    plt.show()

# ------------------------------------------------
# TASK 9 — BIVARIATE ANALYSIS
# ------------------------------------------------

print("\nTASK 9 — BIVARIATE")

sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.title("Correlation Heatmap")
plt.show()

# ------------------------------------------------
# TASK 10 — INSIGHTS
# ------------------------------------------------

print("\nTASK 10 — INSIGHTS")

print("1. Dataset shows relationships between student scores.")
print("2. Some subjects have higher score distributions.")
print("3. Correlation shows how marks relate across subjects.")
print("4. Dataset appears clean with minimal missing values.")
print("5. Some score distributions show slight skewness.")