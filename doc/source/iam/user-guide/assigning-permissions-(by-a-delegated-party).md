# Assigning Permissions \(by a Delegated Party\)<a name="iam_01_0063"></a>

When an account establishes a trust relationship between itself and your account, you become a delegated party. You can authorize a user to manage resources of the delegating party. After an account establishes multiple trust relationships between itself and your account, you can authorize different users to manage resources of the delegating party. However, each user can switch to only the delegated agencies. You can create custom policies to grant specified permissions to users.

## Prerequisites<a name="section8625973163627"></a>

-   An account has created the trust relationship with you.
-   You have obtained the name of the delegating account and the name and ID of the created agency.

## Procedure<a name="section126738501115"></a>

1.  <a name="li4527132844312"></a>Create a custom policy.

    >![](/images/icon-note.gif) **NOTE:**   
    >-   To delegate a specific agency to a user, perform the following steps.  
    >-   To delegate all agencies to a user, go to  [2](#li135311310144613).  

    1.  In the navigation pane, choose  **Policies**.
    2.  On the  **Policies**  page, click  **Create Custom Policy**.
    3.  Enter a policy name.
    4.  Select  **Global-level service**  for  **Scope**.
    5.  In the  **Policy Information**  area, enter the following content:

        ```
        {
                "Version": "1.1",
                "Statement": [
                        {
                                "Action": [
                                        "iam:agencies:assume"
                                ],
                                "Resource": {
                                        "uri": [
                                                "/iam/agencies/b36b1258b5dc41a4aa8255508xxx..."
                                        ]
                                },
                                "Effect": "Allow"
                        }
                ]
        }
        ```

        >![](/images/icon-note.gif) **NOTE:**   
        >-   Copy and paste all the content, and replace  _b36b1258b5dc41a4aa8255508xxx..._  with the ID of the agency to be granted.  
        >-   This procedure provides only required operations for fine-grained authorization. For more information about fine-grained policies, see  [Fine-grained Policy Management](fine_grained_policy_management).

    6.  Click  **OK**.

2.  <a name="li135311310144613"></a>Create a user group and grant permissions to it.
    1.  In the navigation pane, choose  **User Groups**.
    2.  On the  **User Groups**  page, click  **Create User Group**.
    3.  Enter a user group name.
    4.  Click  **OK**.

        The user group list is displayed, including the newly created user group.

    5.  Click  **Modify**  in the  **Operation**  column of the row that contains the newly created user group.
    6.  Click  **Configure Permission**  in the  **Operation**  column of the row that contains the newly created user group.
    7.  In the  **User Group Permissions**  area, click  **Modify**  in the  **Operation**  column of the row that contains the  **Global**  project.
    8.  On the  **User Group Permissions**  tab page, click  **Configure Policy**  in the  **Operation**  column of the row that contains the  **Global**  project.
    9.  Select the policy created in  [1](#li4527132844312)  or the  **Agent Operator**  permission.

        >![](/images/icon-note.gif) **NOTE:**   
        >-   Custom policy: Allows a user to access only a specified agency.  
        >-   **Agent Operator**  permission: Allows a user to access all agencies.  

    10. Click  **OK**.

3.  <a name="li695863494610"></a>Create a user and add it to the user group.
    1.  In the navigation pane, choose  **Users**.
    2.  On the  **Users**  page, click  **Create User**.
    3.  On the  **Create User**  page, enter  **Username**.
    4.  Select  **Password**  for  **Credential Type**.
    5.  Select the user group created in  [2](#li135311310144613)  from the drop-down list box in the  **User Groups**  area.
    6.  Click  **Next**.
    7.  Select  **Set at first login**  for  **Password Type**.
    8.  Enter an email address.
    9.  Click  **OK**.

4.  Switch your roles.
    1.  Log in to the system as the user created in  [3](#li695863494610).
    2.  Click the logged-in account in the upper right corner of the page and choose  **Switch Role**.
    3.  On the  **Switch Role**  page, enter the name of the delegating account.

        >![](/images/icon-note.gif) **NOTE:**   
        >The system automatically matches the account to an agency. If the matched agency has not been delegated, you have no permissions to access the account. However, you can remove the agency and select an authorized one from the drop-down list box.  

    4.  Click  **OK**  to switch to the delegating account.


## Follow-up Operation<a name="section54138067163127"></a>

Click the delegating account in the upper right corner of the page and choose  **Switch Role**  to switch back to your account.

