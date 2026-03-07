# import the libraries we need for the code
import pandas as pd
import matplotlib.pyplot as plt

# load the .csv file into a variable
dataset = pd.read_csv("video-games.csv")

# TODO - make a bar chart of the number of games per score
number_of_games_per_rating = dataset["Score"].value_counts().sort_index()
plt.bar(number_of_games_per_rating.index, number_of_games_per_rating)
plt.title('Number of games per Score')
plt.xlabel('Score')
plt.ylabel('Number of Games')
plt.show()

# TODO - make a line chart of the number of games per score
plt.plot(number_of_games_per_rating.index, number_of_games_per_rating)
plt.title('Number of games per Score')
plt.xlabel('Score')
plt.ylabel('Number of Games')
plt.show()

# TODO - make a pie chart of the distribution of consoles
number_of_games_per_console = dataset["Console"].value_counts()
plt.pie(number_of_games_per_console, labels=number_of_games_per_console.index)
plt.title("Number of Games per Console")
plt.show()


