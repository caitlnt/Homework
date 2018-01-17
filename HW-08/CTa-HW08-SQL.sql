-- CTa-HW08-SQL

---------------------------------------------------------------------------------------------------------------------------------------------------

-- USING SAKILA DATABASE FOR HOMEWORK

USE sakila;

----------------------------------------------------------------------------------------------------------------------------------------------------

-- 1a. Display the first and last names of all actors from the table actor.
select first_name, last_name
from actor;


-- 1b. Display the first and last name of each actor in a single column in upper case letters. Name the column Actor Name.
select (concat(upper(first_name),' ',upper(last_name))) as 'Actor_Name'
from actor;


-- 2a. You need to find the ID number, first name, and last name of an actor, of whom you know only the first name, "Joe." What is one query would you use to obtain this information?
select actor_id, first_name, last_name
from actor
where first_name = 'Joe';


-- 2b. Find all actors whose last name contain the letters GEN:
select *
from actor
where last_name like '%GEN%';


-- 2c. Find all actors whose last names contain the letters LI. This time, order the rows by last name and first name, in that order:
select *
from actor
where last_name like '%LI%'
order by last_name desc;


-- 2d. Using IN, display the country_id and country columns of the following countries: Afghanistan, Bangladesh, and China:
select country_id, country
from country
where country in ('Afghanistan', 'Bangladesh', 'China');


-- 3a. Add a middle_name column to the table actor. Position it between first_name and last_name. Hint: you will need to specify the data type.
alter table actor
add column middle_name varchar(50) after first_name;

	-- verify middle_name is positioned after first_name
	select * from actor;


-- 3b. You realize that some of these actors have tremendously long last names. Change the data type of the middle_name column to blobs.
alter table actor modify middle_name blob;

	-- verify middle_name changed data_type to blob
	select column_name, data_type from information_schema.columns
	where table_name = 'actor' and column_name = 'middle_name';


-- 3c. Now delete the middle_name column.
alter table actor drop column middle_name;

	-- verify middle_name is no longer in table
	select * from actor;


-- 4a. List the last names of actors, as well as how many actors have that last name.
select last_name, count(*) as 'quantity'
from actor
group by last_name;


-- 4b. List last names of actors and the number of actors who have that last name, but only for names that are shared by at least two actors
select last_name, count(*) as 'quantity'
from actor
group by last_name 
having quantity >= 2;


-- 4c. Oh, no! The actor HARPO WILLIAMS was accidentally entered in the actor table as GROUCHO WILLIAMS, the name of Harpo's second cousin's husband's yoga teacher. 
-- Write a query to fix the record.

	-- find groucho williams	
	select * 
	from actor
	where first_name = 'GROUCHO' and last_name = 'WILLIAMS';

update actor
set first_name = 'HARPO'
where first_name = 'GROUCHO' and last_name = 'WILLIAMS';

	-- verify name was changed
	select *
	from actor where last_name  = 'WILLIAMS';


-- 4d. Perhaps we were too hasty in changing GROUCHO to HARPO. It turns out that GROUCHO was the correct name after all! 
-- In a single query, if the first name of the actor is currently HARPO, change it to GROUCHO. Otherwise, change the first name to MUCHO GROUCHO, 
-- as that is exactly what the actor will be with the grievous error. BE CAREFUL NOT TO CHANGE THE FIRST NAME OF EVERY ACTOR TO MUCHO GROUCHO, HOWEVER! 
-- (Hint: update the record using a unique identifier.)

update actor
set first_name = 'GROUCHO'
where actor_id = '172';

	-- verify name was changed
	select *
	from actor where last_name  = 'WILLIAMS';


-- 5a. You cannot locate the schema of the address table. Which query would you use to re-create it?
create database actor;


-- 6a. Use JOIN to display the first and last names, as well as the address, of each staff member. Use the tables staff and address:
select s.first_name, s.last_name, a.address
from staff s
join address a on s.address_id = a.address_id;


-- 6b. Use JOIN to display the total amount rung up by each staff member in August of 2005. Use tables staff and payment.
select s.first_name, s.last_name, sum(p.amount) as 'total_amount'
from staff s
join payment p on s.staff_id = p.staff_id
where Monthname(payment_date) = 'August' and Year(payment_date) = '2005'
group by s.last_name, s.first_name;


-- 6c. List each film and the number of actors who are listed for that film. Use tables film_actor and film. Use inner join.
select title, count(actor_id) as 'Number_Actors'
from film_actor fa
inner join film f on fa.film_id = f.film_id
group by title;


-- 6d. How many copies of the film Hunchback Impossible exist in the inventory system?
select f.title, count(i.film_id)
from film f
join inventory i on f.film_id = i.film_id
where f.title = 'Hunchback Impossible';


-- 6e. Using the tables payment and customer and the JOIN command, list the total paid by each customer. List the customers alphabetically by last name:
select c.first_name, c.last_name, sum(p.amount) as 'total_amount'
from customer c
join payment p on c.customer_id = p.customer_id
group by c.first_name, c.last_name
order by c.last_name asc;


-- 7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. As an unintended consequence, films starting with the letters K and Q have also soared in popularity. 
-- Use subqueries to display the titles of movies starting with the letters K and Q whose language is English.

select title 
from film 
where language_id = 
(
select language_id 
from language 
where name = 'English'
)
and title like 'K%'or title like 'Q%';


-- 7b. Use subqueries to display all actors who appear in the film Alone Trip.
select first_name, last_name
from actor
where actor_id in 
(select actor_id from film_actor where film_id in
(select film_id from film where title = 'Alone Trip'));


select * from actor;

-- 7c. You want to run an email marketing campaign in Canada, for which you will need the names and email addresses of all Canadian customers. Use joins to retrieve this information.
select first_name, last_name, email
from customer c 
inner join address a on c.address_id = a.address_id
inner join city y on a.city_id = y.city_id
inner join country r on y.country_id = r.country_id
where r.country = 'Canada';


-- 7d. Sales have been lagging among young families, and you wish to target all family movies for a promotion. Identify all movies categorized as famiy films.
select title 
from film f
inner join film_category fc on f.film_id = fc.film_id
inner join category c on fc.category_id = c.category_id
where c.name = 'Family';


-- 7e. Display the most frequently rented movies in descending order.
select title, count(title) as 'rental_qty'
from film f
inner join inventory i on f.film_id = i.film_id
inner join rental r on i.inventory_id = r.inventory_id
group by f.title
order by rental_qty desc;


-- 7f. Write a query to display how much business, in dollars, each store brought in.
select city, country, sum(p.amount) as 'total_sales'
from payment p
join rental r on p.rental_id = r.rental_id
join inventory i on r.inventory_id = i.inventory_id
join store s on i.store_id = s.store_id
join address a on s.address_id = a.address_id
join city c on a.city_id = c.city_id
join country y on c.country_id = y.country_id
join staff f on s.manager_staff_id = f.staff_id
group by s.store_id
order by y.country, c.city;


-- 7g. Write a query to display for each store its store ID, city, and country.
select store_id, city, country
from store s, address a , city c, country y
where s.address_id = a.address_id
and a.city_id = c.city_id
and c.country_id = y.country_id;


-- 7h. List the top five genres in gross revenue in descending order. (Hint: you may need to use the following tables: category, film_category, inventory, payment, and rental.)
select name, sum(p.amount) as 'revenue'
from payment p
join rental r on p.rental_id = r.rental_id
join inventory i on r.inventory_id = i.inventory_id
join film f on i.film_id = f.film_id
join film_category fc on f.film_id = fc.film_id
join category c on fc.category_id = c.category_id
group by name
order by revenue
limit 5;


-- 8a. In your new role as an executive, you would like to have an easy way of viewing the Top five genres by gross revenue. Use the solution from the problem above to create a view. 
-- If you haven't solved 7h, you can substitute another query to create a view.
create view v_top_5_genre as 
select name, sum(p.amount) as 'revenue'
from payment p
join rental r on p.rental_id = r.rental_id
join inventory i on r.inventory_id = i.inventory_id
join film f on i.film_id = f.film_id
join film_category fc on f.film_id = fc.film_id
join category c on fc.category_id = c.category_id
group by name
order by revenue
limit 5;

	-- verify view exists after creation
    select * from v_top_5_genre;
    
    
-- 8b. How would you display the view that you created in 8a?
select * from v_top_5_genre;


-- 8c. You find that you no longer need the view top_five_genres. Write a query to delete it.
drop view v_top_5_genre;

	-- verify that the view no longer exists
	select * from v_top_5_genre;

