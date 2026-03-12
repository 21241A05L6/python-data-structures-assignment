import matplotlib.pyplot as plt

# -------------------------------
# Task 1: Line Plot (Sales Trend)
# -------------------------------

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [1200, 1500, 1800, 2000, 2200, 2500]

plt.figure()
plt.plot(months, sales)
plt.title("Monthly Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()


# -------------------------------
# Task 2: Scatter Plot
# -------------------------------

hours_studied = [1, 2, 3, 4, 5, 6, 7]
marks = [40, 50, 55, 65, 70, 80, 90]

plt.figure()
plt.scatter(hours_studied, marks)
plt.title("Study Hours vs Marks")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.show()


# -------------------------------
# Task 3: Bar Plot
# -------------------------------

products = ["Laptop", "Mobile", "Tablet", "Camera"]
sales_values = [50, 80, 30, 20]

# Vertical bar chart
plt.figure()
plt.bar(products, sales_values)
plt.title("Product Sales (Vertical Bar)")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()

# Horizontal bar chart
plt.figure()
plt.barh(products, sales_values)
plt.title("Product Sales (Horizontal Bar)")
plt.xlabel("Sales")
plt.ylabel("Products")
plt.show()


# -------------------------------
# Task 4: Multiple Bar Plot
# -------------------------------

years = ["2022", "2023", "2024"]

sales_A = [100, 120, 150]
sales_B = [90, 110, 140]

x = range(len(years))

plt.figure()
plt.bar(x, sales_A, width=0.4, label="Product A")
plt.bar([i + 0.4 for i in x], sales_B, width=0.4, label="Product B")

plt.title("Yearly Sales Comparison")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.xticks([i + 0.2 for i in x], years)
plt.legend()
plt.show()


# -------------------------------
# Task 5: Stacked Bar Chart
# -------------------------------

electronics = [50, 60, 70]
accessories = [30, 40, 50]

years = ["2022", "2023", "2024"]

plt.figure()
plt.bar(years, electronics, label="Electronics")
plt.bar(years, accessories, bottom=electronics, label="Accessories")

plt.title("Stacked Sales Chart")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.legend()
plt.show()


# -------------------------------
# Task 6: Histogram
# -------------------------------

marks_distribution = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

plt.figure()
plt.hist(marks_distribution, bins=5)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()


# -------------------------------
# Task 7: Pie Chart
# -------------------------------

categories = ["Electronics", "Clothing", "Food", "Books"]
market_share = [40, 25, 20, 15]

plt.figure()
plt.pie(market_share, labels=categories, autopct="%1.1f%%")

plt.title("Market Share by Category")
plt.show()