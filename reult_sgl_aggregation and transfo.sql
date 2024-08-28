-- 1.1 Determine the shortest and longest movie durations and name the values as max_duration and min_duration.
SELECT 
    MAX(length) AS max_duration, 
    MIN(length) AS min_duration 
FROM film;

-- 1.2 Express the average movie duration in hours and minutes.
SELECT 
    FLOOR(AVG(length) / 60) AS hours, 
    ROUND(AVG(length) % 60) AS minutes 
FROM film;

-- 2.1 Calculate the number of days that the company has been operating.
SELECT 
    DATEDIFF(
        (SELECT MAX(rental_date) FROM rental), 
        (SELECT MIN(rental_date) FROM rental)
    ) AS days_operating;

-- 2.2 Retrieve rental information and add two additional columns to show the month and weekday of the rental. Return 20 rows of results.
SELECT 
    rental_id, 
    rental_date, 
    DATE_FORMAT(rental_date, '%M') AS rental_month, 
    DATE_FORMAT(rental_date, '%W') AS rental_weekday 
FROM rental 
LIMIT 20;

-- 2.3 Bonus: Add a column DAY_TYPE with values 'weekend' or 'workday' depending on the day of the week.
SELECT 
    rental_id, 
    rental_date, 
    DATE_FORMAT(rental_date, '%M') AS rental_month, 
    DATE_FORMAT(rental_date, '%W') AS rental_weekday,
    CASE
        WHEN DATE_FORMAT(rental_date, '%W') IN ('Saturday', 'Sunday') THEN 'weekend'
        ELSE 'workday'
    END AS DAY_TYPE
FROM rental 
LIMIT 20;

-- 3. Retrieve the film titles and their rental duration, replacing NULL with 'Not Available'.
SELECT 
    title, 
    IFNULL(rental_duration, 'Not Available') AS rental_duration 
FROM film 
ORDER BY title ASC;

-- 4. Bonus: Retrieve concatenated first and last names of customers with the first 3 characters of their email.
SELECT 
    CONCAT(first_name, ' ', last_name) AS full_name, 
    LEFT(email, 3) AS email_prefix 
FROM customer 
ORDER BY last_name ASC;

-- Challenge 2
-- 1.1 The total number of films that have been released.
SELECT COUNT(*) AS total_films FROM film;

-- 1.2 The number of films for each rating.
SELECT rating, COUNT(*) AS number_of_films 
FROM film 
GROUP BY rating;

-- 1.3 The number of films for each rating, sorted in descending order of the number of films.
SELECT rating, COUNT(*) AS number_of_films 
FROM film 
GROUP BY rating 
ORDER BY number_of_films DESC;

-- 2.1 Mean film duration for each rating, sorted in descending order.
SELECT 
    rating, 
    ROUND(AVG(length), 2) AS average_duration 
FROM film 
GROUP BY rating 
ORDER BY average_duration DESC;

-- 2.2 Identify which ratings have a mean duration of over two hours.
SELECT 
    rating, 
    ROUND(AVG(length), 2) AS average_duration 
FROM film 
GROUP BY rating 
HAVING average_duration > 120;

-- 3. Bonus: Determine which last names are not repeated in the actor table.
SELECT 
    last_name, 
    COUNT(*) AS name_count 
FROM actor 
GROUP BY last_name 
HAVING name_count = 1;
