# Using the Client on a Cluster Node<a name="EN-US_TOPIC_0125375262"></a>

## Scenario<a name="section65278330165558"></a>

After the client is updated, users can use the client on a Master node or a Core node in the cluster.

## Prerequisites<a name="section4933742165723"></a>

The client has been updated on the active management node.

## Procedure<a name="section51771356165739"></a>

-   Using the client on a Master node:
    1.  On the active management node where the client is updated, that is, a Master node, run the  **sudo su - omm**  command to switch the user. Run the following command to go to the client directory:

        **cd /opt/client**

    2.  Run the following command to configure the environment variable:

        **source bigdata\_env**

    3.  If the Kerberos authentication is enabled for the current cluster, run the following command to authenticate users. If the Kerberos authentication is disabled for the current cluster, skip this step.

        **kinit** **_MRS cluster user_**

        For example,  **kinit admin**.

    4.  Run a component client command.

        For example, run  **hdfs dfs -ls /**  to view files in the HDFS root directory.


-   Using the client on a Core node
    1.  Update the client on the active management node.
    2.  Locate the active management node based on the IP address and log in to the active management node as user  **linux**  using VNC. For details, see [Logging In to an ECS Using VNC](logging-in-to-an-ecs-using-vnc.md).
    3.  On the active management node, run the following command to switch the user:

        **sudo su - omm**

    4.  On the MRS management console, view  **IP Address** in the **Node**  page of the specified cluster.

        Record the IP address of the Core node on which the client is to be used.

    5.  On the active management node, run the following command to copy the package to a Core node:

        **scp -p /tmp/MRS-client/MRS\_Services\_Client.tar** _IP address of the Core node_**:///opt/client**

    6.  Log in to the Core node as user  **linux**. For details, see [Logging In to an ECS Using VNC](logging-in-to-an-ecs-using-vnc.md).

        The Master node supports Cloud-init. The preset username for Cloud-init is  **linux**. The password is randomly generated and is displayed on the VNC login page by default. If you have changed the password, log in to the node using the new password.

    7.  On the Core node, run the following command to switch the user:

        **sudo su - omm**

    8.  Run the following command to update the client configuration:

        **sh /opt/client/refreshConfig.sh** _Client installation directory_ _Full path of the client configuration file package_

        For example:

        **sh /opt/client/refreshConfig.sh /opt/client /opt/client/MRS\_Services\_Client.tar**

    9.  Run the following commands to go to the client directory and configure the environment variable:

        **cd /opt/client**

        **source bigdata\_env**

    10. If the Kerberos authentication is enabled for the current cluster, run the following command to authenticate users. If the Kerberos authentication is disabled for the current cluster, skip this step.

        **kinit** **_MRS cluster user_**

        For example,  **kinit admin**.

    11. Run a component client command.

        For example, run  **hdfs dfs -ls /**  to view files in the HDFS root directory.



