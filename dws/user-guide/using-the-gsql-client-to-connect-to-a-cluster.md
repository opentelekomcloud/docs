# Using the gsql Client to Connect to a Cluster<a name="dws_01_0037"></a>

This section describes how to connect to a database through an SQL client after you create a data warehouse cluster and before you use the cluster's database. DWS provides the gsql client that matches the cluster version for you to access the cluster using the cluster's public or private network address.

## Using the gsql CLI Client to Connect to a Cluster<a name="section2664278815443"></a>

1.  Prepare a Linux ECS to install and run the gsql client.

    For details, see  [Preparing an ECS as the gsql Client Host](preparing-an-ecs-as-the-gsql-client-host.md).

2.  Download the DWS client.

    For details, see section  [Downloading the Client](downloading-the-client.md).

3.  Use WinSCP to upload the client tool to the target Linux host.

    The user who uploads the client must have the full control permission on the target directory to which the client is uploaded.

4.  \(Optional\) To connect to the cluster in SSL mode, configure SSL authentication parameters on the client. For details, see section  [Establishing Secure TCP/IP Connections in SSL Mode](establishing-secure-tcp-ip-connections-in-ssl-mode.md).

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >The SSL connection mode delivers higher security than the non-SSL mode. You are advised to use the SSL mode on the client.  

5.  Use the SSH tool to remotely log in to the host.

    For details about how to log in to an ECS, see  **ECSs \> Logging In to a Linux ECS \> Login Using an SSH Password**  in the  _Elastic Cloud Server User Guide_.

6.  Run the following commands to decompress the client:

    **cd <Path for saving the client\>**

    ****tar -xvf dws\_client\_redhat\_x64.tar.gz****

    In the preceding commands:

    -   <_Path for saving the client_\>: Replace it with the actual path.
    -   **dws\_client\_redhat\_x64.tar.gz**: In this command, the client tool package of  **RedHat x64**  is used as an example. Replace the client tool package with the actual one.

7.  Run the following command to configure the DWS client:

    **source gsql\_env.sh**

    If the following information is displayed, the DWS client is successfully configured:

    ```
    All things done.
    ```

    You can connect to a data warehouse cluster through the DWS client.

8.  Run the following command. Replace the values of each parameter with actual values. This command will use the gsql client to connect to the database in the data warehouse cluster:

    **gsql -d <Database name\> -h <Cluster address\> -U <Database user\> -p <Database port\> -r**

    The parameters are described as follows:

    -   **Database name**: Enter the name of the database to be connected. If you use the client to connect to the cluster for the first time, enter the default database  **postgres**.
    -   **Database user**: Enter the username of the cluster's database. If you use the client to connect to the cluster for the first time, set this parameter to the default administrator configured during cluster creation, for example,  **dbadmin**.
    -   **Database port**: Enter the database port set during cluster creation.
    -   **Cluster address**: For details about how to obtain this address, see section  [Obtaining the Cluster Connection Address](obtaining-the-cluster-connection-address.md). If a public network address is used for connection, set this parameter to  **Public Network Address**  or  **Public Network Domain Name**. If a private network address is used for connection, set this parameter to  **Private Network Address**  or  **Private Network Domain Name**.

    For example, run the following command to connect to the  **postgres**  default database in the data warehouse cluster:

    ****gsql -d postgres -h 10.168.0.74 -U dbadmin -p 8000 -r****

    If the following information is displayed after you enter the password as prompted, the connection is successful:

    ```
    postgres=>
    ```


## gsql Command Reference<a name="section41003216539"></a>

  

  

For more information about the gsql commands, see the .

  

