#Full Name: Zheng Xiaoxiao 

import pandas as pd
import csv

df = pd.read_csv('restaurants.csv')

#Assum
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
print("4-5: Excellent")
print("3-4: Very Good")
print("2-3: Good")
print("1-2: Average")


print("Aggregates for the ratings: ")
print(aggregates)
print("----------------------------")
print("")

df_ratings = df.sort_values(by='User Aggregate Rating', ascending=False)

print(df_ratings)