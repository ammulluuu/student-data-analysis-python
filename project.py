import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv(r"C:\Users\SSSM\Desktop\ammulu\AMMULLUU\student.csv")

#  Extract subject columns
maths = df["Maths"]
physics = df["Physics"]
chemistry = df["Chemistry"]

# Calculate average
df["Average"] = df[["Maths", "Physics", "Chemistry"]].mean(axis=1)

#  Create one window with multiple plots
plt.figure(figsize=(10, 8))
# 1. Bar Chart (Average Marks)

plt.subplot(2, 2, 1)
plt.bar(range(len(df)), df["Average"])
plt.title("Average Marks")
# 📈 2. Scatter Plot (Maths vs Physics)
plt.subplot(2, 2, 2)
plt.scatter(maths, physics)
plt.xlabel("Maths")
plt.ylabel("Physics")
plt.title("Maths vs Physics")
# 📈 3. Scatter Plot (Physics vs Chemistry)
plt.subplot(2, 2, 3)
plt.scatter(physics, chemistry)
plt.xlabel("Physics")
plt.ylabel("Chemistry")
plt.title("Physics vs Chemistry")

#  4. Heatmap (Correlation)

plt.subplot(2, 2, 4)
corr = df[["Maths", "Physics", "Chemistry"]].corr()
plt.imshow(corr)
plt.colorbar()
plt.xticks([0,1,2], ["Maths","Physics","Chemistry"])
plt.yticks([0,1,2], ["Maths","Physics","Chemistry"])
plt.title("Correlation Heatmap")

# adjust layout
plt.tight_layout()

# show all plots
plt.show()

#  Print results

print("First 5 Rows:\n", df.head())
print("\nOverall Average:", df["Average"].mean())

#  Topper
topper = df.loc[df["Average"].idxmax()]
print("\nTopper Details:\n", topper)