# Creating a User Group<a name="EN-US_TOPIC_0125375850"></a>

## Scenario<a name="sa9c5d5718780410abadb38f2c1a3a6f9"></a>

This section describes how to create user groups and specify their operation permissions on MRS Manager. Management of single or multiple users can be unified in the user groups. After being added to a user group, users can obtain operation permissions owned by the user group.

Up to 100 user groups can be created on MRS Manager.

## Prerequisites<a name="s4c410d4536d24bc6ba636a26c8ab144c"></a>

-   Administrators have learned service requirements and created roles required by service scenarios.
-   You have obtained a cluster with Kerberos authentication enabled or a normal cluster with the EIP function enabled.

## Procedure<a name="s721fc66598ab4a19aaeb75442bd08d60"></a>

1.  On MRS Manager, click  **System**.
2.  In the  **Permission** area, click **Manage User Group**.
3.  Above the user group list, click  **Create User Group**.
4.  Set  **Group Name** and **Description**.

    **Group Name** is mandatory and contains 3 to 20 digits, letters, and underscores \(\_\). **Description**  is optional.

5.  In  **Role**, click **Select and Add Role**  to select and add specified roles.

    If you do not add the roles, the user group you are creating now does not have the permission to use MRS clusters.

6.  Click  **OK**. The user group is created.

## Related Tasks<a name="s8b3f4e1eddd4484a89bd0259fac2463b"></a>

**Modifying a user group**

1.  On MRS Manager, click  **System**.
2.  In the  **Permission** area, click **Manage User Group**.
3.  In the row of a user group to be modified, click  **Modify**.

    >![](/images/icon-note.gif) **NOTE:**   
    >If you change role permissions assigned to the user group, it takes 3 minutes to make new configurations take effect.  

4.  Click  **OK**. The modification is complete.

**Deleting a user group**

1.  On MRS Manager, click  **System**.
2.  In the  **Permission** area, click **Manage User Group**.
3.  In the row of the user group to be deleted, click  **Delete**.
4.  Click  **OK**. The user group is deleted.

