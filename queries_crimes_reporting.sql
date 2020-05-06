use crimes;

# Creating the database and the table 
# Since the csv file it is quiet big(1.6 GB), it has benn used mysq to load the data

create database crimes;
create table crimes(ID integer primary key auto_increment);

load data local infile 
"/var/lib/mysql-files/Crimes_-_2001_to_present.csv" 
into table crimes 
fields terminated by "," lines 
terminated by "\n" 
ignore 1 rows;




SELECT 
    *
FROM
    crimes
LIMIT 10;

SELECT 
    Year, COUNT(*) AS NR
FROM
    crimes
WHERE
    `Arrest` = 'true'
GROUP BY Year
ORDER BY NR DESC;

SELECT 
    `Primary Type`, COUNT(`Primary Type`) AS NR_CASES
FROM
    crimes
GROUP BY `Primary Type`
ORDER BY NR_CASES DESC;

SELECT 
    `Year`, District, COUNT(District) AS Nr_Cases
FROM
    crimes
GROUP BY Year , District
ORDER BY Nr_Cases DESC;

SELECT 
    `Primary Type`, COUNT(`Primary Type`) AS count_
FROM
    crimes
GROUP BY `Primary Type`
ORDER BY count_ DESC
LIMIT 1;
