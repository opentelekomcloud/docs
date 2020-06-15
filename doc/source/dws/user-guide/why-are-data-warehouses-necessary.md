# Why Are Data Warehouses Necessary?<a name="dws_03_0003"></a>

## Status Quo and Requirements<a name="section776152855415"></a>

A large amount of business operation data \(orders, stocks, materials, and payments\) is generated in the business operation systems and background \(transactional\) database of enterprises. 

Enterprises' decision makers must categorize and analyze the data to obtain the service characteristics, providing data for business decision-making. 

## Difficulties<a name="section181742342540"></a>

Data categorization and analysis involve the concurrent access to the data in multiple database tables. That is, multiple tables being updated by different transactions may be locked at the same time, which may cause complications to the database systems during peak hours.

-   If multiple tables are locked at the same time, the latency during complex queries increases. 
-   The transactions that are updating the database tables are blocked, delaying or even interrupting services. 

## Solution<a name="section1829395716559"></a>

Data warehouses excel in to enterprise data analysis scenarios involving data aggregation and association, helping users effortlessly mine massive amounts of data for greater business intelligence to implement more accurate decision making. The mining requires complex queries that involve the aggregation and association of data on multiple tables. 

By implementing the ETL process, data in business operation databases can be copied to data warehouses for analysis and computing. Data can be aggregated from multiple business operation systems into one data warehouse for better association, analysis, and actionable insights.

Data warehouses and standard transaction-oriented databases such as Oracle, MS SQL Server, and MySQL use different design modes. Data warehouses are optimized in terms of data aggregation and association but the transaction or data adding and deleting functions or performance may not be guaranteed. Therefore, data warehouses and databases apply to different scenarios. Transactional databases are dedicated to transaction processing \(business operation of enterprises\) whereas data warehouses excel at complex data analysis. In conclusion, databases apply to data updates whereas data warehouses apply to data analysis. 

