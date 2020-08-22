#importing pandas for reading datasets
import pandas as pd
#importing matplotlib for data visualisation
import matplotlib.pyplot as plt
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
# creating dataframe with 'rating' count values
ratings_count = pd.DataFrame(data_merged.groupby('title')['rating'].mean())
ratings_count['num of ratings'] = pd.DataFrame(data_merged.groupby('title')['rating'].count())
ratings_count.head()