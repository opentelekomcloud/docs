# Configuring the TDE Function<a name="rds_11_0004"></a>

Transparent Data Encryption \(TDE\) encrypts data files and backup files using certificates to implement real-time I/O encryption and decryption. This function effectively protects the security of databases and data files.

Currently, the TDE function supports single and primary/standby DB instances of the Microsoft SQL Server editions listed in  [Table 1](#table118553718299).

**Table  1**  SQL Server editions that support the TDE function

<a name="table118553718299"></a>
<table><thead align="left"><tr id="row685657172920"><th class="cellrowborder" valign="top" width="45.910000000000004%" id="mcps1.2.3.1.1"><p id="p1585711713299"><a name="p1585711713299"></a><a name="p1585711713299"></a>DB Instance Type</p>
</th>
<th class="cellrowborder" valign="top" width="54.09%" id="mcps1.2.3.1.2"><p id="p585717762915"><a name="p585717762915"></a><a name="p585717762915"></a>Editions Support for TDE</p>
</th>
</tr>
</thead>
<tbody><tr id="row198571172295"><td class="cellrowborder" valign="top" width="45.910000000000004%" headers="mcps1.2.3.1.1 "><p id="p1985767122916"><a name="p1985767122916"></a><a name="p1985767122916"></a>Primary/Standby (1/1)</p>
</td>
<td class="cellrowborder" valign="top" width="54.09%" headers="mcps1.2.3.1.2 "><a name="ul3985531133010"></a><a name="ul3985531133010"></a>
<p id="p45586354112"><a name="p45586354112"></a><a name="p45586354112"></a>2016 EE</p>
</td>
</tr>
<tr id="row58571479298"><td class="cellrowborder" valign="top" width="45.910000000000004%" headers="mcps1.2.3.1.1 "><p id="p1985718710299"><a name="p1985718710299"></a><a name="p1985718710299"></a>Single DB instances</p>
</td>
<td class="cellrowborder" valign="top" width="54.09%" headers="mcps1.2.3.1.2 "><p id="p636817296104"><a name="p636817296104"></a><a name="p636817296104"></a>2016 EE</p>
</td>
</tr>
</tbody>
</table>

## Constraints<a name="section795253052715"></a>

1.  If TDE has been enabled for a single DB instance, the instance cannot be changed to primary/standby DB instances.
2.  RDS for SQL Server currently does not support TDE certificate download. To restore data offline using the encrypted .bak file, perform the following operations:
    1.  Disable TDE for the database. For details, see  [Configuring Database-Level TDE](#section17914116134615).
    2.  Create a manual backup for the database.
    3.  Restore data from the manual backup.
    4.  Enable TDE for the database as required.

3.  Enabling TDE improves data security but affects read and write performance of encrypted databases. Exercise caution when enabling TDE.
4.  To migrate on-premises encrypted databases to RDS SQL Server DB instances, you need to disable database-level TDE first.
5.  DB instances with the instance-level TDE function enabled cannot be restored from backups to existing DB instances.
6.  When enabling the instance-level TDE function or using the stored procedure rds\_tde to enable or disable database-level TDE, do not perform the following operations:
    -   Delete files from file groups in databases.
    -   Delete databases.
    -   Take databases offline
    -   Split databases.
    -   Convert databases or file groups to the READ ONLY state.
    -   Run the ALTER DATABASE command.
    -   Create backups.
    -   Start backup for databases or database files.
    -   Start restoration for databases or database files.


## Enabling Instance-Level TDE<a name="section1740671110297"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, click the target DB instance.
5.  In the  **DB Information**  area, click  ![](figures/public.png)  in the  **TDE**  field to enable TDE.

## Configuring Database-Level TDE<a name="section17914116134615"></a>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>Before enabling the database-level TDE function, ensure that the instance-level TDE function has been enabled.  

1.  Connect to the target DB instance.
2.  Use the stored procedure rds\_tde to enable, disable, or query the database-level TDE status.

    **exec master.dbo.rds\_tde** _DatabaseName_,_TDE\_Action_

    -   **_DatabaseName_**: indicates the target database name, which can be  **null**.
    -   _TDE\_Action_:
        -   The value  **-1**  indicates that the database encryption status is queried.

            If  **_DatabaseName_**  is  **null**, the encryption status of all databases is returned.

        -   The value  **0**  indicates that the TDE function is disabled.
        -   The value  **1**  indicates that the TDE function is enabled.

    1.  Enable TDE for database db1.

        **exec master.dbo.rds\_tde db1, 1**

        **Figure  1**  Enabling TDE<a name="fig153869240383"></a>  
        ![](figures/enabling-tde.png "enabling-tde")

    2.  Disable TDE for database db1.

        **exec master.dbo.rds\_tde db1, 0**

        **Figure  2**  Disabling TDE<a name="fig192748201439"></a>  
        ![](figures/disabling-tde.png "disabling-tde")

    3.  Query the TDE status of database db1.

        **exec master.dbo.rds\_tde db1, -1**

        **Figure  3**  Querying the TDE status \(Enabled\)<a name="fig54779334418"></a>  
        ![](figures/querying-the-tde-status-(enabled).png "querying-the-tde-status-(enabled)")

        **Figure  4**  Querying the TDE status \(Disabled\)<a name="fig179000914615"></a>  
        ![](figures/querying-the-tde-status-(disabled).png "querying-the-tde-status-(disabled)")

    4.  Query the TDE status of all databases.

        **exec master.dbo.rds\_tde null, -1**

        **Figure  5**  Querying the TDE status of all databases<a name="fig16951152134915"></a>  
        ![](figures/querying-the-tde-status-of-all-databases.png "querying-the-tde-status-of-all-databases")



