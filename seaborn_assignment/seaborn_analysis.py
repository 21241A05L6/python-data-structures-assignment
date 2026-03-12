import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("StudentsPerformance.csv")

# ------------------------------
# Task 1: Relational Plot
# ------------------------------

sns.relplot(
    data=df,
    x="math score",
    y="reading score",
    hue="gender"
)

plt.title("Math vs Reading Scores")
plt.show()


# Scatter version
sns.relplot(
    data=df,
    x="math score",
    y="reading score",
    hue="gender",
    kind="scatter"
)

plt.title("Scatter Plot: Math vs Reading")
plt.show()


# ------------------------------
# Task 2: Line Plot + Facet
# ------------------------------

sns.lineplot(
    data=df,
    x="math score",
    y="writing score"
)

plt.title("Math vs Writing Scores")
plt.show()


sns.relplot(
    data=df,
    x="math score",
    y="writing score",
    col="gender"
)

plt.show()


# ------------------------------
# Task 3: Distribution Plots
# ------------------------------

sns.histplot(df["math score"])

plt.title("Histogram of Math Scores")
plt.show()


sns.kdeplot(df["math score"])

plt.title("KDE Plot")
plt.show()


sns.rugplot(df["math score"])

plt.title("Rug Plot")
plt.show()


sns.histplot(df["math score"], kde=True)

plt.title("Histogram + KDE")
plt.show()


# ------------------------------
# Task 4: Bivariate Distribution
# ------------------------------

sns.histplot(
    data=df,
    x="math score",
    y="reading score"
)

plt.title("Bivariate Histogram")
plt.show()


sns.kdeplot(
    data=df,
    x="math score",
    y="reading score"
)

plt.title("Bivariate KDE")
plt.show()


# ------------------------------
# Task 5: Matrix Plots
# ------------------------------

sns.pairplot(df[
    ["math score", "reading score", "writing score"]
])

plt.show()


corr = df[
    ["math score", "reading score", "writing score"]
].corr()

sns.heatmap(corr, annot=True)

plt.title("Correlation Matrix")
plt.show()


# ------------------------------
# Task 6: Categorical Plots
# ------------------------------

sns.barplot(
    data=df,
    x="gender",
    y="math score"
)

plt.title("Bar Plot")
plt.show()


sns.boxplot(
    data=df,
    x="gender",
    y="math score"
)

plt.title("Box Plot")
plt.show()


sns.violinplot(
    data=df,
    x="gender",
    y="math score"
)

plt.title("Violin Plot")
plt.show()


sns.countplot(
    data=df,
    x="gender"
)

plt.title("Count Plot")
plt.show()


# ------------------------------
# Task 7: Regression Plots
# ------------------------------

sns.regplot(
    data=df,
    x="math score",
    y="reading score"
)

plt.title("Regression Plot")
plt.show()


sns.lmplot(
    data=df,
    x="math score",
    y="reading score",
    hue="gender"
)

plt.show()


# ------------------------------
# Task 8: Multi-Plots
# ------------------------------

g = sns.FacetGrid(
    df,
    col="gender"
)

g.map(sns.scatterplot, "math score", "reading score")

plt.show()


sns.relplot(
    data=df,
    x="math score",
    y="reading score",
    hue="gender"
)

plt.show()


sns.catplot(
    data=df,
    x="gender",
    y="math score",
    kind="box"
)

plt.show()


sns.displot(df["math score"])

plt.show()