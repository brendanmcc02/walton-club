import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("movies.csv")

# create a pie chart of the proportion of Ratings in the dataset
number_of_films_per_rating = dataset["Rating"].value_counts()
plt.pie(number_of_films_per_rating, labels=number_of_films_per_rating.index)
plt.show()
