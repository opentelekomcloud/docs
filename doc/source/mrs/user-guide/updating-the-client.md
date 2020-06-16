# Updating the Client<a name="EN-US_TOPIC_0125375601"></a>

## Scenario<a name="section3898197016294"></a>

An MRS cluster provides a client for users to connect to servers, query task results, and manage data. Before using the MRS client or modifying service configuration parameters and restarting the services on MRS Manager, users must prepare the client configuration file and update the client.

During cluster creation, the original client is installed and saved in the  **/opt/client**  directory on all nodes in the cluster by default. After the cluster is created, only the client on Master nodes can be used directly, and the client on Core nodes must be updated before being used.

## Procedure<a name="section27505902163727"></a>

****Method 1: applicable to all versions****

1.  Log in to MRS Manager.
2.  Click  **Service**, and click **Download Client**.

    Set  **Client Type** to **Only configuration files**, set **Download Path** to **Server**, and click **OK** to generate the client configuration file. The generated file is saved in the **/tmp/MRS-client**  directory on the active management node by default. You can modify the file save path as required.

3.  On the MRS management console, click  **Active Clusters**.
4.  In the cluster list, click the specified cluster name and view the  **Active Master Node IP Address**.

    **Active Master Node IP Address**  is the IP address of the active Master node in a cluster, which is also the IP address of the active management node of MRS Manager.

5.  Locate the active management node based on the IP address and log in to the active management node as user  **linux**  using VNC. For details, see [Logging In to an ECS Using VNC](logging-in-to-an-ecs-using-vnc.md).

    The Master node supports Cloud-init. The preset username for Cloud-init is  **linux**. The password is randomly generated and is displayed on the VNC login page by default. If you have changed the password, log in to the node using the new password.

6.  Run the following command to switch the user:

    **sudo su - omm**

7.  Run the following command to go to the client directory:

    **cd /opt/client**

8.  Run the following command to update the client configuration:

    **sh refreshConfig.sh** _Client installation directory_ _Full path of the client configuration file package_

    For example:

    **sh refreshConfig.sh /opt/client /tmp/MRS-client/MRS\_Services\_Client.tar**

    If the following information is displayed, the configuration is updated successfully.

    ```
    ReFresh components client config is complete.
    Succeed to refresh components client config.
    ```


****Method 2: applicable to MRS 1.9.2 or later****

1.  After the cluster is installed, run the following command to switch to user  **omm**. If the client is used outside the cluster, switch to user  **root**.

    **sudo su - omm**

2.  Run the following command to go to the client directory:

    **cd /opt/client**

3.  Run the following command and enter the MRS Manager username and password with the download permission \(for example, the username is  **admin**  and the password is the one set during cluster creation\) as prompted to update client configurations.

    **sh autoRefreshConfig.sh**

4.  After the command is executed, the following information is displayed, where  _XXX_  indicates the name of the component installed in the cluster. To update client configurations of all components, press  **Enter**. To update client configurations of some components, enter the component names and separate them with commas\(,\).

    ```
    Components "xxx" have been installed in the cluster. Please input the comma-separated names of the components for which you want to update client configurations. If you press Enter without inputting any component name, the client configurations of all components will be updated:
    ```

    If the following information is displayed, The client configurations are updated successfully.

    ```
    Succeed to refresh components client config.
    ```

    If the following information is displayed, the username or password is incorrect.

    ```
    login manager failed,Incorrect username or password.
    ```

    >![](/images/icon-note.gif) **NOTE:**   
    >-   This script automatically connects to the cluster and invokes the  **refreshConfig.sh**  script to download and update the client configuration file.  
    >-   By default, the client uses the floating IP address specified by  **wsom=xxx**  in the  **Version**  file in the installation directory to update the client configurations. To update the configuration file of another cluster, modify the value of  **wsom=xxx**  in the  **Version**  file to the floating IP address of the corresponding cluster before performing this step.  


