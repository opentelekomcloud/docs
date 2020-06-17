# What Inappropriate Parameter Settings Cause Unavailability of the PostgreSQL Database?<a name="rds_faq_0031"></a>

In the following cases, inappropriate parameter settings cause unavailability of the database:

-   Parameter value ranges are related to DB instance specifications.

    The maximum values of  **shared\_buffers**  and  **max\_connections**  are related to the DB instance physical memory. If you set the parameters inappropriately, the database is unavailable.

-   Parameter association is incorrect.
    -   If  **log\_parser\_stats**,  **log\_planner\_stats**, or  **log\_executor\_stats**  is enabled, you must disable  **log\_statement\_stats**. Otherwise, the database is unavailable.
    -   **max\_connections**,  **autovacuum\_max\_workers**, and  **max\_worker\_processes**  must meet the following requirements. Otherwise, the database is unavailable.

        **max\_connections**  value +  **autovacuum\_max\_workers**  value +  **max\_worker\_processes**  value + 1 < 8388607



>![](/images/icon-note.gif) **NOTE:**   
>For details on parameter descriptions, visit the  [PostgreSQL official website](https://www.postgresql.org/docs/current/static/runtime-config.html).  

Solution:

1.  Log in to the RDS console and query the logs to locate the incorrectly configured parameter.
2.  On the  **Configuration**  page, change parameters to default values and reboot the database.
3.  Set the incorrectly configured parameter to a correct value and other parameters to the original values.

