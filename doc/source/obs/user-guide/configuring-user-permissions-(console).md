# Configuring User Permissions<a name="obs_03_0304"></a>

If your cloud service account does not need individual IAM users, then you may skip this section. Your permissions to use OBS functions are not affected.

If IAM users are required, you need to grant OBS access permissions to the users. Because OBS is separately deployed from other cloud resources.

## Process<a name="section12521716448"></a>

**Figure  1**  Granting an IAM user the access permissions to OBS<a name="obs_03_0122_fig292324264713"></a>  
![](figures/granting-an-iam-user-the-access-permissions-to-obs.png "granting-an-iam-user-the-access-permissions-to-obs")

## Procedure<a name="section1056019017457"></a>

1.  Log in to the management console using a cloud service account.
2.  On the top navigation menu, choose  **Service List**  \>  **Management & Deployment**  \>  **Identity and Access Management**. The IAM console page is displayed.
3.  Create a user group and grant the OBS permissions to the user group.

    User groups facilitate centralized user management and streamlined permissions management. Users in the same user group have the same permissions. Users created in IAM inherit permissions from the groups to which they belong.

    1.  In the navigation pane on the left, click  **User Groups**. The  **User Groups**  page is displayed.
    2.  Click  **Create User Group**.
    3.  On the  **Create User Group**  page, enter a name for the user group and click  **OK**.

        The user group is displayed in the user group list once the creation completes.

    4.  In the row where the newly created user group resides, click  **Assign Permissions**  in the  **Operation**  column. Then on the  **Group Permissions**  tab page that is displayed, find OBS in the global service region.
    5.  Click  **Attach Policy**  in the  **Operation**  column, select the required policy, and click  **OK**.

        >![](/images/icon-note.gif) **NOTE:**   
        >Unfold  **Policy Content**, you can view the details about the policy.  


4.  Create a user.
    1.  In the navigation pane on the left, click  **Users**. The  **Users**  page is displayed.
    2.  Click  **Create User**.
    3.  Set user information and click  **Next**.

        **Table  1**  User parameters

        <a name="obs_03_0122_table127131345071"></a>
        <table><thead align="left"><tr id="obs_03_0122_row4714144517714"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="obs_03_0122_p137145451578"><a name="obs_03_0122_p137145451578"></a><a name="obs_03_0122_p137145451578"></a>Parameter</p>
        </th>
        <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="obs_03_0122_p1071417451679"><a name="obs_03_0122_p1071417451679"></a><a name="obs_03_0122_p1071417451679"></a>Description</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="obs_03_0122_row157141451376"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="obs_03_0122_p1971404515717"><a name="obs_03_0122_p1971404515717"></a><a name="obs_03_0122_p1971404515717"></a>Username</p>
        </td>
        <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="obs_03_0122_p1871494519719"><a name="obs_03_0122_p1871494519719"></a><a name="obs_03_0122_p1871494519719"></a>The user name for logging in to the cloud service.</p>
        </td>
        </tr>
        <tr id="obs_03_0122_row37141245171"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="obs_03_0122_p3714645874"><a name="obs_03_0122_p3714645874"></a><a name="obs_03_0122_p3714645874"></a>Credential Type</p>
        </td>
        <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><div class="p" id="obs_03_0122_p1652150296"><a name="obs_03_0122_p1652150296"></a><a name="obs_03_0122_p1652150296"></a>A credential refers to the identity credential used for user system authentication. In this example, password is selected.<a name="obs_03_0122_ul194541357781"></a><a name="obs_03_0122_ul194541357781"></a><ul id="obs_03_0122_ul194541357781"><li>Password: Used for accessing cloud services using the console or development tools.</li><li>Access key: Used for logging to the cloud service using development tools. This credential type is more secure, and is recommended if the user does not need to use the console.</li></ul>
        </div>
        </td>
        </tr>
        <tr id="obs_03_0122_row67141445471"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="obs_03_0122_p167148452713"><a name="obs_03_0122_p167148452713"></a><a name="obs_03_0122_p167148452713"></a>User Groups</p>
        </td>
        <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="obs_03_0122_p1471412456719"><a name="obs_03_0122_p1471412456719"></a><a name="obs_03_0122_p1471412456719"></a>You can add a user to one or more user groups. Then the user will inherit the permissions granted to these user groups. The default user group <strong id="obs_03_0122_b181532620463"><a name="obs_03_0122_b181532620463"></a><a name="obs_03_0122_b181532620463"></a>admin</strong> has the administrator permissions and all of the permissions required to use all cloud resources.</p>
        </td>
        </tr>
        <tr id="obs_03_0122_row16714184512714"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="obs_03_0122_p142481183015"><a name="obs_03_0122_p142481183015"></a><a name="obs_03_0122_p142481183015"></a>Description</p>
        </td>
        <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="obs_03_0122_p167144453719"><a name="obs_03_0122_p167144453719"></a><a name="obs_03_0122_p167144453719"></a>(Optional) Brief description about the user.</p>
        </td>
        </tr>
        </tbody>
        </table>

    4.  On the next page, set a password type, an email address, and a mobile number, and click  **OK**.

        Password Types:

        -   **Set at first login**: Select this option if you are not the entity using the user that is being created. The new user can log in to the cloud service through the one-time link provided in the email and set the password upon login.
        -   **Automatically generated**: Select this option if the user that is being created will access the cloud service through development tools. A 10-digit password will be automatically generated.
        -   **Set manually**: Select this option if you are the entity using the user that is being created.

5.  Use the created IAM user to log in to OBS Console and verify the user permissions.

