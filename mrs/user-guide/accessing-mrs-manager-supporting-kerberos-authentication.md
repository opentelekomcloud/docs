# Accessing MRS Manager Supporting Kerberos Authentication<a name="EN-US_TOPIC_0125376119"></a>

## Scenario<a name="s20330b7ef6e5401a90794743167305b1"></a>

After users create MRS clusters that support Kerberos authentication, they can manage running clusters on MRS Manager.

This section describes how to prepare a work environment on the public cloud platform for accessing MRS Manager.

## Impact on the System<a name="sd9a66de36a9142998daa10ccb344cf83"></a>

Site trust must be added to the browser when you access MRS Manager for the first time. Otherwise, MRS Manager cannot be accessed.

## Prerequisites<a name="s7df06c0ed2af4f0fb4b8d44c294a3f8b"></a>

You have obtained the password of user  **admin**. The password of user **admin**  is specified by the user during MRS cluster creation.

## Procedure<a name="s2224b7e4354345f9a67bdc1604424e52"></a>

If the cluster version is MRS 1.9.2 or later, perform the following steps:

1.  Log in to the MRS management console.
2.  In the navigation pane, choose  **Clusters** \> **Active Clusters**. Click the target cluster name to access the cluster details page.
3.  Click  **View**. The **Access MRS Manager**  page is displayed.
    1.  Select an available EIP from the drop-down list or click  **Manage EIP**  to purchase one.
    2.  Add a security group rule. By default, the user's public IP address used for accessing port 9022 is filled in the rule. If you want to add multiple IP address segments to a trusted range for accessing MRS Manager, refer to  [6](#en-us_topic_0125376155_li1049410469610)  to  [9](#en-us_topic_0125376155_li035723593115). If you want to view, modify, or delete a security group rule, click  **Manage Security Group Rule**.

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >-   It is normal that the automatically generated public IP address is different from the local IP address and no action is required.  
        >-   If port 9022 is a Knox port, you need to enable the permission of port 9022 to access Knox for accessing MRS Manager.  

    3.  Select the checkbox indicating that "**I** **confirm that xx.xx.xx.xx is a trusted public IP address and MRS Manager can be accessed using this IP address**."

4.  Click  **OK**. The MRS Manager login page is displayed.
5.  Enter the default username  **admin** and password you set when creating the cluster, and click **Log In**. The  **MRS Manager**  page is displayed.
6.  <a name="en-us_topic_0125376155_li1049410469610"></a>On the MRS management console, click  **Active Clusters**  and click the target cluster name to access the cluster details page.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >To assign MRS Manager access permissions to other users, perform  [6](#en-us_topic_0125376155_li1049410469610)  to  [9](#en-us_topic_0125376155_li035723593115)  to add the users' public IP addresses to a trusted range.  

7.  Click  **Add Security Group Rule**  behind the EIP.
8.  On the  **Add Security Group Rule**  page, enter a public IP address range to open the access permissions and select the checkbox indicating that "**I confirm that the authorized object is a trusted public IP address range. Do not use 0.0.0.0/0. Otherwise, security risks may arise**.".

    By default, your public IP address is filled in the rule. If you want to change the IP address segment, for example, add multiple IP address segments to a trusted range, repeat  [6](#en-us_topic_0125376155_li1049410469610)  to  [9](#en-us_topic_0125376155_li035723593115). If you want to view, modify, or delete a security group rule, click  **Manage Security Group Rule**.

9.  <a name="en-us_topic_0125376155_li035723593115"></a>Click  **OK**  to add the security group rule.

If the cluster version is earlier than MRS 1.9.2, perform the following steps:

1.  On the MRS management console, click  **Clusters**.
2.  In the  **Active Clusters**  list, click the specified cluster name.

    Record  **AZ**, **VPC**, and **Floating IP Address** of the cluster, and **Default Security Group**  of the Master node.

3.  On the ECS management console, create a new ECS.

    -   Ensure that  **AZ**, **VPC**, and **Security Group**  of the ECS are the same as those of the cluster to be accessed.
    -   Select a Windows public image. For example, select the  **Enterprise\_Windows\_STD\_2012R2\_20170316-0\(80GB\)**  enterprise image.
    -   For details about other parameter configurations, see  **Elastic Cloud Server User Guide**  \>  **Getting Started**  \>  **Creating an ECS**.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If the security group of the ECS is different from  **Default Security Group**  of the Master node, you can modify the configuration using either of the following methods:  
    >-   Change the security group of the ECS to the default security group of the Master node. For details, see  **Changing the Security Group** in **Elastic Cloud Server User Guide**  \>  **Management**  \>  **Modifying ECS Specifications**.  
    >-   Add two security group rules to the security groups of the Master node and Core node to ensure that the ECS can access the cluster and set the protocol to  **TCP**. Set **Port Range** of the two rules to **28443** and **20009**, respectively. For details, see **Virtual Private Cloud User Guide**  \>  **Security**  \>  **Security Group**  \>  **Adding a Security Group Rule**.  

4.  On the VPC management console, apply for an EIP and bind it to the ECS.

    See the  **Virtual Private Cloud User Guide**  \>  **Network Components**  \>  **EIP**  \>  **Assigning an EIP and Binding It to an ECS**\).

5.  Log in to the ECS.

    The account, password, EIP, and security group configuration rules of the Windows system are required for logging in to the ECS. For details about how to log in to the ECS, see  **Elastic Cloud Server User Guide**  \>  **Getting Started**  \>  **Logging In to an ECS**  \>  **Logging In to a Windows ECS Using a Password \(MSTSC\)**.

6.  On the Windows remote desktop, use your browser to access MRS Manager.

    For example, you can use Internet Explorer 11 in the Windows 2012 OS.

    In the browser address bar, enter  **https://_Floating_** **_IP Address_:28443/web**. Enter the name and password of the MRS cluster user, for example, user **admin**.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   If you access MRS Manager with other MRS cluster usernames, change the password upon your first access. The new password must meet the requirements of the current password complexity policies. For details, contact the administrator.  
    >-   By default, a user is locked after inputting an incorrect password five consecutive times. The user is automatically unlocked after 5 minutes.  

7.  If you want to exit MRS Manager, move the cursor to  ![](figures/en-us_image_0125375393.jpg) in the upper-right corner and click **Log Out**.

## Related Operation<a name="section5824002417933"></a>

**Configuring mapping between node names and IP addresses**

1.  Log in to MRS Manager and click  **Host**.

    Record the  **Host Name** and **OM IP Address**  of all nodes in a cluster.

2.  In the work environment, use  **Notepad** to open the **hosts**  file and add the mapping relationship between node names and IP addresses to the file.

    Each mapping relationship occupies an independent line. The following is an example:

    ```
    192.168.4.127 node-core-Jh3ER
    192.168.4.225 node-master2-PaWVE
    192.168.4.19 node-core-mtZ81
    192.168.4.33 node-master1-zbYN8
    192.168.4.233 node-core-7KoGY
    ```

    Save the configurations and exit.


