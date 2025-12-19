USE food_delivery;
select count(*) from food_delivery_5_sheets_clean;
select *
from food_delivery_5_sheets_clean
limit 10;
select order_id , count(*)
from food_delivery_5_sheets_clean
group by Order_ID
having count(*) > 1;
select count(*) as total_orders
from food_delivery_5_sheets_clean;
select count(*) as delayed_orders
from food_delivery_5_sheets_clean
where Delay_Reason <> 'on-time' ;
select count(*) as on_time_orders
from food_delivery_5_sheets_clean
where Delay_Reason ='on-time';
select
avg(timestampdiff(minute,start_time, end_time)) as avg_delivery_minutes
from food_delivery_5_sheets_clean;
SELECT 
    Delay_Reason,
    COUNT(*) AS delay_count
FROM food_delivery_5_sheets_clean
WHERE Delay_Reason <> 'On-Time'
GROUP BY Delay_Reason
ORDER BY delay_count DESC;
SELECT 
    Rider_ID,
    AVG(TIMESTAMPDIFF(MINUTE, Start_Time, End_Time)) AS avg_delivery_time
FROM food_delivery_5_sheets_clean
GROUP BY Rider_ID
ORDER BY avg_delivery_time;

