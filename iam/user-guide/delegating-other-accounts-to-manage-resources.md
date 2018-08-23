# Delegating Other Accounts to Manage Resources<a name="en-us_topic_0079496986"></a>

To share resources with other accounts or delegate other accounts to manage your resources, you can create an agency and grant resource management permissions to the delegated account.

This section uses account A and the delegated account B as an example to describe how to delegate other accounts to manage resources in your account.

1.  The security administrator of account A creates an agency.

    ![](figures/en-us_image_0126271983.png)

2.  Security administrator B of account B grants user Job the **Agent Operator** permission to manage resources in account A.

    1.  Create a user group \(for example, Agency\) and grant it **Agent Operator** permission.
    2.  Add user Job to the user group **Agency**.
    ![](figures/en-us_image_0126272056.png)

3.  User Job of account B manages the resources in account A.
    1.  Job logs in to the public cloud system and switches the role to account A.
    2.  Job switches to project A.
    3.  Job manages the resources in account A based on permissions.

        ![](figures/en-us_image_0126271971.png)


-   **[Creating an Agency](creating-an-agency.md)**  

-   **[Switching Roles](switching-roles.md)**  


