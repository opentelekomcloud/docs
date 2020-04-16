# Connecting to a DB Instance Through a Client<a name="en-us_topic_0044018334"></a>

## **Scenarios**<a name="section46429645141251"></a>

This section guides you on how to connect to DB instances through a database client using a common connection or an SSL connection. You are advised to use SSL to encrypt connections to ensure data security.

Based on the application scenario, you can determine whether to access a DB instance through an EIP. For details, see  [Scenarios](binding-and-unbinding-an-eip(cluster).md#section055104935914).

This section uses the Linux OS as an example to describe how to connect to a cluster instance.

## Restrictions<a name="section135810251275"></a>

For details about restrictions on connecting to a DB instance, see  [Restrictions](restrictions(cluster).md).

## **Prerequisites**<a name="section12950115493212"></a>

1.  An ECS or a device that can access DDS is ready for use.
    -   To connect to a  DDS DB instance  from an ECS, you need to create and log in to the ECS. For details, see  [How Can I Create and Log In to an ECS?](how-can-i-create-and-log-in-to-an-ecs.md)
    -   To connect to a  DB instance  through an EIP:
        1.  For details on how to bind an EIP, see section  [Binding an EIP](binding-and-unbinding-an-eip(cluster).md#section3199593620428).
        2.  Ensure that your local device can access the EIP that has been bound to the DB instance.

2.  A MongoDB client has been installed on the prepared ECS or the device.

    For details on how to install a MongoDB client, see section  [How Can I Install a MongoDB Client?](how-can-i-install-a-mongodb-client.md)


## SSL Connection<a name="section1640311061419"></a>

1.  On the  **Instance Management**  page, locate the target DB instance and click its name. On the  **Basic Information**  page, click  ![](figures/download.png)  in the  **SSL**  field to download the root certificate.
2.  Upload the root certificate to the ECS that connects to the DB instance or save the root certificate to a local device that can access DDS.

    The following describes how to upload the certificate to a Linux and Window ECS:

    -   In Linux, run the following command:

        **scp** _<IDENTITY\_FILE\>_ _<REMOTE\_USER\>_**@**_<REMOTE\_ADDRESS\>_**:**_<REMOTE\_DIR\>_

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >-   **IDENTITY\_FILE**  indicates the directory where the root certificate locates. The file access permission is 600.  
        >-   **REMOTE\_USER**  indicates the ECS OS user.  
        >-   **REMOTE\_ADDRESS**  indicates the ECS address.  
        >-   **REMOTE\_DIR**  indicates the directory of the ECS to which the root certificate is uploaded.  

    -   In Windows, upload the root certificate using file transfer tools.

3.  Connect to the DB instance in the directory where the MongoDB client is located.

    The Linux OS is used as an example.

    **./mongo --host**  <_DB\_HOST_\>  **--port**  <_DB\_PORT_\>  **-u**  <_DB\_USER_\>  **-p** **--authenticationDatabase admin --ssl --sslCAFile**  <_FILE\_PATH_\>

    Enter the database account password when prompted:

    ```
    Enter password:
    ```

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   A cluster instance uses the management IP address to generate SSL certificate.  **--sslAllowInvalidHostnames**  is needed for the SSL connection through an EIP.  
    >-   **DB\_HOST**  indicates the IP address of the remotely connected DB instance. Obtain the value from the  **Private IP Address**  column in the node list in the  **Node Information**  area. If a device can access the DB instance through an EIP, set this parameter to the EIP displayed in  **EIP**  column in the node list in the  **Node Information**  area.  
    >-   **DB\_PORT**  indicates the port number. Obtain the value from  **Database Port**  in the  **Network Information**  area on the  **Basic Information**  page.  
    >-   **DB\_USER**  indicates the database account name. The default value is  **rwuser**.  
    >-   **FILE\_PATH**  indicates the path where the root certificate is stored.  

    Example:

    **./mongo --host 192.168.1.6 --port 8635 -u rwuser -p --authenticationDatabase admin --ssl --sslCAFile /tmp/ca.crt**

4.  Check the connection result. If the following information is displayed, the connection is successful.

    ```
    mongos>
    ```


## Common Connection<a name="sfc3bfb212a8440799f49320d91fc096c"></a>

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>To use the common connection mode, you need to disable the SSL connection. For details, see section  [Disabling SSL](enabling-or-disabling-ssl(cluster).md#section4225593518277).  

1.  Log in to the prepared ECS or the device that can access the document database.
2.  Connect to the  DB instance  in the directory where the MongoDB client is located.

    **./mongo --host**  <_DB\_HOST_\>  **--port**  <_DB\_PORT_\>  **-u**  <_DB\_USER_\>  **-p --authenticationDatabase admin**

    Enter the database account password when prompted:

    ```
    Enter password:
    ```

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   **DB\_HOST**  indicates the IP address of the remotely connected DB instance. Obtain the value from the  **Private IP Address**  column in the node list in the  **Node Information**  area. If a device can access the DB instance through an EIP, set this parameter to the EIP displayed in  **EIP**  column in the node list in the  **Node Information**  area.  
    >-   **DB\_PORT**  indicates the port number. Obtain the value from  **Database Port**  in the  **Network Information**  area on the  **Basic Information**  page.  
    >-   **DB\_USER**  indicates the database account name. The default value is  **rwuser**.  

    Example:

    **./mongo --host 192.168.1.6 --port 8635 -u rwuser -p --authenticationDatabase admin**

3.  Check the connection result. If the following information is displayed, the connection is successful.

    ```
    mongos>
    ```


