# import the libraries we need for the code
import pandas as pd
import matplotlib.pyplot as plt

# load the .csv file into a variable
dataset = pd.read_csv("video-games.csv")

# TODO - make a bar chart of the number of games per score
# hint: 
number_of_games_per_rating = dataset[?].value_counts().sort_index()
plt.bar(number_of_games_per_rating.index, number_of_games_per_rating)
plt.title('Number of games per Score')
plt.xlabel('Score')
plt.ylabel('Number of Games')
plt.show()

# TODO - make a line chart of the number of games per score
# hint: you can re-use the `number_of_games_per_rating` variable above
plt.plot(?, ?)
# TODO - put a plot title here
# TODO - put an x-axis label here
# TODO - put an y-axis label here
# TODO - show the plot

# TODO - make a pie chart of the distribution of consoles
number_of_games_per_console = dataset[?].value_counts()
plt.pie(?, labels=?.index)
# TODO - put a plot title here
# TODO - show the plot
