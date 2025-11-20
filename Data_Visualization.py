# Matplotlib Charts Examples
import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.arange(1, 6)
y = np.array([10, 15, 7, 12, 5])
y2 = np.array([5, 8, 12, 6, 10])
categories = ['A', 'B', 'C', 'D', 'E']
data = np.random.randn(100)  # for histogram & boxplot
matrix = np.random.rand(5, 5)  # for heatmap

# 1️⃣ Line Plot
plt.figure(figsize=(6,4))
plt.plot(x, y, marker='o', color='blue')
plt.title("Line Plot")
plt.show()

# 2️⃣ Bar Chart
plt.figure(figsize=(6,4))
plt.bar(categories, y)
plt.title("Bar Chart")
plt.show()

# 3️⃣ Horizontal Bar Chart
plt.figure(figsize=(6,4))
plt.barh(categories, y)
plt.title("Horizontal Bar Chart")
plt.show()

# 4️⃣ Scatter Plot
plt.figure(figsize=(6,4))
plt.scatter(x, y, color='red', s=100)
plt.title("Scatter Plot")
plt.show()

# 5️⃣ Histogram
plt.figure(figsize=(6,4))
plt.hist(data, bins=10, color='green', edgecolor='black')
plt.title("Histogram")
plt.show()

# 6️⃣ Pie Chart
plt.figure(figsize=(6,6))
plt.pie(y, labels=categories, autopct='%1.1f%%', startangle=90)
plt.title("Pie Chart")
plt.show()

# 7️⃣ Box Plot
plt.figure(figsize=(6,4))
plt.boxplot(data)
plt.title("Box Plot")
plt.show()

# 8️⃣ Violin Plot
plt.figure(figsize=(6,4))
plt.violinplot(data)
plt.title("Violin Plot")
plt.show()

# 9️⃣ Area Plot (Filled Line Plot)
plt.figure(figsize=(6,4))
plt.fill_between(x, y, color='skyblue', alpha=0.5)
plt.plot(x, y, color='blue', marker='o')
plt.title("Area Plot")
plt.show()

# 1️⃣0️⃣ Stacked Area Plot
plt.figure(figsize=(6,4))
plt.stackplot(x, y, y2, colors=['blue', 'orange'], labels=['y', 'y2'])
plt.legend()
plt.title("Stacked Area Plot")
plt.show()

# 1️⃣1️⃣ Heatmap (using imshow)
plt.figure(figsize=(6,4))
plt.imshow(matrix, cmap='viridis')
plt.colorbar()
plt.title("Heatmap")
plt.show()

# 1️⃣2️⃣ 3D Plot
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure(figsize=(6,4))
ax = fig.add_subplot(111, projection='3d')
ax.plot([1,2,3,4,5], [5,6,2,3,7], [1,4,9,16,25], marker='o', color='purple')
ax.set_title("3D Line Plot")
plt.show()




import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# ============================
# 1️⃣ Line Plot
# ============================
plt.figure(figsize=(6,4))
sns.lineplot(x=[1, 2, 3, 4], y=[10, 20, 15, 25])
plt.title("Line Plot")
plt.show()

# ============================
# 2️⃣ Bar Plot
# ============================
plt.figure(figsize=(6,4))
sns.barplot(x=["A", "B", "C"], y=[5, 7, 3])
plt.title("Bar Plot")
plt.show()

# ============================
# 3️⃣ Count Plot
# ============================
plt.figure(figsize=(6,4))
sns.countplot(x=["A", "B", "A", "C", "B", "A"])
plt.title("Count Plot")
plt.show()

# ============================
# 4️⃣ Scatter Plot
# ============================
plt.figure(figsize=(6,4))
sns.scatterplot(x=[1, 2, 3, 4], y=[5, 7, 6, 9])
plt.title("Scatter Plot")
plt.show()

# ============================
# 5️⃣ Histogram
# ============================
plt.figure(figsize=(6,4))
sns.histplot([1, 2, 2, 3, 3, 3, 4, 5], kde=False)
plt.title("Histogram")
plt.show()

# ============================
# 6️⃣ KDE Plot
# ============================
plt.figure(figsize=(6,4))
sns.kdeplot([1, 2, 2, 3, 3, 3, 4, 5])
plt.title("KDE (Density) Plot")
plt.show()

# ============================
# 7️⃣ Box Plot
# ============================
plt.figure(figsize=(6,4))
sns.boxplot(y=[10, 12, 14, 10, 18, 20, 25])
plt.title("Box Plot")
plt.show()

# ============================
# 8️⃣ Violin Plot
# ============================
plt.figure(figsize=(6,4))
sns.violinplot(y=[10, 12, 14, 10, 18, 20, 25])
plt.title("Violin Plot")
plt.show()

# ============================
# 9️⃣ Heatmap
# ============================
plt.figure(figsize=(6,4))
data = np.random.rand(4, 4)
sns.heatmap(data, annot=True)
plt.title("Heatmap")
plt.show()

# ============================
# 🔟 Pairplot
# ============================
df = sns.load_dataset("iris")
sns.pairplot(df)
plt.suptitle("Pairplot", y=1.02)
plt.show()
