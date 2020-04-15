# Synchronizing IAM Users to MRS<a name="EN-US_TOPIC_0226013039"></a>

IAM user synchronization is to synchronize IAM users bound with MRS policies to the MRS system and create accounts sharing same names with the IAM users but different passwords. Then, you can use an IAM username \(the password needs to be reset by user  **admin**  of MRS Manager\) to log in to MRS Manager for cluster management, and submit jobs on the GUI in a cluster with Kerberos authentication enabled.

[Table 1](#table3878619101919)  compares IAM users' permission policies and the synchronized users' permissions on MRS. For details about the default permissions on MRS Manager, see  [Users and Permissions of Clusters with Kerberos Authentication Enabled](users-and-permissions-of-clusters-with-kerberos-authentication-enabled.md).

**Table  1**  Policy and permission mapping after synchronization

<a name="table3878619101919"></a>
<table><thead align="left"><tr id="row5879191971913"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.1"><p id="p135212352216"><a name="p135212352216"></a><a name="p135212352216"></a>Policy Type</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.2"><p id="p12879101917195"><a name="p12879101917195"></a><a name="p12879101917195"></a>IAM Policy</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.3"><p id="p724173216312"><a name="p724173216312"></a><a name="p724173216312"></a>User's Default Permissions on MRS After Synchronization</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.4"><p id="p12472158103113"><a name="p12472158103113"></a><a name="p12472158103113"></a>Have Permission to Perform the Synchronization</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.5"><p id="p14949142373515"><a name="p14949142373515"></a><a name="p14949142373515"></a>Have Permission to Submit Jobs</p>
</th>
</tr>
</thead>
<tbody><tr id="row1087961921914"><td class="cellrowborder" rowspan="3" valign="top" width="20%" headers="mcps1.2.6.1.1 "><p id="p2104201613119"><a name="p2104201613119"></a><a name="p2104201613119"></a>Fine-grained</p>
<p id="p191048161316"><a name="p191048161316"></a><a name="p191048161316"></a></p>
<p id="p16104101643115"><a name="p16104101643115"></a><a name="p16104101643115"></a></p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="p4306134273012"><a name="p4306134273012"></a><a name="p4306134273012"></a>MRS ReadOnlyAccess</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.3 "><p id="p10949195293012"><a name="p10949195293012"></a><a name="p10949195293012"></a>Manager_viewer</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.4 "><p id="p7473381310"><a name="p7473381310"></a><a name="p7473381310"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p16423218365"><a name="p16423218365"></a><a name="p16423218365"></a>No</p>
</td>
</tr>
<tr id="row987918191191"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p230604216306"><a name="p230604216306"></a><a name="p230604216306"></a>MRS CommonOperations</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><a name="ul4444174612152"></a><a name="ul4444174612152"></a><ul id="ul4444174612152"><li>Manager_viewer</li><li>default</li></ul>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p1347315893112"><a name="p1347315893112"></a><a name="p1347315893112"></a>No</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p15642122116367"><a name="p15642122116367"></a><a name="p15642122116367"></a>Yes</p>
</td>
</tr>
<tr id="row7879181971912"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p1530654223011"><a name="p1530654223011"></a><a name="p1530654223011"></a>MRS FullAccess</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><a name="ul7241758151514"></a><a name="ul7241758151514"></a><ul id="ul7241758151514"><li>Manager_administrator</li><li>Manager_auditor</li><li>Manager_operator</li><li>Manager_tenant</li><li>Manager_viewer</li><li>System_administrator</li><li>default</li></ul>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p84738823119"><a name="p84738823119"></a><a name="p84738823119"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p16425213366"><a name="p16425213366"></a><a name="p16425213366"></a>Yes</p>
</td>
</tr>
<tr id="row688031916194"><td class="cellrowborder" rowspan="3" valign="top" width="20%" headers="mcps1.2.6.1.1 "><p id="p18374033173417"><a name="p18374033173417"></a><a name="p18374033173417"></a>RBAC</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="p1530634213017"><a name="p1530634213017"></a><a name="p1530634213017"></a>MRS Administrator</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.3 "><a name="ul162146189167"></a><a name="ul162146189167"></a><ul id="ul162146189167"><li>Manager_administrator</li><li>Manager_auditor</li><li>Manager_operator</li><li>Manager_tenant</li><li>Manager_viewer</li><li>System_administrator</li><li>default</li></ul>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.4 "><p id="p164738811313"><a name="p164738811313"></a><a name="p164738811313"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p3642192173610"><a name="p3642192173610"></a><a name="p3642192173610"></a>Yes</p>
</td>
</tr>
<tr id="row18880151911919"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p19306114211307"><a name="p19306114211307"></a><a name="p19306114211307"></a>Server Administrator, Tenant Guest, and MRS Administrator</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><a name="ul1336513422162"></a><a name="ul1336513422162"></a><ul id="ul1336513422162"><li>Manager_administrator</li><li>Manager_auditor</li><li>Manager_operator</li><li>Manager_tenant</li><li>Manager_viewer</li><li>System_administrator</li><li>default</li></ul>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p2473178103117"><a name="p2473178103117"></a><a name="p2473178103117"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p2020173383615"><a name="p2020173383615"></a><a name="p2020173383615"></a>Yes</p>
</td>
</tr>
<tr id="row11873260273"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p1530624211302"><a name="p1530624211302"></a><a name="p1530624211302"></a>Tenant Administrator</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><a name="ul1514932717501"></a><a name="ul1514932717501"></a><ul id="ul1514932717501"><li>Manager_administrator</li><li>Manager_auditor</li><li>Manager_operator</li><li>Manager_tenant</li><li>Manager_viewer</li><li>System_administrator</li><li>default</li></ul>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p1147318123117"><a name="p1147318123117"></a><a name="p1147318123117"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p172011033183610"><a name="p172011033183610"></a><a name="p172011033183610"></a>Yes</p>
</td>
</tr>
<tr id="row46716711273"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.1 "><p id="p01044164313"><a name="p01044164313"></a><a name="p01044164313"></a>Custom</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="p123065424306"><a name="p123065424306"></a><a name="p123065424306"></a>Custom policy</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.3 "><a name="ul47440335173"></a><a name="ul47440335173"></a><ul id="ul47440335173"><li>Manager_viewer</li><li>default</li></ul>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.4 "><a name="ul1344810351981"></a><a name="ul1344810351981"></a><ul id="ul1344810351981"><li>If custom policies use RBAC policies as a template, refer to the RBAC policies.</li><li>If custom policies use fine-grained policies as a template, refer to the fine-grained policies. The fine-grained policies are recommended.</li></ul>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p112018336360"><a name="p112018336360"></a><a name="p112018336360"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>To facilitate user permission management, use fine-grained policies rather than RBAC policies. In fine-grained policies, the Deny action takes precedence over other actions.  
>-   A user has permission to synchronize IAM users only when the user has the Tenant Administrator role or has the Server Administrator, Tenant Guest, and MRS Administrator roles at the same time.  
>-   A user with the  **action:mrs:cluster:syncUser**  policy has permission to synchronize IAM users.  

## Procedure<a name="section1968244415315"></a>

1.  Log in to the IAM management console and create a user and authorize the user to use MRS.
2.  Log in to the MRS management console and create a cluster. For details, see  [Creating a Cluster](creating-a-cluster.md).
3.  In the left navigation pane, choose  **Clusters**  \>  **Active Clusters**. Click the cluster name to go to the cluster details page.
4.  <a name="li6999515311"></a>In the  **Basic Information**  area on the  ****Dashboard****  tab page, click  ![](figures/en-us_image_0226013672.png)  on the right side of  ****IAM User Sync****  to synchronize IAM users.
5.  After a synchronization request is sent, choose  **Operation Logs**  in the left navigation pane on the MRS console to check whether the synchronization is successful. For details about the logs, see  [Querying Operation Logs](querying-operation-logs.md).
6.  After the synchronization is successful, use the user synchronized with IAM to perform subsequent operations.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   When the policy of the user group to which the IAM user belongs changes from MRS ReadOnlyAccess to MRS CommonOperations, MRS FullAccess, or MRS Administrator, wait for 5 minutes until the new policy takes effect after the synchronization is complete because the  **sssd**  cache of cluster nodes needs time to be updated. Then, submit a job. Otherwise, the job may fail to be submitted.  
    >-   When the policy of the user group to which the IAM user belongs changes from MRS CommonOperations, MRS FullAccess, or MRS Administrator to MRS ReadOnlyAccess, wait for 5 minutes until the new policy takes effect after the synchronization is complete because the  **sssd**  cache of cluster nodes needs time to be updated.  
    >-   After you click the icon on the right side of  **IAM User Sync**, the cluster details page is blank for a short time, because user data is being synchronized. The page will be properly displayed after the data synchronization is complete.  

    -   Submitting jobs in a security cluster: Users can submit jobs using the job management function on the GUI in the security cluster. For details, see  [Running a MapReduce Job](running-a-mapreduce-job.md).
    -   Logging in to MRS Manager

        1.  Log in to MRS Manager as user  **admin**. For details, see  [Accessing MRS Manager](accessing-mrs-manager.md).
        2.  <a name="li169901714175"></a>Initialize the password of the user synchronized with IAM. For details, see  [Initializing the Password of a System User](initializing-the-password-of-a-system-user.md).
        3.  Modify the role bound to the user group to which the user belongs to control user permissions on MRS Manager. For details, see  [Related Tasks](creating-a-user-group.md#s8b3f4e1eddd4484a89bd0259fac2463b). For details about how to create and modify a role, see  [Creating a Role](creating-a-role.md). After the component role bound to the user group to which the user belongs is modified, it takes some time for the role permissions to take effect.
        4.  Log in to MRS Manager using the user synchronized with IAM and the password modified in  [6.b](#li169901714175).

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >If the IAM user's permission changes, go to  [4](#li6999515311)  to perform second synchronization. After the second synchronization, a system user's permissions are the union of the permissions defined in the IAM system policy and the permissions of roles added by the system user on MRS Manager. After the second synchronization, a custom user's permissions are subject to the permissions configured on MRS Manager.  
        >-   System user: If all user groups to which an IAM user belongs are bound to system policies \(RABC policies and fine-grained policies belong to system policies\), the IAM user is a system user.  
        >-   Custom user: If the user group to which an IAM user belongs is bound to any custom policy, the IAM user is a custom user.  



