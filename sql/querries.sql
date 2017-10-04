"there are database tests"
select * from customer
where
customer.id = 2;

select * from customer;

select * from "order";

select * from order_details;

select * from product;


"only orders from one cart"
select id, customer_id, quantity from "order"
inner join
order_details on "order".id = order_details.order_id;


"query that shows customer data and his cart content"
"id username productid quantity"
select customer.id, customer.user_name, order_details.product_id, order_details.quantity
from customer
inner join
order_details on customer.id = order_details.order_id;


"do the same but instead product id change to product name"
"this would be good for print function"
select
customer.id as id_customer,
customer.user_name,
product.id as id_produktu,
order_details.product_id as id_order_details,
product.name as product_name,
order_details.quantity
from ((customer
inner join
order_details on customer.id = order_details.order_id)
inner join product on order_details.product_id = product.id
)
order by id_customer
;

"this would be good for print function"
select
customer.id as id_customer,
customer.user_name,
product.name as product_name,
order_details.quantity
from ((customer
inner join
order_details on customer.id = order_details.order_id)
inner join product on order_details.product_id = product.id
)
order by id_customer
;

"**********************************"
"operations on database tests"

"add order to orders table"
insert into "order" (customer_id) values (2);

"add cart items to details..."
insert into  order_details (order_id, product_id, quantity) values (1, 2, 11)
insert into  order_details (order_id, product_id, quantity) values (1, 1, 5)
insert into  order_details (order_id, product_id, quantity) values (1, 4, 100)