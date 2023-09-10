#Full Name: Zheng Xiaoxiao 

import pandas as pd
import json
from pandas.io.json import json_normalize
import requests

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
country_code = pd.read_excel('Country-Code.xlsx',sheet_name='Sheet1')

df['Country Code'] = df['Country Code'].astype(str)
country_code['Country Code'] = country_code['Country Code'].astype(str)

merged_df = pd.merge(df, country_code, on='Country Code', how='inner')
merged_df = merged_df.drop(columns=['Country Code'])
merged_df['User Aggregate Rating'] = merged_df['User Aggregate Rating'].astype(float)
print('')

try:
    merged_df.to_csv('restaurants.csv', index=False)
    print("downloaded restaurants.csv")
 
except:
    print ("Unable to extract and import to restaurants.csv")