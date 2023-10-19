-- reads from an imported table in database
USE hbtn_0c_0;
SOURCE /~/alx-higher_level_programming/0x0D-SQL_introduction/temperatures.sql;
SELECT city, AVG(value) AS temp
FROM temperatures
GROUP BY city
ORDER BY temp DESC;
