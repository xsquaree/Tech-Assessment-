#Full Name: Zheng Xiaoxiao 

import pandas as pd
import csv

df = pd.read_csv('restaurants.csv')


def map_text_rating(rating):
    if 0 <= rating < 1:
        return 'Poor'
    elif 1 <= rating < 2:
        return 'Average'
    elif 2 <= rating < 3:
        return 'Good'
    elif 3 <= rating < 4:
        return 'Very Good'
    elif 4 <= rating <= 5:
        return 'Excellent'
    else:
        return 'No rating'
    
df['Text Rating'] = df['User Aggregate Rating'].apply(map_text_rating)

aggregates = df['Text Rating'].value_counts()

print("Aggregates for the ratings: ")
print(aggregates)
print("----------------------------")
print("")

df_ratings = df.sort_values(by='User Aggregate Rating', ascending=False)

print(df_ratings)