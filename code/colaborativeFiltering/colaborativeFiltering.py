#importing pandas for reading datasets
import pandas as pd
#importing matplotlib for data visualisation
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')
#importing numpy to do array calculations and handling
import numpy as np


#creating dataframe for rating.csv file that contains rows user id, movieid, rating, timestmp
rating_df=pd.read_csv("../../datasets/ratings.csv")
#to get all the columns of ratings.csv
rating_df.columns
#to print head and tail of ratings.csv
print(rating_df.head())
print(rating_df.tail())
#creating datframe for movies.csv that contains movie name for corresponding movie Id
movies_df=pd.read_csv("../../datasets/movies.csv")
#to print head and tail to movies.csv
print(movies_df.head())
print(movies_df.tail())
# print(movies_df.iloc[2])

#Checking for nan values in both dataframe
print(rating_df.isnull().count())
print(movies_df.isnull().count())
#merging the ratings and movie titles tables over movie id
data_merged = pd.merge(rating_df, movies_df, on='movieId')
#printing the head of data merged, it provies of different
# users who rated different movies
data_merged.head()
# Calculate mean rating of all movies and printing it in decending orrder
#grouping them by tittle & ratings mean value
data_merged.groupby('title')['rating'].mean().sort_values(ascending=False).head()
#creating a rating_count dataframe with all the mean ratings of movies
ratings_count = pd.DataFrame(data_merged.groupby('title')['rating'].mean())
# creating anew coulumn in 'rating_count' for rating count values
# that counts all the ratings for specific movie
ratings_count['num of ratings'] = pd.DataFrame(data_merged.groupby('title')['rating'].count())
#printing raings_count head gives a clean view of mean rating of
# each movie and total ratings given to it
ratings_count.head()
# plot graph of 'num of ratings column
plt.figure(figsize =(10, 4))
ratings_count['num of ratings'].hist(bins = 70)
# plot graph of 'ratings' column
plt.figure(figsize =(10, 4))
ratings_count['rating'].hist(bins = 70)
# Sorting values according to
# the 'num of rating column'
moviemat = data_merged.pivot_table(index ='userId',columns ='title', values ='rating')
moviemat.head()
ratings_count.sort_values('num of ratings', ascending = False).head(10)
# analysing correlation with similar movies
forrestGump_user_ratings = moviemat['Forrest Gump (1994)']
forrestGump_user_ratings.head()
# analysing correlation with similar movies
