import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#df = pd.read_csv("steam_app_data.csv")
df = pd.read_csv("steamspy_data.csv")

#print(df.head())
print(df.columns)


data = df[[ 'developer',  'positive', 'negative']];
# Aggregate total reviews (positive + negative) per developer
df["total_reviews"] = df["positive"] + df["negative"]

df_grouped = df.groupby("developer", as_index=False)[["positive", "negative"]].sum()
df_grouped["total_reviews"] = df_grouped["positive"] + df_grouped["negative"]

# Select the top 10 unique developers by total reviews
top_10_unique_devs = df_grouped.nlargest(10, "total_reviews")

# Bar width
bar_width = 0.4
x = np.arange(len(top_10_unique_devs))  # X positions for bars

# Create the plot
fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(x - bar_width/2, top_10_unique_devs["positive"], bar_width, label="Positive Reviews", color="green")
ax.bar(x + bar_width/2, top_10_unique_devs["negative"], bar_width, label="Negative Reviews", color="red")

# Labels & Titles
ax.set_xlabel("Developer")
ax.set_ylabel("Number of Reviews")
ax.set_title("Top 10 Unique Developers by Total Reviews")
ax.set_xticks(x)
ax.set_xticklabels(top_10_unique_devs["developer"], rotation=30, ha="right")
ax.legend()

# Show the plot
plt.tight_layout()
plt.show()
