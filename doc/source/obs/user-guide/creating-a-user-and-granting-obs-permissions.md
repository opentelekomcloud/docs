# Creating a User and Granting OBS Permissions<a name="obs_03_0122"></a>

## Process<a name="section35143124418"></a>

**Figure  1**  Granting an IAM user the access permissions to OBS<a name="fig292324264713"></a>  
![](figures/granting-an-iam-user-the-access-permissions-to-obs.png "granting-an-iam-user-the-access-permissions-to-obs")

## Procedure<a name="section2074420567337"></a>

1.  Log in to the management console using a cloud service account.
2.  On the top navigation menu, choose  **Service List**  \>  **Management & Deployment**  \>  **Identity and Access Management**. The IAM console page is displayed.
3.  Create a user group and grant the OBS permissions to the user group.

    User groups facilitate centralized user management and streamlined permissions management. Users in the same user group have the same permissions. Users created in IAM inherit permissions from the groups to which they belong.

    1.  In the navigation pane on the left, click  **User Groups**. The  **User Groups**  page is displayed.
    2.  Click  **Create User Group**.
    3.  On the  **Create User Group**  page, enter a name for the user group and click  **OK**.

        The user group is displayed in the user group list once the creation completes.

    4.  Click  **Modify**  in the  **Operation**  column of the row where the created user group resides.
    5.  In the  **Group Permissions**  area, locate  **OBS \(S3\)**, click  **Attach Policy**  in the  **Operation**  column, select the policy name, and click  **OK**.

        >![](public_sys-resources/icon-note.gif) **NOTE:** 
        >In the  **Policy Information**  area, you can view the details about the policy.


4.  Create a user.
    1.  In the navigation pane on the left, click  **Users**. The  **Users**  page is displayed.
    2.  Click  **Create User**.
    3.  Set user information and click  **Next**.

        **Table  1**  User parameters

        <a name="table127131345071"></a>
        <table><thead align="left"><tr id="row4714144517714"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p137145451578"><a name="p137145451578"></a><a name="p137145451578"></a>Parameter</p>
        </th>
        <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p1071417451679"><a name="p1071417451679"></a><a name="p1071417451679"></a>Description</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row157141451376"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p1971404515717"><a name="p1971404515717"></a><a name="p1971404515717"></a>Username</p>
        </td>
        <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p1871494519719"><a name="p1871494519719"></a><a name="p1871494519719"></a>The user name for logging in to the cloud service.</p>
        </td>
        </tr>
        <tr id="row37141245171"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p3714645874"><a name="p3714645874"></a><a name="p3714645874"></a>Credential Type</p>
        </td>
        <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><div class="p" id="p1652150296"><a name="p1652150296"></a><a name="p1652150296"></a>A credential refers to the identity credential used for user system authentication. In this example, password is selected.<a name="ul194541357781"></a><a name="ul194541357781"></a><ul id="ul194541357781"><li><strong id="b293243261112"><a name="b293243261112"></a><a name="b293243261112"></a>Password</strong>: Used for accessing cloud services using the console or development tools.</li><li><strong id="b4990439141110"><a name="b4990439141110"></a><a name="b4990439141110"></a>Access key</strong>: Used for logging to the cloud service using development tools. This credential type is more secure, and is recommended if the user does not need to use the console.</li></ul>
        </div>
        </td>
        </tr>
        <tr id="row67141445471"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p167148452713"><a name="p167148452713"></a><a name="p167148452713"></a>User Groups</p>
        </td>
        <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p1471412456719"><a name="p1471412456719"></a><a name="p1471412456719"></a>You can add a user to one or more user groups. Then the user will inherit the permissions granted to these user groups. The default user group <strong id="b181532620463"><a name="b181532620463"></a><a name="b181532620463"></a>admin</strong> has the administrator permissions and all of the permissions required to use all cloud resources.</p>
        </td>
        </tr>
        <tr id="row16714184512714"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p142481183015"><a name="p142481183015"></a><a name="p142481183015"></a>Description</p>
        </td>
        <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p167144453719"><a name="p167144453719"></a><a name="p167144453719"></a>(Optional) Brief description about the user.</p>
        </td>
        </tr>
        </tbody>
        </table>

    4.  Select a type for password generation, set the email address and mobile number, and click  **OK**.

5.  Use the created IAM user to log in to OBS Console and verify the user permissions.

