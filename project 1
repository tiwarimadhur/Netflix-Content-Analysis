import pandas as pd
import numpy as np

# READ DATA
df = pd.read_csv(r"C:\New folder\archive (1).zip", compression="zip", encoding="latin1")
print("\n FULL DATAFRAME\n",df)

print("\n1. 5 MOVIES FROM STARTING\n")
print(df.head())
print("\n5 MOVIES FROM LAST\n")
print(df.tail())

print("\n2. INFORMATION OF DATAFRAME\n")
print(df.info())

print("\n3. FINDING MISSING VALUES\n")
print(df.isnull().sum())
print(df.isnull())

print("\n4. FINDING UNIQUE VALUES\n")
print(df.nunique())

print("\n5. TOP 10 COUNTRIES WITH MOST CONTENT\n")
print(df["country"].value_counts().head(10))

print("\n6. MOST COMMON GENRE\n")
print(df["listed_in"].value_counts().head(10))

print("\n7. MOST FREQUENT DIRECTORS\n")
print(df["director"].value_counts().head(10))

print("\n8. ACTORS WITH MOST APPEARENCES\n")
print(df["cast"].str.split(",", expand= True).stack().value_counts().head(10))

print("\n9. CONTENT ADDED PER YEAR\n")
print(df["release_year"].value_counts().sort_index())

print("\n10. FILTERING INDIAN MOVIES \n")
print(df[(df["type"] =="Movie") & (df["country"].str.contains("India",na=False))])

print("\n11. FILTERING TV Show \n")
print(df[(df["type"] =="TV Show") & (df["country"].str.contains("India",na=False))])

print("\n12. HIGHEST RATED GENRES FOR MOVIES  \n")
movies = df[df["type"]=="Movie"]
Shows = df[df["type"]=="TV Show"]
print(movies["listed_in"].value_counts().head(10))
print("\n13. HIGHEST RATED GENRES FOR TV SHOWS \n")
print(Shows["listed_in"].value_counts().head(10))

print("\n14. ALL SHOWS DIRECTED BY 'Steven Spielberg' \n")
direction = df[df["director"]=="Steven Spielberg"]
if direction.empty:
    print("\n NO shows directed by Steven Spielberg in the Netflix\n")
else:    
    print(direction["director"].value_counts().head(10))


print("\n15. CONTENT DURATION: \n")

print("\nA.        MOVIES \n")

Duration_movies= df[df["type"]=="Movie"]
print(Duration_movies["duration"].value_counts().head(10))

print("\nB.        TV SHOWS \n")

Duration_shows= df[df["type"]=="TV Show"]
print(Duration_shows["duration"].value_counts().head(10))




