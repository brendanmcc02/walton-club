# THOUGHTS AFTER TEACHING THIS CLASS:
# 1. honestly, i'm not sure if a "code-a-long" style is great,
    # i think what could work better is getting printed worksheets (so they can't copy/paste)
    # with the code on them, and tell them to re-type the code on the sheet.
    # i can provide written explanations on them
# 2. i don't think it's worth adding title, xlabel and ylabel to plots - might overcomplicate it, we just want to focus on plotting the data, can worry about those finer details another time
# 3. when the kids downloaded the dataset, the macs gave it this weird filename and gave csv loading errors, so call the dataset something much simpler like "movies.csv", and then after the kids import the dataset, ask them to rename it to "movies.csv"
# 4. rehearse beforehand how kids download the dataset - i lost so much time on this when teaching it the first time and was so stressful!
# 5. some kids had this weird error where they couldn't open the dataset in google sheets - **always give the dataset link (i.e. from kaggle) as a backup in case this happens! it also means the kids without google classroom access can download + work on the dataset**

# * if a section has `[CODE-A-LONG]` above it, it means the class should type it out
# along with the educator (me!)
# * if a section has `[TALK-ABOUT]` above it, it means the class should not type it
# out, but rather the educator (me) should talk about it and run the code
# for the sake of demonstration
# * if a section has `[EXERCISE]` above it, it means it is an exercise for the
# students, and they should be given a few minutes to try to solve it.

# RECAP
# * what did we do last week?
# * show them the code-a-long.py file from lesson-2

# [CODE-A-LONG] import the pandas library
import pandas as pd

# [CODE-A-LONG] import the plot library
import matplotlib.pyplot as plt

# [CODE-A-LONG] load the .csv file into a variable
dataset = pd.read_csv("simple-movie-ratings-small.csv")

# [TALK-ABOUT]
# * quick recap - what is a .csv file?
# * show them what a .csv file looks like again libre office: columns, rows, headers, etc.

# LINE CHARTS

# * [CODE-A-LONG] line chart of all the movies and their ratings
plt.plot(dataset["Name"], dataset["Rating"])
plt.title('Movie Ratings')
plt.xlabel('Movie Title')
plt.ylabel('Rating')
plt.show()

# [TALK-ABOUT]
# ask the class - is this a good graph?
# why/why not?

# [TALK-ABOUT]
# we should probably change the y-axes
plt.plot(dataset["Name"], dataset["Rating"])
plt.title('Movie Ratings')
plt.xlabel('Movie Title')
plt.ylabel('Rating')
ax = plt.gca()
ax.set_ylim([0, 5.1])
plt.show()

# [EXERCISE]
# do a line chart of all the movies and their year
# plt.plot(?, ?)
# plt.title('Movie Years')
# plt.xlabel('Movie Title')
# plt.ylabel('Year')
# plt.show()


# BAR CHARTS


# * [CODE-A-LONG] bar chart of all the movies and their years
plt.bar(dataset["Name"], dataset["Year"])
plt.title('Movie Years')
plt.xlabel('Movie Title')
plt.ylabel('Movie Year')
plt.show()

# [TALK-ABOUT]
# ask the class - is this a good graph?
# why/why not?

# [TALK-ABOUT]
# what could be done to make it better?
# answer: the y-axis - but what number?

# # [TALK-ABOUT] 
# # set y-axis limits
# # don't get them to type out this code - it's not worth it imo, 
# # the code is not important here, 
# # but the visual graph is important and the fact 
# # you can manipulate the chart with code
plt.bar(dataset["Name"], dataset["Year"])
plt.title('Movie Years')
plt.xlabel('Movie Title')
plt.ylabel('Movie Year')
ax = plt.gca()
ax.set_ylim([1900, 2026])
plt.show()

# [EXERCISE]
# do a bar chart of movies and their ratings
# plt.bar(?, ?)
# plt.title('Movie Ratings')
# plt.xlabel('Movie Title')
# plt.ylabel('Movie Rating')
# plt.show()

# # [TALK-ABOUT]
# # this is an example of how you can manipulate graphs and mislead people
percent_who_agreed_with_court = [62, 54, 54]
percent_who_agreed_with_court_labels = ["Democrats", "Republicans", "Independents"]
plt.bar(percent_who_agreed_with_court_labels, percent_who_agreed_with_court, color=["blue", "red", "green"])
plt.title('Percent who agreed with court')
plt.xlabel('Political Party')
plt.ylabel('Percentage of agreement')
ax = plt.gca()
ax.set_ylim([50, 64])
plt.show()

# # [TALK-ABOUT]
plt.bar(percent_who_agreed_with_court_labels, percent_who_agreed_with_court, color=["blue", "red", "green"])
plt.title('Percent who agreed with court')
plt.xlabel('Political Party')
plt.ylabel('Percentage of agreement')
ax = plt.gca()
ax.set_ylim([0, 100])
plt.show()




# PIE CHARTS


# # [CODE-A-LONG]
number_of_films_per_year = dataset["Year"].value_counts() # explain what `value_counts()` does!
plt.pie(number_of_films_per_year, labels=number_of_films_per_year.index)
plt.title("Number of Films per Year")
plt.show()

# [TALK-ABOUT]
# * why use a pie chart here and not a bar chart?
# * pie charts are used to show **distributions** of something!

# # [EXERCISE]
# # * how would we get a pie chart of all the **ratings** of movies? e.g. 4.0, 5.0, etc.
# number_of_films_per_rating = ?
# plt.pie(number_of_films_per_rating, labels=number_of_films_per_rating.index)
# plt.title("Number of Films per Rating")
# plt.show()

