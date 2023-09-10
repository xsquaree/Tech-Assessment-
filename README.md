# Data-Engineer-Internship-Tech-Test--Xiaoxiao

Overview: 

1) Q1.py - Extract the required fields and store the data as restaurants.csv
2) Q2.py - Extract the list of restaurants that have past event in the month of April 2019 and store the data as restaurant_events.csv.
3) Q3.py - Return the aggregates for the ratings and also the table with text rating
4) app.py - runs a web displaying table with text rating (For Q3)
5) Cloud Service Summary.md - Write up summary of how I would design/deploy this using cloud services 

Assumptions: 

- For Q3, assuming user is not allowed to give 0 stars for the aggregate rating
- Threshold are determined by us and these are the threshold: 
  - 1-3 : Poor 
  - 3-3.5 : Average
  - 3.5-4: Good 
  - 4-4.5 : Very Good 
  - 4.5-5 : Excellent

- For Q3, since he would like to find restaurants that have good user ratings, hence I displayed a table from the best rating to the worst with the text rating map.
- For Q3, I used restaurant.csv file as it is extracted from dataset (restaurant_data.json) in Q1
- The URL hosting is for Q3 (http://xiaoxiao2000.pythonanywhere.com/)

How to run source code locally 
1) pip install -r requirements.txt  (If you need to install python, pandas and flask)
2) Navigate to the downloaded folder in the terminal 
3) Finally, run the program with the command below: 
- python Q1.py
- python Q2.py
- python Q3.py
- python app.py (Access the localhost)



