/*a. Use a SELECT statement to generate and output a random sample to :
• Include all columns
• Include field (column) headings
• Randomly select 777 records with a seed value of 7
• Output results to a CSV file named teachersample.csv*/
SELECT 'last_name',	
       'first_name',
       'county',	
       'district',	
       'school',	
       'primary_job',	
       'fte',	
       'salary',	
       'certificate',	
       'subcategory',	
       'teaching_route',	
       'highly_qualified',	
       'experience_district',	
       'experience_nj',	
       'experience_total' 
UNION
(SELECT last_name,	
	first_name,
        county,	
        district,	
        school,	
        primary_job,	
        fte,	
        salary,	
        certificate,	
        subcategory,	
        teaching_route,	
        highly_qualified,	
        experience_district,	
        experience_nj,	
        experience_total 
FROM nj_state_teachers_salaries.nj_state_teachers_salaries
ORDER BY RAND(7)
LIMIT 777)
INTO OUTFILE '/autograder/submission/teachersample.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

/*b. Create a new database called teacher_sample and a table named teachers using teachersample.csv*/
CREATE SCHEMA teacher_sample;

CREATE TABLE teacher_sample.teachers
(last_name TEXT NOT NULL, 
first_name TEXT NOT NULL, 
county TEXT, 
district TEXT, 
school TEXT, 
primary_job TEXT, 
fte DECIMAL(10,5), 
salary INT, 
certificate TEXT, 
subcategory TEXT, 
teaching_route TEXT, 
highly_qualified TEXT, 
experience_district INT, 
experience_nj INT, 
experience_total INT);

LOAD DATA INFILE '/autograder/source/teachersample2.csv'
INTO TABLE teacher_sample.teachers
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

/*c. Using the teacher_sample database, perform the following tasks:
• Calculate the average salary
• Calculate the number of people whose salary is more than 150,000.
• Get the last name of the ones who make more than 150,000 but has less
than 5 years of total experience
• Get the highest salary for Preschool, School Counselor, Principal (anyone
with the word Principal in the title) , School Psychologist, and
Kindergarten.
• Get the last name, first name, and salary of the lowest earner who works in
Atlantic City*/
SELECT AVG(salary) FROM teacher_sample.teachers;

SELECT COUNT(*) FROM teacher_sample.teachers WHERE salary>150000;

SELECT last_name
FROM teacher_sample.teachers 
WHERE salary>150000
AND experience_total<5;

SELECT MAX(salary) FROM teacher_sample.teachers WHERE primary_job = 'Preschool';
SELECT MAX(salary) FROM teacher_sample.teachers WHERE primary_job = 'School Counselor';
SELECT MAX(salary) FROM teacher_sample.teachers WHERE primary_job LIKE '%Principal%';
SELECT MAX(salary) FROM teacher_sample.teachers WHERE primary_job = 'School Psychologist';
SELECT MAX(salary) FROM teacher_sample.teachers WHERE primary_job = 'Kindergarten';

SELECT last_name, first_name, salary
FROM teacher_sample.teachers
WHERE district = 'Atlantic City'
ORDER BY salary
LIMIT 1;

/*d. Get the total number of employees working in Passaic City with more than ten years of total experience.*/
SELECT COUNT(*)
FROM teacher_sample.teachers
WHERE district = 'Passaic City'
AND experience_total > 10






