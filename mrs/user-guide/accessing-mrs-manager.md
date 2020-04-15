# Accessing MRS Manager<a name="EN-US_TOPIC_0125376155"></a>

## Scenario<a name="section6069209810190"></a>

MRS Manager supports MRS cluster monitoring, configuration, and management. You can open the Manager page on the  **MRS Console**  page.

For clusters with Kerberos authentication disabled, you can open MRS Manager on  **MRS Console**. For clusters with Kerberos authentication enabled, see [Accessing MRS Manager Supporting Kerberos Authentication](accessing-mrs-manager-supporting-kerberos-authentication.md)  to learn how to access MRS Manager.

## Procedure<a name="section84831342172417"></a>

If the cluster version is MRS 1.9.2 or later, perform the following steps:

1.  Log in to the MRS management console.
2.  In the navigation pane, choose  **Clusters** \> **Active Clusters**. Click the target cluster name to access the cluster details page.
3.  Click  **View**. The **Access MRS Manager**  page is displayed.
    1.  Select an available EIP from the drop-down list or click  **Manage EIP**  to purchase one.
    2.  Add a security group rule. By default, the user's public IP address used for accessing port 9022 is filled in the rule. If you want to add multiple IP address segments to a trusted range for accessing MRS Manager, refer to  [6](#li1049410469610)  to  [9](#li035723593115). If you want to view, modify, or delete a security group rule, click  **Manage Security Group Rule**.

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >-   It is normal that the automatically generated public IP address is different from the local IP address and no action is required.  
        >-   If port 9022 is a Knox port, you need to enable the permission of port 9022 to access Knox for accessing MRS Manager.  

    3.  Select the checkbox indicating that "**I** **confirm that xx.xx.xx.xx is a trusted public IP address and MRS Manager can be accessed using this IP address**."

4.  Click  **OK**. The MRS Manager login page is displayed.
5.  Enter the default username  **admin** and password you set when creating the cluster, and click **Log In**. The  **MRS Manager**  page is displayed.
6.  <a name="li1049410469610"></a>On the MRS management console, click  **Active Clusters**  and click the target cluster name to access the cluster details page.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >To assign MRS Manager access permissions to other users, perform  [6](#li1049410469610)  to  [9](#li035723593115)  to add the users' public IP addresses to a trusted range.  

7.  Click  **Add Security Group Rule**  behind the EIP.
8.  On the  **Add Security Group Rule**  page, enter a public IP address range to open the access permissions and select the checkbox indicating that "**I confirm that the authorized object is a trusted public IP address range. Do not use 0.0.0.0/0. Otherwise, security risks may arise**.".

    By default, your public IP address is filled in the rule. If you want to change the IP address segment, for example, add multiple IP address segments to a trusted range, repeat  [6](#li1049410469610)  to  [9](#li035723593115). If you want to view, modify, or delete a security group rule, click  **Manage Security Group Rule**.

9.  <a name="li035723593115"></a>Click  **OK**  to add the security group rule.

If the cluster version is earlier than MRS 1.9.2, perform the following steps:

1.  Log in to the MRS management console.
2.  In the navigation pane, choose  **Clusters** \> **Active Clusters**. Click the target cluster name to access the cluster details page.
3.  Click  **View**  to open MRS Manager.

    If you access MRS Manager after successfully logging in to the MRS console, you do not need to enter the password again because user  **admin**  is used for login by default.


