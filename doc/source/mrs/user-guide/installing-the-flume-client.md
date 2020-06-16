# Installing the Flume Client<a name="EN-US_TOPIC_0125375557"></a>

## Scenario<a name="se08949c2aa6e4c74bb2a14c82b37577e"></a>

To use Flume to collect logs, you must install the Flume client on the log host. You can create an ECS to install the client.

## Prerequisites<a name="s5344a5c5dbc24880895ac257e15a3950"></a>

-   A streaming cluster with the Flume component has been created.
-   The log host is in the same VPC and subnet with the cluster. For details, see  [Using the Client on Another Node of a VPC](using-the-client-on-another-node-of-a-vpc.md).
-   You have obtained the username and password for logging in to the log host.

## **Procedure**<a name="sd582e6dfd7344c68a8b8b92b651829a8"></a>

1.  Create an ECS that meets the requirements in the prerequisites.
2.  Log in to MRS Manager. Choose  **Service**  \>  **Flume**  \>  **Download Client**.
    1.  In  **Client Type**, select **All client files**.
    2.  In  **Download Path**, select **Remote host**.
    3.  Set  **Host IP Address** to the IP address of the ECS, set **Host Port** to **22**, and set **Save Path** to **/home/linux**.
        -   If the default port  **22** for logging in to an ECS using SSH has been changed, set **Host Port**  to the new port.
        -   **Save Path**  contains a maximum of 256 characters.

    4.  Set  **Login User** to **linux**.

        If other users are used, ensure that they have read, write, and execute permission on the save path.

    5.  In  **SSH Private Key**, select and upload the private key used for creating the ECS.
    6.  Click  **OK**  to start downloading the client to the ECS.

        If the following information is displayed, the client package is successfully saved.

        ```
        Client files downloaded to the remote host successfully.
        ```

3.  Click  **Instance**. Query the **Business IP Address**  of any Flume instance and any two MonitorServer instances.
4.  Log in to the ECS using VNC. See "Logging In to a Linux ECS Using VNC" in the  _Elastic Cloud Server User Guide_ \(**Getting Started \> Logging In to an ECS \> Logging In to a Linux ECS Using VNC**\).

    All standard \(Standard\_xxx\) and enterprise \(Enterprise\_xxx\) images support Cloud-Init. The preset username for Cloud-Init is  **linux**. The password is randomly generated and is displayed on the VNC login page by default. If you have changed the password, log in to the ECS using the new password. See "How Do I Log In to an ECS Once All Images Support Cloud-Init?" in the _Elastic Cloud Server User Guide_ \(**FAQs \> Login FAQs \> How Do I Log In to an ECS Once All Images Support Cloud-Init?**\). It is recommended that you change the password upon the first login.

5.  On the ECS, switch to user  **root** and copy the installation package to the **/opt**  directory.

    **sudo su - root**

    **cp /home/linux/MRS\_Flume\_Client.tar /opt**

6.  Run the following command in the  **/opt**  directory to decompress the package and obtain the verification file and the configuration package of the client:

    **tar -xvf MRS\_Flume\_Client.tar**

7.  Run the following command to verify the configuration package of the client:

    **sha256sum -c MRS\_Flume\_ClientConfig.tar.sha256**

    The command output is as follows:

    ```
    MRS_Flume_ClientConfig.tar: OK
    ```

8.  Run the following command to decompress  **MRS\_Flume\_ClientConfig.tar**:

    **tar -xvf MRS\_Flume\_ClientConfig.tar**

9.  Run the following command to install the client running environment to a new directory, for example,  **/opt/Flumeenv**. The directory is automatically generated during installation.

    **sh /opt/MRS\_Flume\_ClientConfig/install.sh /opt/Flumeenv**

    If the following information is displayed, the client running environment is successfully installed:

    ```
    Components client installation is complete.
    ```

10. Run the following command to configure the environment variable:

    **source /opt/Flumeenv/bigdata\_env**

11. Run the following commands to decompress the Flume client package:

    **cd /opt/MRS\_Flume\_ClientConfig/Flume**

    **tar -xvf FusionInsight-Flume-1.6.0.tar.gz**

12. Run the following command to check whether the password of the current user has expired:

    **chage -l root**

    If the value of  **Password expires** is earlier than the current time, the password has expired. Run the **chage -M -1 root**  command to validate the password.

13. Run the following command to install the Flume client to a new directory, for example,  **/opt/FlumeClient**. The directory is automatically generated during installation.

    **sh /opt/MRS\_Flume\_ClientConfig/Flume/install.sh -d /opt/FlumeClient -f** _Service IP addresses of the MonitorServer instances_ **-c** _Path of the Flume configuration file_ **-l /var/log/ -e** _Service IP address of Flume_ **-n** _Name of the Flume client_

    The parameters are described as follows:

    -   **-d**: indicates the installation path of the Flume client.
    -   **-f**: \(optional\) indicates the service IP addresses of the two MonitorServer instances, separated by a comma. If the IP addresses are not configured, the Flume client will not send alarm information to MonitorServer, and the client information will not be displayed on MRS Manager.
    -   **-c**: \(optional\) indicates the **properties.properties** configuration file that the Flume client loads after installation. If this parameter is not specified, the **fusioninsight-flume-1.6.0/conf/properties.properties** file in the client installation directory is used by default. The configuration file of the client is empty. You can modify **properties.properties**  as required and the Flume client will load it automatically.
    -   **-l**: \(optional\) indicates the log directory. The default value is **/var/log/Bigdata**.
    -   **-e**: \(optional\) indicates the service IP address of the Flume instance. It is used to receive the monitoring indicators reported by the client.
    -   **-n**: \(optional\) indicates the name of the Flume client.
    -   IBM JDK does not support  **-Xloggc**. You must change **-Xloggc** to **-Xverbosegclog** in **flume/conf/flume-env.sh**. For 32-bit JDK, the value of **-Xmx**  must not exceed 3.25 GB.
    -   In  **flume/conf/flume-env.sh**, the default value of **-Xmx**  is 4 GB. If the client memory is too small, you can change it to 512 MB or even 1 GB.

    For example, run  **sh install.sh -d /opt/FlumeClient**.

    If the following information is displayed, the client is successfully installed:

    ```
    install flume client successfully.
    ```


