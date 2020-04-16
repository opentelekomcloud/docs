# How Can I Export Monitoring Data?<a name="EN-US_TOPIC_0084812083"></a>

1.  On the console, choose  **Cloud Service Monitoring**  or  **Server Monitoring**.
2.  Click  **Export Data**.
3.  Set the time range, resource type, dimension, monitored object, and metric.
4.  Click  **Export**.

-   The first row in the exported monitoring report displays the user name, region name, service name, instance name, instance ID, metric name, monitoring data, time, and timestamp. This report enables users to view historical monitoring data.
-   If you need to convert the time in Unix timestamp to the time of the target time zone, perform the following steps:
    1.  Use Excel to open a .csv file. 
    2.  Use the following formula to convert the time:

        Target time = \(Unix timestamp/1000 + \(Target time zone\) x 3600\)/86400 + 70 x 365 + 19

    3.  Set cell format to  **Date**.

        For example, the Unix timestamp is 1475918112000 and the target time is Beijing time. Beijing is located in the UTC+8 time zone. Therefore, the target time is calculated as follows:

        Target time = \(1475918112000/1000 + \(+8\) x 3600\)/86400 + 70 x 365 + 19

        Set the cell format to date and select a presentation format such as 2016/3/14 13:30. Then, the final time is obtained and presented as 2016/10/8 17:15.



