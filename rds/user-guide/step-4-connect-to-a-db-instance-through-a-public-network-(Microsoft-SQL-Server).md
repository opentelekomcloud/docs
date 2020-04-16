# Step 4: Connect to a DB Instance Through a Public Network<a name="rds_03_0007"></a>

You can connect to a DB instance through a common connection or an SSL connection. The  SSL connection encrypts data  and is more secure.

## **Preparations**<a name="section367520762117"></a>

1.  Install the Microsoft SQL Server client.

    For details, see section  [How Can I Install SQL Server Management Studio?](how-can-i-install-sql-server-management-studio.md)

2.  Bind an EIP to the target DB instance and configure security group rules.
    1.  <a name="li1728416257345"></a>Bind an EIP to the target DB instance.

        For details about how to bind an EIP, see section  [Step 3: Bind an EIP](step-3-bind-an-eip-(Microsoft-SQL-Server).md).

    2.  <a name="li85977812411"></a>Obtain the IP address of the local device.
    3.  Configure security group rules.

        Add the IP address and port obtained in  [2.b](#li85977812411)  to the inbound rule of the security group.

        For details about how to configure a security group rule, see section  [Step 2: Configure Security Group Rules](step-2-configure-security-group-rules-(Microsoft-SQL-Server).md).

    4.  Run the  **ping**  command to connect the EIP that has been bound to the target DB instance in  [2.a](#li1728416257345)  to check that the local device can connect to the EIP.


## Common Connection<a name="section8112152217539"></a>

1.  Start SQL Server Management Studio.
2.  Choose  **Connect**  \>  **Database Engine**. In the displayed dialog box, enter login information.

    **Figure  1**  Connecting to the server<a name="fig99151514124518"></a>  
    ![](figures/connecting-to-the-server-(Microsoft-SQL-Server).png "connecting-to-the-server-(Microsoft-SQL-Server)")

    -   **Server name**: indicates the IP address and port of the DB instance. Use a comma \(,\) to separate them. For example: x.x.x.x,8080.
        -   The IP address is the EIP that has been bound to the DB instance.
        -   The port is the database port in the  **Connection Information**  area on the  **Basic Information**  page of the DB instance.

    -   **Authentication**: indicates the authentication mode. Select  **SQL Server Authentication**.
    -   **Login**: indicates the RDS database username. The default administrator is  **rdsuser**.
    -   **Password**: indicates the password of the RDS database username.

3.  Click  **Connect**  to connect to the DB instance.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If the connection fails, ensure that preparations have been correctly made in  [Preparations](#section367520762117)  and try again.  


## SSL Connection<a name="section335618164205"></a>

1.  Download the SSL root certificate and then upload it.
    1.  In the  **DB Information**  area on the  **Basic Information**  page, click  ![](figures/down.png)  in the  **SSL**  field to download the root certificate or certificate bundle.
    2.  Upload the root certificate to the ECS to be connected to the DB instance.
    3.  Import the root certificate to the Windows OS on the ECS. For details, see section  [How Can I Import the Root Certificate to the Windows or Linux OS?](how-can-i-import-the-root-certificate-to-the-windows-or-linux-os.md)

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >-   Replace the old certificate before it expires to improve system security.  
        >-   After you bind an EIP to a Microsoft SQL Server DB instance, you must reboot the instance to make the SSL connection work.  


2.  Start SQL Server Management Studio.
3.  Choose  **Connect**  \>  **Database Engine**. In the displayed dialog box, enter login information.

    **Figure  2**  Connecting to the server<a name="fig1884118334272"></a>  
    ![](figures/connecting-to-the-server-14.png "connecting-to-the-server-(Microsoft-SQL-Server)")

    -   **Server name**: indicates the IP address and port of the DB instance. Use a comma \(,\) to separate them. For example: x.x.x.x,8080.
        -   The IP address is the EIP that has been bound to the DB instance.
        -   The port is the database port in the  **Connection Information**  area on the  **Basic Information**  page of the DB instance.

    -   **Authentication**: indicates the authentication mode. Select  **SQL Server Authentication**.
    -   **Login**: indicates the RDS database username. The default administrator is  **rdsuser**.
    -   **Password**: indicates the password of the RDS database username.

4.  On the  **Connection Properties**  page, enter related parameters and select  **Encrypt connection**  to enable SSL encryption. \(By default,  **Encrypt connection**  is not selected. You need to select it manually.\)

    **Figure  3**  Connection properties<a name="fig2077710158306"></a>  
    ![](figures/connection-properties-15.jpg "connection-properties-(Microsoft-SQL-Server)")

5.  Click  **Connect**  to connect to the DB instance.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If the connection fails, ensure that preparations have been correctly made in  [Preparations](#section367520762117)  and try again.  


