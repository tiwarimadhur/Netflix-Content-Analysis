#  IMPORTS
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#  HELPER FUNCTION

def value_counts_1(series, n=10):
    result = series.value_counts().head(n)
    result.index = range(1, len(result) + 1)
    return result

#  LOAD DATA
df = pd.read_csv(r"/workspaces/Netflix-Content-Analysis/netflix_titles.zip", compression="zip", encoding="latin1")

#  DATA INSPECTION
df = df.reset_index(drop=True)
df.index = df.index + 1

print("\n1. 5 MOVIES FROM STARTING \n")
print(df.head())
print("\n 5 MOVIES FROM LAST\n")
print(df.tail())


print("\n2. INFORMATION OF DATAFRAME\n")
print(df.info())

print("\n3. FINDING MISSING VALUES\n")
print(df.isnull().sum())

print("\n4. FINDING UNIQUE VALUES\n")
print(df.nunique())

print("\n5. TOP 10 COUNTRIES WITH MOST CONTENT\n")

top_countries = value_counts_1(df["country"])
print(top_countries)


print("\n6. MOST COMMON GENRE\n")
common_genre = value_counts_1(df["listed_in"])
print(common_genre)


print("\n7. MOST FREQUENT DIRECTORS\n")
print(value_counts_1(df["director"]))

print("\n8. ACTORS WITH MOST APPEARENCES\n")
top_actors = value_counts_1(df["cast"].str.split(",", expand= True).stack().str.strip())
print(top_actors)

print("\n9. CONTENT ADDED PER YEAR\n")
print(df["release_year"].value_counts().sort_index())

print("\n10. FILTERING INDIAN MOVIES \n")
print(df[(df["type"] =="Movie") & (df["country"].str.contains("India",na=False))])

print("\n11. FILTERING TV Show \n")
print(df[(df["type"] =="TV Show") & (df["country"].str.contains("India",na=False))])

print("\n12. HIGHEST RATED GENRES FOR MOVIES  \n")
movies = df[df["type"]=="Movie"]
Shows = df[df["type"]=="TV Show"]
print(value_counts_1(movies["listed_in"]))
print("\n13. HIGHEST RATED GENRES FOR TV SHOWS \n")
print(value_counts_1(Shows["listed_in"]))

print("\n14. ALL SHOWS DIRECTED BY 'Steven Spielberg' \n")
direction = df[df["director"]=="Steven Spielberg"]
if direction.empty:
    print("\n NO shows directed by Steven Spielberg in the Netflix\n")
else:    
    print(value_counts_1(direction["director"]))


print("\n15. CONTENT DURATION: \n")

print("\nA.        MOVIES \n")

Duration_movies= df[df["type"]=="Movie"]
print(value_counts_1(Duration_movies["duration"]))

print("\nB.        TV SHOWS \n")

Duration_shows= df[df["type"]=="TV Show"]
print(value_counts_1(Duration_shows["duration"]))
print("\n")
print("\n==============================")
print("***   DATA VISUALIZATION   *** ")
print("==============================\n")

# MOVIES VS TV SHOWS (PIE CHART)
type_count = df["type"].value_counts()
plt.figure(figsize=(6,6))
plt.pie(type_count,labels=type_count.index,autopct="%1.1f%%")#
plt.title("Movies VS TV Shows on Netflix")
plt.tight_layout()
plt.savefig("Movies_VS_TV Shows.jpg", dpi=300,bbox_inches="tight")
plt.show()

# RELEASE TREND OVER YEARS 

content_year = df["release_year"].value_counts().sort_index()

plt.figure(figsize=(10,5))
plt.plot(content_year.index,content_year.values)
plt.title("Netflix Content Release Trend Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.grid(True)
plt.tight_layout()
plt.savefig("Release_trend.jpg")
plt.show()

# MOST COMMON GENRE
plt.figure(figsize=(10,5))
common_genre.plot(kind="barh", color= "blue")
plt.title("Most Common Genre")
plt.xlabel("Count")
plt.ylabel("Genre")
plt.tight_layout()
plt.savefig("common_genre.jpg")
plt.show()

# TOP 10 COUNTRIES IN CONTENT PRODUCING
plt.figure(figsize=(10,5))
top_countries.plot(kind="bar", color="pink")
plt.title("Top 10 Countries with most Content")
plt.xlabel("country")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_10_countries.jpg")
plt.show()

# MOVIES DURATION DISTRIBUTION
movies_duration = df[df["type"]=="Movie"]["duration"].str.replace("min","",regex =False).dropna().astype(int)
plt.figure(figsize=(8,5))
plt.hist(movies_duration,bins=20, color ="orange",edgecolor="black")
plt.title("Distribution of Movie Durations")
plt.xlabel("Duration (Minutes)")
plt.ylabel("Number of Movies")
plt.tight_layout()
plt.savefig("movie_durations.jpg")
plt.show()

# RELEASE YEAR VS MOVIE DURATION TREND (SCATTER PLOT)
scatter_df = df[df["type"]=="Movie"][["release_year","duration"]].dropna()
scatter_df["duration"]= scatter_df["duration"].str.replace("min","",regex=False).astype(int)

plt.figure(figsize=(10,6))
plt.scatter(scatter_df["release_year"],scatter_df["duration"], alpha=0.4, color="red")
plt.title("Release year VS Movie Duration ")
plt.xlabel("Release year")
plt.ylabel("Duration (Minutes)")
plt.grid(True)
plt.tight_layout()
plt.savefig("Relation_between_release_year_vs_duration.jpg")
plt.show()
