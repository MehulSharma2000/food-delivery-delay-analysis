import pandas as pd

# Read CSV file
df = pd.read_csv("Food_Delivery_5_Sheets_Clean.csv")

# Show first 10 rows
print(df.head(10))

# Show summary
print(df.info())

# Check unique delay reasons
print(df['Delay_Reason'].value_counts())
#start time and end time
df['Start_Time'] = pd.to_datetime(df['Start_Time'], format="%H:%M")
df['End_Time'] = pd.to_datetime(df['End_Time'], format="%H:%M")

#duration time
df['Duration'] = (df['End_Time'] - df['Start_Time']).dt.total_seconds() / 60
print(df['Duration'].head())

#dealy reason
print(df.groupby('Delay_Reason')['Duration'].mean())

#top 10 slowest delivery
print(df.nlargest(10, 'Duration')[['Order_ID', 'Rider_ID', 'Duration', 'Delay_Reason']])

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Food_Delivery_5_Sheets_Clean.csv")

df["Start_Time"] = pd.to_datetime(df["Start_Time"])
df["End_Time"] = pd.to_datetime(df["End_Time"])
df["Duration"] = (df["End_Time"] - df["Start_Time"]).dt.total_seconds() / 60

# Chart 1
df["Delay_Reason"].value_counts().plot(kind="bar")
plt.title("Delay Reason Count")
plt.show()

# Chart 2
plt.hist(df["Duration"], bins=10)
plt.title("Delivery Duration Distribution")
plt.show()

# Chart 3
df.groupby("Rider_ID")["Duration"].mean().plot(kind="bar", figsize=(10,4))
plt.title("Average Delivery Time per Rider")
plt.show()

# Chart 4
df.groupby("Delay_Reason")["Duration"].mean().plot(kind="bar")
plt.title("Average Delivery Duration by Delay Reason")
plt.show()