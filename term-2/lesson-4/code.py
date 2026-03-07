import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("books.csv")

# print(dataset.head())

# print(str(dataset["title"].tolist()))

# mean_of_average_ratings = dataset["average_rating"].mean()
# print(mean_of_average_ratings)

# good_books = dataset[dataset["average_rating"] >= 4.0]
# print(good_books)

# scholastic_books = dataset[dataset["publisher"] == "Scholastic Inc."]
# print(scholastic_books)

# line

plt.plot(dataset["title"], dataset["average_rating"], marker='o')
plt.xticks([]) # this removes text on the x-axis - makes it much nicer
plt.title("idk")
plt.xlabel("Books")
plt.ylabel("Average Ratings")
plt.show()

# bar

# small_dataset = dataset.head(3)

# plt.xticks(fontsize=4) # small font size on the x-axis
# plt.bar(small_dataset["title"], small_dataset["number_of_pages"])
# plt.show()

# pie

publisher_counts = dataset["publisher"].value_counts()
plt.pie(publisher_counts, labels=publisher_counts.index, textprops={"fontsize": 6})
plt.show()
