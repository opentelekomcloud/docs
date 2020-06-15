# Granting Namespace-Level Permissions \(Kubernetes RBAC Authorization\)<a name="cce_01_0189"></a>

This section describes how to grant CCE users and user groups the permissions to various namespaced resources. Namespace-level authorization is more fine-grained than cluster-level authorization. Users and user groups with both a cluster-wide role \(CCE Admin or CCE Viewer\) and a namespace-wide role can not only perform operations on a cluster but also on specified namespaces in the cluster.  [Process Flow](#section41056841)  shows the process for granting permissions.

## Configuration<a name="section188449192496"></a>

-   You need a public cloud account that has created one or more user groups and IAM users.
-   By way of example, both a user group and a user are granted permissions to access namespaced resources. You have the choice to grant permissions to either users or user groups.
-   The process flow is used only to add namespace permissions policies for users or user groups who never have such policies. To edit permissions policies of users or user groups, click  **Edit**  on the  **Permissions Management**  \>  **Namespace-Level Permissions**  page.
-   If multiple permissions are granted to a user or user group, all of these permissions will take effect at the same time. The permissions granted to a user group are applicable to all users in the user group.

## Constraints<a name="section1687142618538"></a>

Kubernetes RBAC authorization can be used for CCE clusters of v1.13.

Only CCE clusters of v1.11.7-r2 and later support Kubernetes RBAC authorization. By default, Kubernetes RBAC authorization is enabled in container clusters of v1.11.7-r2. For details on cluster version upgrade, see  [Upgrading a Cluster](upgrading-a-cluster.md).

**Table  1**  User permissions comparison

<a name="table886210176509"></a>
<table><thead align="left"><tr id="row14863201719502"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p14863111718502"><a name="p14863111718502"></a><a name="p14863111718502"></a>User Type</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p18636175506"><a name="p18636175506"></a><a name="p18636175506"></a>Cluster Version Earlier Than v1.11.7-r2</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p98631617175014"><a name="p98631617175014"></a><a name="p98631617175014"></a>Cluster Version of v1.11.7-r2 or Later</p>
</th>
</tr>
</thead>
<tbody><tr id="row138631617185012"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1787744075015"><a name="p1787744075015"></a><a name="p1787744075015"></a>Account</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p14863717165019"><a name="p14863717165019"></a><a name="p14863717165019"></a>All permissions</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p18524164555119"><a name="p18524164555119"></a><a name="p18524164555119"></a>All permissions</p>
</td>
</tr>
<tr id="row138631317205019"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p3878104075018"><a name="p3878104075018"></a><a name="p3878104075018"></a>IAM user with the CCE Administrator role</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p270032114512"><a name="p270032114512"></a><a name="p270032114512"></a>All permissions</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p053164611516"><a name="p053164611516"></a><a name="p053164611516"></a>All permissions</p>
</td>
</tr>
<tr id="row1386412176506"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p187854025013"><a name="p187854025013"></a><a name="p187854025013"></a>IAM user with the CCE Admin or CCE Viewer role</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p12703172316516"><a name="p12703172316516"></a><a name="p12703172316516"></a>All permissions</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p986431775011"><a name="p986431775011"></a><a name="p986431775011"></a>Namespace permissions configured on the <strong id="b86254183359"><a name="b86254183359"></a><a name="b86254183359"></a>Permissions Management</strong> page</p>
</td>
</tr>
<tr id="row141962030123614"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p486412177509"><a name="p486412177509"></a><a name="p486412177509"></a>IAM user who is granted the Tenant Guest role and belongs to an account for which fine-grained access control is disabled</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1886418177508"><a name="p1886418177508"></a><a name="p1886418177508"></a>Read-only permission</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1186471717504"><a name="p1186471717504"></a><a name="p1186471717504"></a>Read-only permission</p>
</td>
</tr>
<tr id="row28641117145019"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p11879440195014"><a name="p11879440195014"></a><a name="p11879440195014"></a>IAM user who is granted the Tenant Guest role and belongs to an account for which fine-grained access control is enabled</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p118641617145015"><a name="p118641617145015"></a><a name="p118641617145015"></a>All permissions</p>
<div class="note" id="note13531359163519"><a name="note13531359163519"></a><a name="note13531359163519"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p73541859183514"><a name="p73541859183514"></a><a name="p73541859183514"></a>Enabling fine-grained access control will change read-on permissions to all permissions.</p>
</div></div>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p18864317105017"><a name="p18864317105017"></a><a name="p18864317105017"></a>Namespace permissions configured on the <strong id="b1487817843920"><a name="b1487817843920"></a><a name="b1487817843920"></a>Permissions Management</strong> page</p>
</td>
</tr>
</tbody>
</table>

## Process Flow<a name="section41056841"></a>

A namespace is an abstract collection of resources and objects. It enables resources to be organized into non-overlapping groups. Multiple namespaces can be created in a cluster. Data is isolated between namespaces so namespaces can share the same cluster service while not affecting each other. An important role of namespace is to act as a virtual cluster.

This section describes how to grant namespace-level permissions to the IAM user James001 and the user group Developers created in  [Granting IAM Users the Permissions to Access CCE](granting_iam_users_the_permissions_to_access_cce).

**Figure  1**  Process for granting namespace permissions<a name="fig19140481542"></a>  
![](figures/process-for-granting-namespace-permissions.png "process-for-granting-namespace-permissions")

## Step 1: Grant Namespace Permissions to an IAM User or User Group<a name="section39693318615"></a>

In this step, the IAM user James001 and user group Developers will be granted permissions to operate on resources in a cluster's namespace.

1.  Log in to the CCE console. In the navigation pane, choose  **Permissions Management**.
2.  Click the  **Namespace-Level Permissions**  tab. In the upper right corner of the namespace permissions list, select the cluster that contains the namespace whose access will be managed, and click  **Add Permissions**.

    **Figure  2**  Adding namespace permissions<a name="fig1449163112011"></a>  
    ![](figures/adding-namespace-permissions.png "adding-namespace-permissions")

3.  On the  **Add Permissions**  page, confirm the cluster name, select a namespace whose access will be managed. By way of example, namespace  **default**  is selected.

    **Figure  3**  Selecting a namespace<a name="fig12485439132014"></a>  
    ![](figures/selecting-a-namespace.png "selecting-a-namespace")

4.  Click  **Add Policy for Users**, add the  **admin**  permissions policy for the user group  **Developers**.

    -   **User/User Group**: Select  **User Group**  from the drop-down list and then select  **Developers**  from the user group list.
    -   **Permissions Policy**: Select  **admin**.

    **Figure  4**  Adding permissions for the user group<a name="fig16091311191914"></a>  
    ![](figures/adding-permissions-for-the-user-group.png "adding-permissions-for-the-user-group")

5.  Click  **Add Policy for Namespaces**. Click  **Add Policy for Users**, and add the  **dev-test**  permissions policy for the user James001.

    -   **Namespaces**: Select  **dev-test**.
    -   **User/User Group**: Select  **User**  from the drop-down list and then select  **James001**  from the user list.
    -   **Permissions Policy**: Select  **view**.

    **Figure  5**  Granting namespace permissions<a name="fig25312516202"></a>  
    ![](figures/granting-namespace-permissions.png "granting-namespace-permissions")

6.  Click  **Create**. The namespace permissions granted to the user group and user appear in the permissions list.

    **Figure  6**  Namespace permissions list<a name="fig172791058192119"></a>  
    ![](figures/namespace-permissions-list.png "namespace-permissions-list")

    >![](/images/icon-note.gif) **NOTE:**   
    >To sum up, the Kubernetes RBAC authorization result is as follows:  
    >-   The user group Developers has  **admin**  access to the namespace  **default**. This  **admin**  access also applies to the IAM user James001 in the user group Developers.  
    >-   The IAM user James001 has  **view**  access to the namespace  **dev-test**.  


## Step 2: Log In and Verify Permissions<a name="section191001533766"></a>

Use the username James001 and identity credential to log in to the CCE console, and verify that the IAM user James001 has the namespace permissions.

1.  On the public cloud login page, enter the account name, username, and password, and click  **Log In**.

    -   The account name is the name of the public cloud account that created the IAM user.
    -   The username and password are those set by the account when creating the IAM user James001. You will be prompted to change the initial password at initial login.

    If the login fails, contact the entity owning the account to verify the username and password. Alternatively, you can reset the password.

2.  After successful login, switch to a region where the user has been granted permissions on the management console. The default region is eu-de.
3.  Choose  **Service List**  \>  **Computing \> Cloud Container Engine**  to launch the CCE console. Then verify James001's namespace permissions.

