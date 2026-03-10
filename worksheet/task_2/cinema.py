"""
This is where you should write your code and this is what you need to upload to Gradescope for autograding.

You must NOT change the function definitions (names, arguments).

You can run the functions you define in this file by using test.py (python test.py)
Please do not add any additional code underneath these functions.
"""

import sqlite3


def customer_tickets(conn, customer_id):
    """
    Return a list of tuples:
    (film_title, screen, price)

    Include only tickets purchased by the given customer_id.
    Order results by film title alphabetically.
    """
    query = """
    SELECT films.title, screenings.screen, tickets.price
    FROM screenings
    JOIN films on films.film_id=screenings.film_id
    JOIN tickets on screenings.screening_id=tickets.screening_id
    WHERE tickets.customer_id = ?
    ORDER BY films.title
    """

    result = []
    cursor = conn.execute(query, (customer_id,))
    for row in cursor:
        result.append(row) 
    
    return result
    


def screening_sales(conn):
    """
    Return a list of tuples:
    (screening_id, film_title, tickets_sold)

    Include all screenings, even if tickets_sold is 0.
    Order results by tickets_sold descending.
    """

    query="""
    SELECT screenings.screening_id, films.title, COUNT(ticket_id)
    FROM screenings
    JOIN films on films.film_id=screenings.film_id
    LEFT JOIN tickets on tickets.screening_id=screenings.screening_id
    GROUP BY screenings.screening_id

    ORDER BY COUNT(ticket_id) DESC
    """

    result = []
    cursor = conn.execute(query)
    for row in cursor:
        result.append(row)
    
    return result

    pass


def top_customers_by_spend(conn, limit):
    """
    Return a list of tuples:
    (customer_name, total_spent)

    total_spent is the sum of ticket prices per customer.
    Only include customers who have bought at least one ticket.
    Order by total_spent descending.
    Limit the number of rows returned to `limit`.
    """

    query = """

    SELECT customers.customer_name, SUM(tickets.price)
    FROM tickets
    JOIN customers on customers.customer_id=tickets.customer_id
    GROUP BY customers.customer_id
    ORDER BY SUM(tickets.price) DESC
    LIMIT ?

    """

    result=[]
    cursor = conn.execute(query, (limit, ))
    for row in cursor:
        result.append(row)
    
    return result

