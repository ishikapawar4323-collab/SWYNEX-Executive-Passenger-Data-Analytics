import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Titanic_Cleaned.csv")

print(df.describe(include="all"))

# Survival by gender
df.groupby("Sex")["Survived"].mean().mul(100).plot(kind="bar")
plt.ylabel("Survival %")
plt.title("Gender vs Survival")
plt.show()
