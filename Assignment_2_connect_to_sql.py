import mysql.connector as sq
mydb = sq.connect(host='localhost', user='root', passwd='0510Hh!!', buffered=True)

mycursor = mydb.cursor()
mycursor.execute('CREATE DATABASE nj_state_teachers_salaries')

mycursor.execute("CREATE TABLE nj_state_teachers_salaries.nj_state_teachers_salaries(last_name TEXT NOT NULL, \
first_name TEXT NOT NULL, county TEXT, district TEXT, school TEXT, \
primary_job TEXT, fte DECIMAL(10,5), salary INT, certificate TEXT, \
subcategory TEXT, teaching_route TEXT, highly_qualified TEXT, \
experience_district INT, experience_nj INT, experience_total INT)")

SQLCMD = """LOAD DATA INFILE '/Users/vivhuang/MySQLfiles/nj_state_teachers_salaries.csv' 
INTO TABLE nj_state_teachers_salaries.nj_state_teachers_salaries
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' 
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS"""

mycursor.execute(SQLCMD)

mydb.commit()