/* Ejercicios SQL */

/* 1. Show actor's first and last name. */
select first_name, last_name from actor;

/* 2. Show actor name and film name. */
SELECT actor.first_name, actor.last_name, film.title FROM actor JOIN film_actor ON actor.actor_id=film_actor.actor_id JOIN film ON film_actor.film_id=film.film_id;

/* 3. Show actor name and number in descending order. */
SELECT actor.first_name, actor.last_name, count(film_actor.film_id) FROM actor JOIN film_actor ON actor.actor_id=film_actor.actor_id GROUP BY actor.first_name, actor.last_name ORDER BY count(film_actor.film_id) DESC;

/* 4. Show films and number of rentals. */
SELECT title, count(rental.rental_id) FROM film JOIN inventory ON film.film_id=inventory.film_id JOIN rental ON inventory.inventory_id=rental.inventory_id GROUP BY title;

/* 5. Show film and amount. */
SELECT title, sum(payment.amount) FROM film JOIN inventory ON film.film_id=inventory.film_id JOIN rental ON inventory.inventory_id=rental.inventory_id JOIN payment ON rental.rental_id=payment.rental_id GROUP BY title;

/* 6. Name of the best client (highest total payment). */
SELECT customer.first_name, customer.last_name FROM customer JOIN payment ON customer.customer_id=payment.customer_id GROUP BY customer.first_name, customer.last_name ORDER BY sum(payment.amount) DESC FETCH FIRST 1 ROWS ONLY;

/* 7. Name of the best client (highest amount of rentals). */
SELECT customer.first_name, customer.last_name FROM customer JOIN rental ON customer.customer_id=rental.customer_id GROUP BY customer.first_name, customer.last_name ORDER BY count(rental.rental_id) DESC FETCH FIRST 1 ROWS ONLY;