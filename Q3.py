#Full Name: Zheng Xiaoxiao 

import pandas as pd
import csv

df = pd.read_csv('restaurants.csv')

def map_text_rating(rating):
    if 1 <= rating < 3:
        return 'Poor'
    elif 3 <= rating < 3.5:
        return 'Average'
    elif 3.5 <= rating < 4:
        return 'Good'
    elif 4 <= rating < 4.5:
        return 'Very Good'
    elif 4.5 <= rating <= 5:
        return 'Excellent'
    else:
        return 'No rating'
    
df['Text Rating'] = df['User Aggregate Rating'].apply(map_text_rating)

aggregates = df['Text Rating'].value_counts()
print("Threshold for ratings:") 
print("4.5-5: Excellent")
print("4-4.5: Very Good")
print("3.5-4: Good")
print("3-3.5: Average")
print("1-3: Poor")


print("Aggregates for the ratings: ")
print(aggregates)
print("----------------------------")
print("")

df_ratings = df.sort_values(by='User Aggregate Rating', ascending=False)

print(df_ratings)