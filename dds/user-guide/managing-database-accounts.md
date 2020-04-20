# Managing Database Accounts<a name="dds_03_0057"></a>

## Scenarios<a name="section6515110014278"></a>

This section guides you through how to create a database account and change the account password to manage the instances you created. 

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>When creating a database account for a specified DB instance, you are advised to enable the SSL connection to improve data security.  

## **Prerequisites**<a name="section42310965142628"></a>

A  DDS DB instance  has been connected.

-   For details on how to connect to a cluster instance, see  [Connecting to a DB Instance Through a Client](connecting-to-a-db-instance-through-a-client(cluster).md).
-   For details on how to connect to a replica set instance, see  [Connecting to a DB Instance Through a Client](connecting-to-a-db-instance-through-a-client(replica-set).md).

## Account Description<a name="section21810854151259"></a>

To provide management services for DDS DB instances, users  **root**,  **monitor**, and  **backup**  are created when you create a DDS DB instance. Attempting to delete, rename, change the passwords, or change privileges for these accounts will result in errors.

You can change the password of the database administrator  **rwuser**  and any accounts you create.

## Setting Password Strength for Database Accounts<a name="section330367810910"></a>

-   The administrator password must meet the following password policy:
    -   8 to 32 characters in length
    -   A combination of uppercase letters, lowercase letters, digits, and special characters: \~!@\#%^\*-\_=+?

-   The DDS instance database uses comprehensive password security policies. The password of a DDS instance database account must meet the following conditions:
    -   8 to 32 characters in length
    -   A combination of uppercase letters, lowercase letters, digits, and special characters: \~!@\#%^\*-\_=+?


When you create a DB instance, the system automatically checks your password strength. You can change the password as user  **rwuser**. For security reasons, you are advised to set up a strong password.

## Creating an Account<a name="section2493797710952"></a>

1.  Run the following command to select the admin database:

    **use admin**

2.  Run the following command to create a database account \(**user1**  as an example\):

    **db.createUser\(\{user: "user1", pwd: "**_Test\_12345_**", passwordDigestor:"server", roles:\[\{role: "root", db: "admin"\}\]\}\)**

    -   _**server**_: indicates that the password is encrypted on the server.
    -   _**Test\_12345**_: indicates the example new password. The password must be 8 to 32 characters in length and contain uppercase letters, lowercase letters, digits, and special characters, such as \~@\#%-\_!\*+=^?
    -   _**roles**_  restricts the rights of the account. If an empty array is specified, the account does not have any permission.

3.  Check the result:

    The account is successfully created if the following information is displayed:

    ```
    Successfully added user: {
            "user" : "user1",
            "passwordDigestor" : "server",
            "roles" : [
                    {
                            "role" : "root",
                            "db" : "admin"
                    }
            ]
    }
    ```


## Changing a Password<a name="section44669932101727"></a>

1.  Run the following command to select the admin database:

    **use admin**

2.  Uses user  **user1**  as an example. Run the following command to change its password:

    **db.updateUser\("user1", \{passwordDigestor:"server",pwd:"newPasswd12\#"\}\)**

    -   _**server**_: indicates that the password is encrypted on the server.
    -   _**newPasswd12\#**_: indicates the example new password. The password must be 8 to 32 characters in length and contain uppercase letters, lowercase letters, digits, and special characters, such as \~@\#%-\_!\*+=^?

3.  Check the setting result. The password is successfully changed if the following information is displayed:
    -   Cluster

        ```
        mongos>
        ```

    -   Replica set

        ```
        replica:PRIMARY>
        ```



