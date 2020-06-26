# Viewing Slow Query Logs<a name="en-us_topic_slow_query_log"></a>

## **Scenarios**<a name="section61232893165332"></a>

Slow query logs record statements that exceed  **long\_query\_time**. You can use these logs to identify and optimize the statements that are executing slowly.

RDS supports the following statement types:

-   SELECT
-   INSERT
-   UPDATE
-   DELETE
-   CREATE

## Viewing Log Details<a name="section467223910567"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, click the target DB instance.
5.  In the navigation pane on the left, choose  **Logs**. On the  **Slow Query Logs**  page, view details about slow query logs.
    -   You can view the slow query log records of a specified execution statement type or a specific time period.
    -   The  **long\_query\_time**  parameter determines when a slow query log is recorded. However, changes to this parameter do not affect already recorded logs. If  **long\_query\_time**  is changed from 1s to 0.1s, none of the previously recorded logs that do not meet the new threshold are deleted. For example, a 1.5s SQL statement that was recorded when the threshold was 1s will not be deleted now that the new threshold is 2s.


