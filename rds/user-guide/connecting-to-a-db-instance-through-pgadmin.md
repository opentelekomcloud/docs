# Connecting to a DB Instance Through pgAdmin<a name="rds_pg_11_0005"></a>

You can use the  pgAdmin  client to  connect to an RDS DB instance.

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>-   The pgAdmin client only supports access through EIPs.  
>-   The pgAdmin version must be 4 or later.  

## **Preparations**<a name="section48118919135236"></a>

1.  <a name="li345439671899"></a>Prepare a device that can access RDS DB instances.

    To connect to a DB instance through an EIP, you must:

    1.  Bind the EIP to the DB instance. For details, see  [Step 3: Bind an EIP](step-3-bind-an-eip-(PostgreSQL)
.md).
    2.  Ensure that the device can access the EIP that has been bound to the DB instance.

2.  Install the pgAdmin client on the device that was prepared in  [step 1](#li345439671899).

## Procedure<a name="section161845331185"></a>

1.  Start pgAdmin.
2.  In the displayed login window, choose  **Servers**  \>  **Create**  \>  **Server**.

    **Figure  1**  Creation<a name="fig271103014223"></a>  
    ![](figures/creation.png "creation")

3.  On the  **General**  page, specify  **Name**. On the  **Connection**  page, specify information about the DB instance to be connected. Then, click  **Save**.

    **Figure  2**  General page<a name="fig12951421269"></a>  
    ![](figures/general-page.png "general-page")

    **Figure  3**  Connection page<a name="fig1037014231499"></a>  
    ![](figures/connection-page.png "connection-page")

    Parameter description:

    -   **Host name/address**: indicates the EIP of the DB instance to be connected.
    -   **Port**: indicates the database port. By default, the value is  **5432**.
    -   **User name**: indicates the username. By default, the value is  **root**.
    -   **Password**: indicates the password of the target database username.

4.  In the login window, check that the connection information is correct. The target DB instance is successfully connected.

