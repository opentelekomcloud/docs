# Step 1: Starting Preparations<a name="dws_01_0088"></a>

This guide is an introductory tutorial that demonstrates how to create a sample data warehouse cluster, connect to the cluster's database, and analyze the sample data. You can use this tutorial to evaluate DWS.

Before creating a data warehouse cluster, ensure that the following prerequisites are met:

-   [Registering and Authenticating a Public Cloud Account Using Your Real Name](#section269013516364)
-   [Determining the Cluster Ports](#section788591414617)

## Registering and Authenticating a Public Cloud Account Using Your Real Name<a name="section269013516364"></a>

If you do not have a public cloud account, register one. If you have an account that has passed real-name authentication, skip this step and use your existing account.

1.  Open the official public cloud website and click  **Register**  in the upper right corner. The registration page is displayed.
2.  Fill in user information as instructed to complete the registration.
3.  Click the username in the upper right corner to enter the  **Account Info**  page. Then click  **Real-Name Authentication**  in the left navigation pane.
4.  Perform real-name authentication as prompted.

    >![](/images/icon-note.gif) **NOTE:**   
    >You must perform real-name authentication before enabling cloud services.  


## Determining the Cluster Ports<a name="section788591414617"></a>

-   When creating a data warehouse cluster, you need to specify a port for SQL clients or applications to access the cluster.
-   If your client is behind a firewall, you need an available port so that you can connect to the cluster and perform query and analysis from the SQL client tool.
-   If you do not know an available port, contact the network administrator to specify an open port on your firewall. The ports supported by DWS range from 8000 to 10000.
-   After the cluster is created, its port number cannot be changed. Ensure that the port specified during cluster creation is available.

