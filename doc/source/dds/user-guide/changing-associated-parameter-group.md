# Changing Associated Parameter Group<a name="dds_03_0014"></a>

## **Scenarios**<a name="section44721983185853"></a>

After a DB instance is created, you can change the parameter group associated with the DB instance to achieve optimal performance. The parameter group associated with the DB instance cannot be changed in any of the following cases:

-   A DB instance is being restarted.
-   A backup file is being created.
-   Cluster instance nodes are being added.
-   The storage space is being expanded.
-   The instance class is being changed.
-   An SSL connection is being enabled or disabled.
-   The port is being changed.

## Cluster<a name="en-us_topic_0055918187_section58363492163438"></a>

1.  [Log in to the DDS console.](logging-in-to-the-dds-console.md)
2.  On the  **Instance Management**  page, click the target cluster instance.
3.  In the  **Node Information**  area on the  **Basic Information**  page, click  **mongos**,  **shard**, or  **config**, locate the target node, and click  **Change Parameter Group**.
4.  On the displayed dialog box, select the parameter group to be modified and click  **OK**. 
    -   If the static parameter value is changed in the new parameter group, restart the instance for the modification to take effect.
    -   If no parameter groups are available for  **New Parameter Group**, create a parameter group. For details, see section  [Creating a Parameter Group](creating-a-parameter-group.md).


## Replica Set<a name="section8401914192859"></a>

1.  [Log in to the DDS console.](logging-in-to-the-dds-console.md)
2.  On the  **Instance Management**  page, locate the target replica set instance, and choose  **More**  \>  **Change Parameter Group**  in the  **Operation**  column.
3.  On the displayed dialog box, select the parameter group to be modified and click  **OK**.
    -   If the static parameter value is changed in the new parameter group, restart the instance for the modification to take effect.
    -   If no parameter groups are available for  **New Parameter Group**, create a parameter group. For details, see section  [Creating a Parameter Group](creating-a-parameter-group.md).


