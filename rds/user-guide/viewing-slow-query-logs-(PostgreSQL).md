# Viewing Slow Query Logs<a name="slow_query_log-pg"></a>

## **Scenarios**<a name="section61232893165332"></a>

Slow query logs record statements that exceed the  **log\_min\_duration\_statement**  value. You can view log details to identify statements that are slowly executed and optimize the statements. 

RDS supports the following statement types:

-   SELECT
-   INSERT
-   UPDATE
-   DELETE
-   CREATE
-   DROP
-   ALTER
-   DO
-   CALL
-   COPY

## Parameter Description<a name="section121471583582"></a>

**Table  1**  Parameters related to PostgreSQL slow queries

<a name="table1455312241604"></a>
<table><thead align="left"><tr id="row1755318241201"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.3.1.1"><p id="p455311242020"><a name="p455311242020"></a><a name="p455311242020"></a><strong id="b842352706181819"><a name="b842352706181819"></a><a name="b842352706181819"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.2.3.1.2"><p id="p15534249012"><a name="p15534249012"></a><a name="p15534249012"></a><strong id="b14271343152219"><a name="b14271343152219"></a><a name="b14271343152219"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row145532241400"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p26741582414"><a name="p26741582414"></a><a name="p26741582414"></a>log_min_duration_statement</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p13674185817412"><a name="p13674185817412"></a><a name="p13674185817412"></a>Specifies the minimum execution time. The statements whose execution time is greater than or equal to the value of this parameter are recorded. </p>
</td>
</tr>
</tbody>
</table>

## Viewing Log Details<a name="section467223910567"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, click the target DB instance.
5.  In the navigation pane on the left, choose  **Logs**. On the  **Slow Query Logs**  page, view details about slow query logs.
    -   You can view the slow query log records of a specified execution statement type or a specific time period.
    -   The  **log\_min\_duration\_statement**  parameter determines when a slow query log is recorded. However, changes to this parameter do not affect already recorded logs. If  **log\_min\_duration\_statement**  is changed from 1s to 0.1s, none of the previously recorded logs that do not meet the new threshold are deleted. For example, a 1.5s SQL statement that was recorded when the threshold was 1s will not be deleted now that the new threshold is 2s.


