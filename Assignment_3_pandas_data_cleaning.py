import pandas as pd
import numpy as np
df = pd.read_csv('/autograder/source/nj_state_teachers_salaries.csv')

# Eliminate all blank lines
df.dropna(how='all', inplace=True)
# Remove trailing space for first_name column
df['first_name']=df['first_name'].str.strip()
# Check each column and change all invalid values to NaN
df['last_name']=df['last_name'].replace('[^A-Za-z\\s\'\-]', np.NaN, regex=True)
df['first_name']=df['first_name'].replace('[^A-Za-z\\s\'\-]', np.NaN, regex=True)
df['county']=df['county'].replace('[^A-Za-z\\s]', np.NaN, regex=True)
df['district']=df['district'].replace('[^A-Za-z\\s\-\.\:\/\'\(\)]', np.NaN, regex=True)
df['school']=df['school'].replace('[^A-Za-z0-9\\s\-\.\/\#\@\(\)\'\:\&]', np.NaN, regex=True)
df['primary_job']=df['primary_job'].replace('[^A-Za-z0-9\\s\/\(\)\,\.\:\&\-]', np.NaN, regex=True)
df['fte']=df['fte'].replace('[^0-9]', np.NaN, regex=True)
df['salary']=df['salary'].replace('[^0-9]', np.NaN, regex=True)
df['certificate']=df['certificate'].replace('[^A-Za-z\\s]', np.NaN, regex=True)
df['subcategory']=df['subcategory'].replace('[^A-Za-z\\s]', np.NaN, regex=True)
df['teaching_route']=df['teaching_route'].replace('[^A-Za-z]', np.NaN, regex=True)
df['highly_qualified']=df['highly_qualified'].replace('[^A-Za-z0-9\\s\'\.\,\/]', np.NaN, regex=True)
df['experience_district']=df['experience_district'].replace('[^0-9]', np.NaN, regex=True)
df['experience_nj']=df['experience_nj'].replace('[^0-9]', np.NaN, regex=True)
df['experience_total']=df['experience_total'].replace('[^0-9]', np.NaN, regex=True)
# Drop all rows with NaN in any columns
df=df.dropna()
# Save cleaned data back to csv file
df.to_csv('/autograder/submission/nj_state_teachers_salaries.csv', index=False)
# Use python MySQL connector and create a connection
import mysql.connector as sq
mydb = sq.connect(host='localhost', user='User', passwd="password", buffered=True)
# Create a cursor
mycursor = mydb.cursor()
# Create a database
mycursor.execute('CREATE DATABASE nj_state_teachers_salaries')
# Create a table
mycursor.execute("CREATE TABLE nj_state_teachers_salaries.nj_state_teachers_salaries(last_name TEXT NOT NULL, \
first_name TEXT NOT NULL, county TEXT, district TEXT, school TEXT, \
primary_job TEXT, fte DECIMAL(10,5), salary INT, certificate TEXT, \
subcategory TEXT, teaching_route TEXT, highly_qualified TEXT, \
experience_district INT, experience_nj INT, experience_total INT)")
# Query to load data from csv file into databse
SQLCMD = """LOAD DATA INFILE '/autograder/submission/nj_state_teachers_salaries.csv' 
INTO TABLE nj_state_teachers_salaries.nj_state_teachers_salaries
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' 
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS"""
# Execute SQLCMD
mycursor.execute(SQLCMD)
# Commit to confirm all changes
mydb.commit()