# I (Brendan) didn't actually teach this class, 
# Lalith taught it, so I'm not 100% sure how good the material was for teaching
# honestly, i'm not sure if a "code-a-long" style is great,
# i think what could work better is getting printed worksheets (so they can't copy/paste)
# with the code on them, and tell them to re-type the code on the sheet.
# i can provide written explanations on them

# * do an interactive walkthrough of the code below
# * type the code along with them and go step-by-step

# import the pandas library
import pandas as pd

# load the csv file into a variable
dataset = pd.read_csv("simple-movie-ratings.csv")

# get a quick look at some rows
print(dataset.head())

# get all the values for a column
# tell them about the square bracket notation - that's how you access **columns**
movie_years = dataset["Year"].tolist()
print(str(movie_years))

# # how would you get all the movie titles?
# TODO leave this as an exercise for them, give them ~1 min
movie_titles = ?
print(str(movie_titles))

# # how would you get all the movie years?
# TODO leave this as an exercise for them, give them ~1 min
movie_years = ?
print(str(movie_years))

# filter out films
# tell them about the square bracket notation again
# this is essentially a filter
# break down the `dataset[dataset["Rating"] >= 4.0]` because the first time they see this will be confusing
movies_i_like = dataset[dataset["Rating"] >= 4.0]
print(str(movies_i_like))

# # how would you filter out films that have 4.5 rating or higher?
# hint: use dataset[dataset["Rating"] >= 4.5]
# TODO leave this as an exercise for them, give them ~1 min
movies_i_really_like = ?
print(str(movies_i_really_like))

# # how would you filter out films that have 3.0 rating or lower?
# TODO leave this as an exercise for them, give them ~1 min
movies_i_dont_like = ?
print(str(movies_i_dont_like))

# # how would you filter out films that have lower than a 2.5 rating?
# TODO leave this as an exercise for them, give them ~1 min
movies_i_hate = ?
print(str(movies_i_hate))

# # how would you filter out films that have a rating of 5.0 exactly?
# # hint use `==` instead of `<` or `>` like done previously
# TODO leave this as an exercise for them, give them ~1 min
movies_i_love = ?
print(str(movies_i_love))

# get the mean value of a column
mean_years = dataset["Year"].mean()
print(str(mean_years))

# # how would you get the mean value of the ratings column?
mean_ratings = ?
print(str(mean_ratings))