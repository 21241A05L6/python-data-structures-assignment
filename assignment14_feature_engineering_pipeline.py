import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# ------------------------------------------------
# CREATE DATASET (no external file needed)
# ------------------------------------------------

data = {
    "age":[22,25,47,35,52,46,23,40],
    "salary":[30000,35000,80000,65000,90000,70000,32000,60000],
    "department":["HR","IT","Finance","IT","Finance","HR","IT","Finance"],
    "experience":[1,2,15,7,20,12,1,10],
    "target":[0,0,1,1,1,1,0,1]
}

df = pd.DataFrame(data)

print("Original Dataset")
print(df)

# ------------------------------------------------
# PART 1 – FEATURE ENGINEERING
# ------------------------------------------------

print("\n--- Feature Engineering ---")

# new feature
df["salary_per_experience"] = df["salary"] / (df["experience"] + 1)

# age group
df["age_group"] = pd.cut(
    df["age"],
    bins=[20,30,40,60],
    labels=["Young","Adult","Senior"]
)

print(df)

print("\nDate/Text column not available so step skipped.")

# ------------------------------------------------
# PART 2 – ONE HOT ENCODING
# ------------------------------------------------

print("\n--- One Hot Encoding ---")

df_encoded = pd.get_dummies(df, columns=["department","age_group"])

print(df_encoded)

# ------------------------------------------------
# COLUMN TRANSFORMER
# ------------------------------------------------

print("\n--- Column Transformer ---")

numeric_features = ["age","salary","experience","salary_per_experience"]
categorical_features = ["department","age_group"]

preprocessor = ColumnTransformer(
    transformers=[
        ("num","passthrough",numeric_features),
        ("cat",OneHotEncoder(),categorical_features)
    ]
)

X = df[numeric_features + categorical_features]
y = df["target"]

X_transformed = preprocessor.fit_transform(X)

print("Transformed shape:", X_transformed.shape)

# ------------------------------------------------
# PART 3 – FEATURE SCALING
# ------------------------------------------------

print("\n--- StandardScaler ---")

scaler = StandardScaler()

scaled_data = scaler.fit_transform(df[numeric_features])

print(scaled_data)

print("\n--- MinMaxScaler ---")

minmax = MinMaxScaler()

normalized_data = minmax.fit_transform(df[numeric_features])

print(normalized_data)

# ------------------------------------------------
# PART 4 – BUILDING ML PIPELINE
# ------------------------------------------------

print("\n--- ML Pipeline ---")

numeric_pipeline = Pipeline([
    ("scaler",StandardScaler())
])

categorical_pipeline = Pipeline([
    ("encoder",OneHotEncoder())
])

full_preprocess = ColumnTransformer([
    ("num",numeric_pipeline,numeric_features),
    ("cat",categorical_pipeline,categorical_features)
])

model_pipeline = Pipeline([
    ("preprocess",full_preprocess),
    ("model",LogisticRegression())
])

X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.2,random_state=42
)

model_pipeline.fit(X_train,y_train)

predictions = model_pipeline.predict(X_test)

print("Predictions:",predictions)

# ------------------------------------------------
# TASK 9 – CONCEPTUAL ANSWERS
# ------------------------------------------------

print("\n--- Pipeline Benefits ---")

print("1. Pipelines automate preprocessing and modeling steps.")
print("2. They prevent data leakage and keep workflow consistent.")
print("3. Manual preprocessing requires separate steps while pipelines combine everything.")