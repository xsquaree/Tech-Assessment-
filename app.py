
from flask import Flask, render_template
import pandas as pd
import json
from pandas.io.json import json_normalize
import requests
from pathlib import Path

app = Flask(__name__)

response = requests.get("https://raw.githubusercontent.com/Papagoat/brain-assessment/main/restaurant_data.json")
json_data = json.loads(response.text)


restaurants = json_data[0]["restaurants"]
extracted_fields = []

for restaurant in restaurants:
    data = restaurant["restaurant"]
    extracted_fields.append({
        "Restaurant Id": data["R"]["res_id"],
        "Restaurant Name": data["name"],
        "Country Code": data['location']['country_id'],
        "City": data["location"]["city"],
        "User Rating Votes": data["user_rating"]["votes"],
        "User Aggregate Rating": data["user_rating"]["aggregate_rating"],
        "Cuisines": data["cuisines"]
    })


df = pd.DataFrame(extracted_fields)
country_code = pd.read_excel("Country-Code.xlsx",sheet_name='Sheet1')

df['Country Code'] = df['Country Code'].astype(str)
country_code['Country Code'] = country_code['Country Code'].astype(str)

merged_df = pd.merge(df, country_code, on='Country Code', how='inner')
merged_df = merged_df.drop(columns=['Country Code'])
merged_df['User Aggregate Rating'] = merged_df['User Aggregate Rating'].astype(float)


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


@app.route('/')
def index():

    merged_df['Text Rating'] = merged_df['User Aggregate Rating'].apply(map_text_rating)
    df_ratings = merged_df.sort_values(by='User Aggregate Rating', ascending=False)

    aggregates = df_ratings['Text Rating'].value_counts()
    print("Threshold for ratings:")
    print("4-5: Excellent")
    print("3-4: Very Good")
    print("2-3: Good")
    print("1-2: Average")
    return render_template('index.html', tables=[df_ratings.to_html(classes='data', header="true")])


if __name__ == '__main__':
    app.run(debug = True)


