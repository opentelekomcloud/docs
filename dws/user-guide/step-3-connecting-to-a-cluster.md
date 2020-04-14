# Step 3: Connecting to a Cluster<a name="dws_01_0014"></a>

## Scenario<a name="section6082040915224"></a>

This section describes how to connect to a database through a database client after you have created a data warehouse cluster. You can refer to the following guidance to use the gsql client tool provided by DWS to connect to the database in a cluster.

1.  [Preparing an ECS](#section628535692314): The gsql client of DWS remotely connects to the database in a data warehouse cluster on an ECS.

    In this example, the gsql client provided by DWS is used to access the cluster through the public network address. If you already have a qualified ECS, skip this step.

2.  [Obtaining the Public Network Address of the Cluster](#section55665470121753): The DWS client connects to the database through the public network address.
3.  [Using the ECS to Connect to a Cluster](#section99729517811): Users can log in to the ECS, download and configure the DWS client, and connect to the database in the cluster.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>You can also use other open-source PostgreSQL clients, such as pgAdmin, to connect to the databases and perform database operations. For details, see section  [Using pgAdmin to Connect to a Cluster](using-pgadmin-to-connect-to-a-cluster.md).  

## Prerequisites<a name="section5781841515252"></a>

-   You have obtained the database administrator password of the cluster. The database administrator password has been set in  [Step 2: Creating a Cluster](step-2-creating-a-cluster.md).

-   You have obtained the port number, AZ, VPC, and security group of the created cluster. For details, see section  [Step 2: Creating a Cluster](step-2-creating-a-cluster.md).

## Preparing an ECS<a name="section628535692314"></a>

For details about how to create an ECS, see section  **Getting Started \> Logging In to an ECS**  in the  _Elastic Cloud Server User Guide_.

The ECS must meet the following requirements:

-   The ECS and data warehouse cluster must belong to the same region and AZ.
-   If you use the gsql client provided by DWS to connect to the data warehouse cluster, the ECS image must meet the following requirements:

    There is no special requirement for the image's specifications. The image's OS must be one of the following Linux OSs supported by the gsql client:

    -   The  **RedHat x64**  client can be used on the following OSs:
        -   RHEL 6.4/6.5/6.6/6.7/7.1/7.2
        -   CentOS 6.4/6.5/6.6/6.7
        -   EulerOS 2.0 SP2

    -   The  **SUSE x64**  client can be used on the following OSs:

        SLES11 SP1/SP2/SP3/SP4


-   If the client accesses the cluster using the private network address, ensure that the created ECS is in the same VPC as the data warehouse cluster.

    For details about VPC operations, see section  **VPC and Subnet**  in the  _Virtual Private Cloud User Guide_.

-   If the client accesses the cluster using the public network address, ensure that both created ECS and the data warehouse cluster have an EIP.

    When creating an ECS, you need to set  **EIP**  to  **Automatically assign**  to bind to the EIP.

    For details about how to bind to an EIP, see section  **Elastic IP Address**  in the  _Virtual Private Cloud User Guide_.

-   The security group rules of the ECS must enable communication between the ECS and the port that the data warehouse cluster uses to provide services.

    For details about security group operations, see  **Security**  \>  **Security Group**  in the  _Virtual Private Cloud User Guide_.

    Ensure that the security group of the ECS contains rules meeting the following requirements. If the rules do not exist, add them to the security group:

    -   **Transfer Direction**:  **Outbound**
    -   **Protocol/Application**: The value must contain  **TCP**, for example,  **TCP**  and  **All**.
    -   **Port Range**: The value must contain the database port that provides services in the data warehouse cluster. For example, set this parameter to  **1-65535**  or a specific DWS database port.
    -   **Destination:**  The IP address set here must contain the IP address of the cluster to be connected. For example, set this parameter to  **0.0.0.0/0**  or the specific connection address of the data warehouse cluster.

-   The security group rules of the data warehouse cluster must ensure that DWS can receive network access requests from clients.

    Ensure that the cluster's security group contains rules meeting the following requirements. If the rules do not exist, add them to the security group:

    -   **Transfer Direction**:  **Inbound**
    -   **Protocol/Application**: The value must contain  **TCP**, for example,  **TCP**  and  **All**.
    -   **Port Range**: Set this parameter to the database port that provides services in the data warehouse cluster, for example,  **8000**.
    -   **Source**: The IP address set here must contain the IP address of the DWS client host, for example,  **192.168.0.10/32**.


## Obtaining the Public Network Address of the Cluster<a name="section55665470121753"></a>

1.  Log in to the management console at  [https://console.otc.t-systems.com/dws/](https://console.otc.t-systems.com/dws/).
2.  In the navigation tree on the left, click  **Cluster Management**.
3.  In the cluster list, select a created cluster \(for example,  **dws-demo**\) click  ![](figures/en-us_image_0169938471.png)  next to  **Cluster Name**  to obtain the public network address. Save this information.

    The public network address will be used to connect to the database in the cluster in  [6](#li41463031113158).

    **Figure  1**  Cluster management<a name="fig15421040194519"></a>  
    ![](figures/cluster-management.png "cluster-management")


## Using the ECS to Connect to a Cluster<a name="section99729517811"></a>

1.  Remotely log in to an ECS using SSH.

    For details about more login methods, see section  **Getting Started \> Logging In to an ECS**  in the  _Elastic Cloud Server User Guide_.

2.  In the ECS Linux command window, run the following commands to create a  **dws**  directory and switch to the directory:

    **mkdir dws**

    **cd dws**

3.  In the ECS Linux command window, run the Wget tool to download the DWS client.

    **wget https://obs.otc.t-systems.com/dws/download/dws\_client\_redhat\_x64.tar.gz --no-check-certificate**

    The client contains database connection tool gsql and the script for testing the sample data.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >You can also log in to the DWS management console to download the DWS client. For details, see section  [Downloading the Client](downloading-the-client.md).  

4.  In the ECS Linux command window, run the following command to decompress the DWS client:

    ****tar -xvf dws\_client\_redhat\_x64.tar.gz****

5.  In the ECS Linux command window, run the following command to configure the DWS client:

    ****source gsql\_env.sh****

    If the following information is displayed, the DWS client is successfully configured:

    ```
    All things done.
    ```

6.  <a name="li41463031113158"></a>In the ECS Linux command window, run the following command to use the gsql tool to connect to the database in the data warehouse cluster:

    **gsql -d** _<Database name\>_ **-h** _<Public network address of the cluster\>_ **-U** _<Administrator\>_ **-p** _<Data warehouse port number\>_  -r

    -   **Database name**  indicates the default database  **postgres**  created during cluster creation.
    -   **Administrator**  and  **Data warehouse port number**  indicate those you set in  [Step 2: Creating a Cluster](step-2-creating-a-cluster.md).
    -   Obtain  **Public network address of the cluster**  according to  [Obtaining the Public Network Address of the Cluster](#section55665470121753).

    Run the following command to connect to the  **postgres**  database in the data warehouse cluster:

    ****gsql -d postgres -h 10.168.0.74 -U dbadmin -p 8000 -r****

    If the following information is displayed after you enter the password as prompted, the connection is successful:

    ```
    postgres=>
    ```

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >The gsql client can also connect to a cluster in SSL mode. The SSL connection mode has higher security than the common mode. You are advised to enable SSL connection \(enabled by default\) in the cluster and connect the client to the cluster in SSL mode. For details, see section  [Using the gsql Client to Connect to a Cluster](using-the-gsql-client-to-connect-to-a-cluster.md).  


