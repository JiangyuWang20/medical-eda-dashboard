# eda.py
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ---------------------------
# Global settings
# ---------------------------
sns.set_style("whitegrid")   # Set grid style
sns.set_palette("Set2")      # Set default color palette

# Ensure figures folder exists
os.makedirs("figures", exist_ok=True)

# ---------------------------
# Load dataset
# ---------------------------
df = pd.read_csv(r"D:\project\diabetes_clean.csv")  # Load Diabetes dataset

# ---------------------------
# 1. Correlation Heatmap
# ---------------------------
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap", fontsize=16)
plt.tight_layout()
plt.savefig("figures/heatmap.png", dpi=300, bbox_inches="tight")
plt.show()

# ---------------------------
# 2. Age Distribution by Diabetes Outcome
# ---------------------------
plt.figure(figsize=(8, 6))
sns.histplot(data=df, x="Age", hue="Outcome", kde=True, bins=30)
plt.title("Age Distribution by Diabetes Outcome", fontsize=16)
plt.xlabel("Age", fontsize=14)
plt.ylabel("Count", fontsize=14)
plt.tight_layout()
plt.savefig("figures/age_distribution.png", dpi=300, bbox_inches="tight")
plt.show()

# ---------------------------
# 3. BMI vs Diabetes Outcome (Violin Plot)
# ---------------------------
plt.figure(figsize=(8, 6))
sns.violinplot(data=df, x="Outcome", y="BMI", hue="Outcome", palette="Set2", legend=False)
plt.title("BMI vs Diabetes Outcome", fontsize=16)
plt.xlabel("Outcome", fontsize=14)
plt.ylabel("BMI", fontsize=14)
sns.despine()
plt.tight_layout()
plt.savefig("figures/bmi_violin.png", dpi=300, bbox_inches="tight")
plt.show()

# ---------------------------
# 4. Glucose vs Diabetes Outcome (Boxplot)
# ---------------------------
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x="Outcome", y="Glucose", hue="Outcome", palette="Set3", legend=False)
plt.title("Glucose Level vs Diabetes Outcome", fontsize=16)
plt.xlabel("Outcome", fontsize=14)
plt.ylabel("Glucose", fontsize=14)
sns.despine()
plt.tight_layout()
plt.savefig("figures/glucose_boxplot.png", dpi=300, bbox_inches="tight")
plt.show()

# ---------------------------
# 5. Pairplot of Key Features
# ---------------------------
sns.pairplot(df, hue="Outcome", vars=["Age", "Glucose", "BMI", "BloodPressure"], palette="husl")
plt.suptitle("Pairplot of Key Features by Diabetes Outcome", y=1.02, fontsize=16)
plt.savefig("figures/pairplot.png", dpi=300, bbox_inches="tight")
plt.show()
