# dataset link for backup (in case google classroom doesn't work)
# https://www.kaggle.com/datasets/jealousleopard/goodreadsbooks
# will need to run some pre-processing on it (e.g. remove some columns + rows to make it muuuuch simpler)

import pandas as pd
import matplotlib.pyplot as plt

# some rows are malformed so skip them
dataset = pd.read_csv("goodreads-books-full.csv", on_bad_lines='skip')

dataset = dataset.head(100)

dataset = dataset.drop(["bookID", "isbn", "isbn13", "text_reviews_count", "publication_date", "language_code"], axis=1)

dataset = dataset.rename(columns={"  num_pages": "number_of_pages", "ratings_count": "number_of_ratings"})

dataset.to_csv("books.csv", index=False)
