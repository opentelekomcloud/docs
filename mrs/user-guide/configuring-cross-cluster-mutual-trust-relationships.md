# Configuring Cross-Cluster Mutual Trust Relationships<a name="EN-US_TOPIC_0125375308"></a>

## Scenario<a name="s342ffd1d64e446b9ab080f7ea9da2d11"></a>

If two clusters, both with Kerberos authentication enabled, need to access the resources of each other, the administrator must configure the mutual trust relationships between the clusters.

If no trust relationship is configured, resources of a cluster are available only for users in the cluster. MRS automatically assigns a unique  **domain name**  for each cluster to define the scope of resources for users.

## Impact on the System<a name="sdc71024fdacd4882afba57952ba1bd98"></a>

-   After cross-cluster mutual trust is configured, resources of a cluster become available for users in the other cluster. User permission in the clusters must be regularly checked based on service and security requirements.
-   After cross-cluster mutual trust is configured, the two clusters must be restarted and are unavailable during restart.
-   After cross-cluster mutual trust is configured, internal users  **krbtgt/**_Local cluster domain name_**@**_External cluster domain name_ and **krbtgt/**_External cluster domain name_**@**_Local cluster domain name_ are added to the two clusters. The internal users cannot be deleted. For MRS 1.9.2 or later, the default password of the users is **Crossrealm@123**. For versions earlier than MRS 1.9.2, the default password of the users is **Admin@123**.
-   After cross-cluster mutual trust is configured, the client must be re-installed.

## Prerequisites<a name="sb196ccdb746e4db880075dd98e9a7d0c"></a>

-   Kerberos authentication is enabled for both clusters. For example, two analysis clusters with Kerberos authentication enabled are created.
-   Both clusters are in the same VPC and subnet.

## Procedure<a name="sd8b4ac456c194267b26eeffe44bf5803"></a>

1.  <a name="ldd4a15e05fef43988ee57641d9f2f103"></a>On the MRS management console, query all security groups of the two clusters.

    Each cluster has two security groups, namely the security group of the Master node and Core node respectively.

2.  <a name="le51c96a66ee449eea981a544b7133ab4"></a>On the VPC management console, add rules for each security group.

    Set  **Protocol** to **ANY**, **Transfer Direction** to **Inbound**, and **Source** to **Security Group**. The source is the security group of the peer cluster. Two inbound rules are required.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >For a normal cluster with the Kerberos authentication disabled, perform  [1](#ldd4a15e05fef43988ee57641d9f2f103)  to  [2](#le51c96a66ee449eea981a544b7133ab4)  to configure cross-cluster mutual trust relationship. For a security cluster with the Kerberos authentication enabled, perform the following steps.  

3.  Log in to MRS Manager of the two clusters separately. Click  **Service** and check whether the **Health Status** of all components is **Good**.
    -   If yes, go to  [4](#lc95493313e064108bb1b093adf671eae).
    -   If no, contact technical support personnel for troubleshooting.

4.  <a name="lc95493313e064108bb1b093adf671eae"></a>Query configuration information.
    1.  On MRS Manager of the two clusters, choose  **Service**  \>  **KrbServer**  \>  **Instance**. Query **OM IP Address**  of the two KerberosServer hosts.
    2.  Click  **Service Configuration**. Set **Type** to **All**. Choose **KerberosServer**  \>  **Port** in the navigation tree on the left. Query the value of **kdc\_ports**. The default value is **21732**.
    3.  Click  **Realm** and query the value of **default\_realm**.

5.  <a name="l7d5a34531e174e75a23fab059c2b2735"></a>On MRS Manager of either cluster, modify the  **peer\_realms**  parameter.

    **Table  1**  Parameter description

    <a name="te5677b43705d4ee1be3d967b3d635452"></a>
    <table><thead align="left"><tr id="r2792101fc2d74df58bdbd6b482a231dc"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.3.1.1"><p id="a4f00583de27d4707bfdadaada0db8067"><a name="a4f00583de27d4707bfdadaada0db8067"></a><a name="a4f00583de27d4707bfdadaada0db8067"></a><strong id="adf55e5ec328e48f4ac1594ed23cff7f2"><a name="adf55e5ec328e48f4ac1594ed23cff7f2"></a><a name="adf55e5ec328e48f4ac1594ed23cff7f2"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="77%" id="mcps1.2.3.1.2"><p id="ad902381f60644ba19e64045ae8ded264"><a name="ad902381f60644ba19e64045ae8ded264"></a><a name="ad902381f60644ba19e64045ae8ded264"></a><strong id="a7848272b91374e2ea2f6ee2e20f7608e"><a name="a7848272b91374e2ea2f6ee2e20f7608e"></a><a name="a7848272b91374e2ea2f6ee2e20f7608e"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="rdc90644d2fa94d1da686a74fe2c6c10c"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="a086518c57f5e4916a27564868058bde5"><a name="a086518c57f5e4916a27564868058bde5"></a><a name="a086518c57f5e4916a27564868058bde5"></a>realm_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="aaf9d197bb6a540388f0693dd5df9547b"><a name="aaf9d197bb6a540388f0693dd5df9547b"></a><a name="aaf9d197bb6a540388f0693dd5df9547b"></a><span class="parmname" id="p8572231e99a847b3b9f0d8da7c58eed6"><a name="p8572231e99a847b3b9f0d8da7c58eed6"></a><a name="p8572231e99a847b3b9f0d8da7c58eed6"></a><b>default_realm</b></span> of the peer cluster</p>
    </td>
    </tr>
    <tr id="rfb4fe5a68d674f8f801dedec4c5ab48b"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="a66bfd5fd4c0848869240fe8b59c6f04c"><a name="a66bfd5fd4c0848869240fe8b59c6f04c"></a><a name="a66bfd5fd4c0848869240fe8b59c6f04c"></a>ip_port</p>
    </td>
    <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="aa1e590569c574a0591e7fc673081060a"><a name="aa1e590569c574a0591e7fc673081060a"></a><a name="aa1e590569c574a0591e7fc673081060a"></a>KDC address of the peer cluster. Format: <em id="a86dfe330bbca4e5d8d321f28c17cc511"><a name="a86dfe330bbca4e5d8d321f28c17cc511"></a><a name="a86dfe330bbca4e5d8d321f28c17cc511"></a>IP address of a KerberosServer node in the peer cluster:kdc_port</em></p>
    <p id="a474859e1cb1a476e910cc2c79c92f2eb"><a name="a474859e1cb1a476e910cc2c79c92f2eb"></a><a name="a474859e1cb1a476e910cc2c79c92f2eb"></a>The addresses of the two KerberosServer nodes are separated by a comma. For example, if the IP addresses of the KerberosServer nodes are 10.0.0.1 and 10.0.0.2 respectively, the value of this parameter is <span class="parmvalue" id="p2c294cdd14414b159ce4dd9d51d5377a"><a name="p2c294cdd14414b159ce4dd9d51d5377a"></a><a name="p2c294cdd14414b159ce4dd9d51d5377a"></a><b>10.0.0.1:21732,10.0.0.2:21732</b></span>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   To deploy trust relationships with multiple clusters, click  ![](figures/icon_mrs_addsource.jpg) to add items and specify relevant parameters. To delete an item, click ![](figures/icon_mrs_mj.jpg).  
    >-   A cluster can have trust relationships with a maximum of 16 clusters. By default, no trust relationship exists between different clusters that are trusted by a local cluster.  

6.  Click  **Save Configuration**. In the dialog box that is displayed, select **Restart the affected services or instances** and click **OK**.

    After  **Operation succeeded** is displayed, click **Finish**.

7.  <a name="l1c95f7ce1b354454a6d2b2466e692c6f"></a>Exit MRS Manager and log in to it again. If the login is successful, the configurations are valid.
8.  Log in to MRS Manager of the other cluster and repeat  [5](#l7d5a34531e174e75a23fab059c2b2735) to [7](#l1c95f7ce1b354454a6d2b2466e692c6f).

## Follow-up Operations<a name="section1738410566199"></a>

After you configure the cross-cluster mutual trust relationship, service configurations are modified and the service is restarted on MRS Manager. You need to prepare the client configuration file and update the client again.

Scenario 1:

If cluster A and cluster B \(peer cluster and mutually trusted cluster\) are the same type, for example, analysis cluster or streaming cluster, follow instructions in  [Updating the Client](updating-the-client.md)  to update the client configuration files of cluster A and cluster B.

-   Update the client configuration file of cluster A.
-   Update the client configuration file of cluster B.

Scenario 2:

If cluster A and cluster B \(peer cluster and mutually trusted cluster\) are the different type, perform the following operations to update their clients.

-   Update the client configuration file of cluster A to cluster B.
-   Update the client configuration file of cluster B to cluster A.
-   Update the client configuration file of cluster A.
-   Update the client configuration file of cluster B.

1.  Log in to MRS Manager of cluster A.
2.  <a name="li25485761174241"></a>Click  **Services** and then **Download Client**.
3.  In  **Client Type**, select **Only configuration files**.
4.  In  **Download Path**, select **Remote host**.
5.  Set  **Host IP Address** to the active Master node IP address of cluster B, **Host Port** to **22**, and **Save Path** to **/tmp**.
    -   If the default port  **22** for logging in to cluster B using SSH is changed, set **Host Port**  to a new port.
    -   The value of  **Save Path**  contains a maximum of 256 characters.

6.  Set  **Login User** to **linux**.

    If another user is used, ensure that the user has permissions to read, write, and execute the save path.

7.  In  **SSH Private Key**, select the key file that is used when cluster B is created and upload it.
8.  Click  **OK**  to generate a client file.

    If the following information is displayed, the client file is successfully saved. And then, click  **Close**.

    ```
    Client files downloaded to the remote host successfully. 
    ```

    If the following information is displayed, check the username, password, and security group configurations of the remote host. Ensure that the username and password are correct and an inbound rule of the SSH\(22\) port has been added to the security group of the remote host. And then, go to  [2](#li25485761174241)  to download the client again.

    ```
    Failed to connect to the server. Please check the network connection or parameter settings.
    ```

9.  Log in to an ECS in cluster B using VNC. For details see  **ECS Logins\> Logging In to a Windows ECS\> Remotely Logging In to a Windows ECS Using VNC** in the _Elastic Cloud Server User Guide_.

    All standard images \(Standard\__xxx_\) and enterprise images \(Enterprise\__xxx_\) support Cloud-Init. The preset username of Cloud-Init is **linux** and the password is randomly generated and displayed on the VNC login page by default. If you modify the password and use a new one, follow instructions in **FAQs \> Login FAQs \> How Do I Log In to an ECS Once All Images Support Cloud-Init?** in the _Elastic Cloud Server User Guide_  to log in to the ECS. You are advised to change the password upon the initial login.

10. Run the following command to go to the client directory.

    **cd /opt/client**

11. <a name="li1470645152711"></a>Run the following commands to update client configurations of cluster A to cluster B.

    **sh refreshConfig.sh** _Client installation directory Complete path of the client configuration file package_

    The following provides an example.

    **sh refreshConfig.sh /opt/client /tmp/MRS\_Services\_Client.tar**

    If the following information is displayed, client configurations are successfully updated.

    ```
    ReFresh components client config is complete.
    Succeed to refresh components client config.
    ```

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >You can also refer to method 2 in  [Updating the Client](updating-the-client.md)  to perform operations in  [1](#ldd4a15e05fef43988ee57641d9f2f103)  to  [11](#li1470645152711).  

12. Repeat  [1](#ldd4a15e05fef43988ee57641d9f2f103) to [11](#li1470645152711)  to update the client configuration file of cluster B to cluster A.
13. Follow instructions in  [Updating the Client](updating-the-client.md)  to perform the following operations to update the client configuration files of the local clusters.
    -   Update the client configuration file of cluster A.
    -   Update the client configuration file of cluster B.


