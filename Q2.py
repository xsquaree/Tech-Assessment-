#Full Name: Zheng Xiaoxiao 

import pandas as pd
import json
from pandas.io.json import json_normalize
import requests


response = requests.get("https://raw.githubusercontent.com/Papagoat/brain-assessment/main/restaurant_data.json")
json_data = json.loads(response.text)

restaurants_with_events = []
for restaurant in json_data[0]["restaurants"]:
    events = restaurant["restaurant"].get("zomato_events", [])
    for event in events:
        start_date = event["event"]["start_date"]
        end_date = event["event"]["end_date"]
        if start_date.startswith("2019-04") or end_date.startswith("2019-04"):
            photo_url = event["event"]["photos"][0]["photo"]["url"] if event["event"]["photos"] else "NA"
            restaurants_with_events.append({
                "Event Id": event["event"]["event_id"],
                "Restaurant Id": restaurant["restaurant"]["R"]["res_id"],
                "Restaurant Name": restaurant["restaurant"]["name"],
                "Photo URL": photo_url,
                "Event Title": event["event"]["title"],
                "Event Start Date": start_date,
                "Event End Date": end_date
            })

df = pd.DataFrame(restaurants_with_events)
df['Event Start Date'] = pd.to_datetime(df['Event Start Date'], format='%Y-%m-%d')
df['Event End Date'] = pd.to_datetime(df['Event End Date'], format='%Y-%m-%d')
# Fill empty values with "NA"
df = df.fillna("NA")
df.head()

try:    
    df.to_csv('restaurant_events.csv', index=False)
    print("downloaded restaurant_events.csv")
 
except:
    print ("Unable to extract and import to restaurant_events.csv")