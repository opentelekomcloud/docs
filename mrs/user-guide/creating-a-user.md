# Creating a User<a name="EN-US_TOPIC_0125375721"></a>

## Scenario<a name="s84a447337b8847d0b81501cd18dbccff"></a>

This section describes how to create users on MRS Manager based on site requirements and specify their operation permissions to meet service requirements.

Up to 1000 users can be created on MRS Manager.

## Prerequisites<a name="seeb5b8aa0edd4cf190c530bd6e75c9bd"></a>

-   Administrators have learned service requirements and created roles and role groups required by service scenarios.
-   You have obtained a cluster with Kerberos authentication enabled or a normal cluster with the EIP function enabled.

## Procedure<a name="s377da01f8123455299999264dfa28b02"></a>

1.  On MRS Manager, click  **System**.
2.  In the  **Permission** area, click **Manage User**.
3.  Above the user list, click  **Create User**.
4.  Configure parameters as prompted and enter a username in  **Username**.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   If a username exists, you cannot create another username that only differs from the existing username in case. For example, if  **User1** has been created, you cannot create **user1**.  
    >-   When you use the user you created, enter the correct username, which is case-sensitive.  
    >-   **Username**  is mandatory and contains 3 to 20 digits, letters, and underscores \(\_\).  
    >-   **root**, **omm**, and **ommdba**  are reserved system users. Select another username.  

5.  Set  **User Type** to either **Human-machine** or **Machine-machine**.
    -   **Human-machine** users: used for O&M on MRS Manager and operations on component clients. If you select this user type, you need to enter a password and confirm the password in **Password** and **Confirm Password**  accordingly.
    -   **Machine-machine**  users: used for MRS application development. If you select this user type, you do not need to enter a password, because the password is randomly generated.

6.  In  **User Group**, click **Select and Join User Group**  to select user groups and add users to them.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   If roles have been added to user groups, the users can be granted with permissions of the roles.  
    >-   If you want to grant new users with Hive permissions, add the users to the Hive group.  
    >-   If you want to manage tenant resources, assign the  **Manager\_tenant**  role and the role corresponding to the tenant to the user group.  

7.  In  **Primary Group**, select a group as the primary group for users to create directories and files. The drop-down list contains all groups selected in **User Group**.
8.  In  **Assign Rights by Role**, click **Select and Add Role**  to add roles for users based on onsite service requirements.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   When you create a user, if permissions of a user group that is granted to the user cannot meet service requirements, you can assign other created roles to the user. It takes 3 minutes to make role permissions granted to the new user take effect.  
    >-   Adding a role when you create a user can specify the user rights.  
    >-   A new user can access WebUIs of HDFS, HBase, Yarn, Spark, and Hue even when roles are not assigned to the user.  

9.  In  **Description**, provide description based on onsite service requirements.

    **Description**  is optional.

10. Click  **OK**. The user is created.

    If a new user is used in the MRS cluster for the first time, for example, used for logging in to MRS Manager or using the cluster client, the password must be changed. For details, see section "Changing the Password of an Operation User".


