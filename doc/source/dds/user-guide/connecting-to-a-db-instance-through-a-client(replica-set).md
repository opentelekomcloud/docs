# Connecting to a DB Instance Through a Client<a name="en-us_topic_0105284966"></a>

## **Scenarios**<a name="en-us_topic_0085335422_section46429645141251"></a>

This section guides you on how to connect to DB instances through a database client using a common connection or an SSL connection. You are advised to use SSL to encrypt connections to ensure data security.

Based on the application scenario, you can determine whether to access a DB instance through an EIP. For details, see  [Scenarios](binding-and-unbinding-an-eip(replica-set).md#section055104935914).

You can directly perform operations on the primary and secondary nodes. Primary nodes are used for processing read and write requests. Secondary nodes replicate data from the primary and are used for processing read requests only.

This section uses the Linux OS as an example to describe how to connect to a replica set instance.

## Restrictions<a name="section135810251275"></a>

For details about restrictions on connecting to a DB instance, see  [Restrictions](restrictions(replica-set).md).

## **Prerequisites**<a name="en-us_topic_0085335422_section12950115493212"></a>

1.  An ECS or a device that can access DDS is ready for use.
    -   To connect to a  DDS DB instance  from an ECS, you need to create and log in to the ECS. For details, see  [How Can I Create and Log In to an ECS?](how-can-i-create-and-log-in-to-an-ecs.md)
    -   To connect to a  DB instance  through an EIP:
        1.  Bind an EIP to a DB instance node. For details, see section  [Binding an EIP](binding-and-unbinding-an-eip(replica-set).md#section33192668203259).
        2.  Ensure that your local device can access the EIP that has been bound to the DB instance.

2.  A MongoDB client has been installed on the prepared ECS or the device.

    For details on how to install a MongoDB client, see  [How Can I Install a MongoDB Client?](how-can-i-install-a-mongodb-client.md)


## SSL Connection<a name="section3730754113815"></a>

1.  On the  **Instance Management**  page, locate the target DB instance and click its name. On the  **Basic Information**  page, click  ![](figures/icon-download.png)  in the  **SSL**  field to download the root certificate.
2.  Upload the root certificate to the ECS that connects to the DB instance or save the root certificate to a local device that can access DDS.

    The following describes how to upload the certificate to a Linux and Window ECS:

    -   In Linux, run the following command:

        **scp** _<IDENTITY\_FILE\>_ _<REMOTE\_USER\>_**@**_<REMOTE\_ADDRESS\>_**:**_<REMOTE\_DIR\>_

        >![](/images/icon-note.gif) **NOTE:**   
        >-   **IDENTITY\_FILE**  indicates the directory where the root certificate locates. The file access permission is 600.  
        >-   **REMOTE\_USER**  indicates the ECS OS user.  
        >-   **REMOTE\_ADDRESS**  indicates the ECS address.  
        >-   **REMOTE\_DIR**  indicates the directory of the ECS to which the root certificate is uploaded.  

    -   In Windows, upload the root certificate using file transfer tools.

3.  Connect to a  DDS DB instance.

    The Linux OS is used as an example.

    **./mongo --host**  <_DB\_HOST_\>  **--port**  <_DB\_PORT_\>  **-u**  <_DB\_USER_\>  **-p** **--authenticationDatabase admin --ssl --sslCAFile**  <_FILE\_PATH_\>  **--sslAllowInvalidHostnames**

    Enter the database account password when prompted:

    ```
    Enter password:
    ```

    >![](/images/icon-note.gif) **NOTE:**   
    >-   A replica set instance uses the management IP address to generate SSL certificate.  **--sslAllowInvalidHostnames**  is needed for the SSL connection.  
    >-   **DB\_HOST**  indicates the IP address of the remotely connected DB instance. Obtain the value from the  **Private IP Address**  column in the node list in the  **Node Information**  area. If a device can access the DB instance through an EIP, set this parameter to the EIP displayed in  **EIP**  column in the node list in the  **Node Information**  area.  
    >-   **DB\_PORT**  indicates the port number. Obtain the value from  **Database Port**  in the  **Network Information**  area on the  **Basic Information**  page.  
    >-   **DB\_USER**  indicates the database account name. The default value is  **rwuser**.  
    >-   **FILE\_PATH**  indicates the path where the root certificate is stored.  

    Example:

    **./mongo --host 192.168.1.6 --port 8635 -u rwuser -p --authenticationDatabase admin --ssl --sslCAFile /tmp/ca.crt** **--sslAllowInvalidHostnames**

4.  Check the connection result. If the following information is displayed, the connection is successful.
    -   Result from connecting the primary node in a replica set:

        ```
        replica:PRIMARY>
        ```

    -   Result from connecting the secondary node in a replica set:

        ```
        replica:SECONDARY>
        ```



## Common Connection<a name="en-us_topic_0085335422_sfc3bfb212a8440799f49320d91fc096c"></a>

>![](/images/icon-notice.gif) **NOTICE:**   
>To use the common connection mode, you need to disable the SSL connection. For details, see section  [Disabling SSL](enabling-or-disabling-ssl(replica-set).md#en-us_topic_0085468614_section4225593518277).  

1.  Log in to the prepared ECS or the device that can access the document database.
2.  Connect to a  DDS DB instance.

    **./mongo --host**  <_DB\_HOST_\>  **--port**  <_DB\_PORT_\>  **-u**  <_DB\_USER_\>  **-p** **--authenticationDatabase** **admin**

    Enter the database account password when prompted:

    ```
    Enter password:
    ```

    >![](/images/icon-note.gif) **NOTE:**   
    >-   **DB\_HOST**  indicates the IP address of the remotely connected DB instance. Obtain the value from the  **Private IP Address**  column in the node list in the  **Node Information**  area. If a device can access the DB instance through an EIP, set this parameter to the EIP displayed in  **EIP**  column in the node list in the  **Node Information**  area.  
    >-   **DB\_PORT**  indicates the port number. Obtain the value from  **Database Port**  in the  **Network Information**  area on the  **Basic Information**  page.  
    >-   **DB\_USER**  indicates the database account name. The default value is  **rwuser**.  

    Example:

    **./mongo --host 192.168.1.6 --port 8635 -u rwuser -p --authenticationDatabase admin**

3.  Check the connection result. If the following information is displayed, the connection is successful.
    -   Result from connecting the primary node in a replica set:

        ```
        replica:PRIMARY>
        ```

    -   Result from connecting the secondary node in a replica set:

        ```
        replica:SECONDARY>
        ```



