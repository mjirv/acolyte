-- question: how many customers do we have?
SELECT count(*) from customers;

-- question: get the 5 customers with the most returned orders
SELECT customers.customer_id, customers.first_name, customers.last_name, sum(orders.amount) as order_amount
from customers
inner join orders on customers.customer_id = orders.customer_id
where status = 'returned'
group by customers.customer_id, first_name, last_name
order by sum(orders.amount) desc limit 5;

-- question: how many customers have used gift cards?
SELECT count(distinct customer_id)
from orders
where gift_card_amount > 0