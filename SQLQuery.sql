select * from [dbo].[Sample - Superstore]
-- to verify columns in the table
select COLUMN_NAME 
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'Sample - Superstore';

-- Sales Trends - 1. Monthly sales trends

select 
FORMAT(CAST([Order Date] as Date), 'yyyy-MM') as month,
sum(cast (sales as float)) as Total_Sales 
from [Sample - Superstore]
group by FORMAT(cast ([Order Date] as Date), 'yyyy-MM')
ORDER BY MONTH;

-- Sales Trends - 1. Yearly sales trends

select 
year(cast([Order Date] as Date)) as year,
sum(cast(sales as float)) as Total_Sales
from [Sample - Superstore]
group by year(cast ([Order Date] as Date ))
Order by Year;

--regional performance query

select
region,
sum(cast(sales as float)) as Total_Sales,
sum(cast(profit as float)) as Total_Profit
from [Sample - Superstore]
group by Region
order by Total_Sales DESC;

-- Customer Segmentation Query

select
Segment,
sum(cast(sales as float)) as Total_Sales,
count( distinct [Customer ID]) as Unique_Customers 
from [Sample - Superstore]
group by Segment
order by Total_Sales DESC;

-- category and sub-category performance analysis 

select
[Category],
[Sub-Category],
sum(cast(sales as float)) as Total_Sales,
sum(cast(profit as float)) as Total_Profit
from [Sample - Superstore]
group by Category, [Sub-Category]
order by Total_Sales DESC;

-- Top 10 Customers by sales.

select top 10
[Customer ID],
sum(cast(sales as float)) as Total_Sales 
from [Sample - Superstore]
group by [Customer ID]
order by Total_Sales DESC;

-- shipping mode performance analysis

select 
[Ship Mode],
sum(cast(sales as float)) as Total_Sales,
 sum(cast(Profit as float)) as Total_Profit
from [Sample - Superstore]
group by [Ship Mode]
order by Total_Sales DESC;
