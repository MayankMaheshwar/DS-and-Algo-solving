DAY	DAYS	DATE_SUB('2016-11-29', INTERVAL 10 DAY)
MONTH	MONTHS	DATE_SUB('2015-11-20', INTERVAL 5 MONTH)
WEEK	WEEKS	DATE_SUB('2016-08-20', INTERVAL 5 WEEK)
QUARTER	QUARTERS	DATE_SUB('2016-08-20', INTERVAL 2 QUARTER)
YEAR	YEARS	DATE_SUB('2016-02-23', INTERVAL 2 YEAR)
YEAR_MONTH	'YEARS-MONTHS'	DATE_SUB('2016-02-23', INTERVAL '2-5' YEAR_MONTH)

DATE_SUB(date, INTERVAL, expression, UNIT)

Example
SELECT DATE_SUB('2016-12-25', INTERVAL 3 DAY)
Output is 2016-12-22
