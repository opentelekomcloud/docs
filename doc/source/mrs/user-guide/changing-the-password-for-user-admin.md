# Changing the Password for User admin<a name="EN-US_TOPIC_0221415055"></a>

Periodically change the password for user  **admin**  to improve the system O&M security.

If the password is changed, the downloaded user credential will be unavailable. You need to download the authentication credential again, and replace the old credential with new one.

## Changing the Password for User admin on the Cluster Node<a name="section41705179143539"></a>

1.  Update the client of the active management node. For details, see  [Updating the Client](updating-the-client.md).
2.  Log in to the active management node.
3.  \(Optional\) If you want to change the password as user  **omm**, run the following command to switch the user:

    **sudo su - omm**

4.  Run the following command to go to the client directory:

    **cd /opt/client**

5.  Run the following command to configure environment variables:

    **source bigdata\_env**

6.  Run the following command to change the password for user  **admin**. This operation takes effect in the entire cluster.

    **kpasswd admin**

    Enter the old password and then enter a new password twice.

    For the MRS 1.6.3 or later cluster, the default password complexity requirements are as follows:

    -   The password must contain at least 8 characters.
    -   The password must contain at least three types of the following: lowercase letters, uppercase letters, digits, spaces, and special characters which can only be \~\`!?,.:;-\_'\(\)\{\}\[\]/<\>@\#$%^&\*+|\\=
    -   The password cannot be the same as the username or reverse username.


## Changing the Password for User admin on MRS Manager<a name="section59954398143935"></a>

The password of user  **admin**  can be changed on MRS Manager only for clusters with Kerberos authentication enabled and clusters with Kerberos authentication disabled but the EIP function enabled.

1.  Log in to MRS Manager as user  **admin**.
2.  Click the username in the upper right corner and choose  **Change Password**.
3.  On the  **Change Password**  page, set  **Old Password**,  **New Password**, and  **Confirm Password**.

    >![](/images/icon-note.gif) **NOTE:**   
    >The default password complexity requirements are as follows:  
    >-   The password must contain 8 to 32 characters.  
    >-   The password must contain at least three types of the following: lowercase letters, uppercase letters, digits, spaces, and special characters which can only be '\~!@\#$%^&\*\(\)-\_=+\\|\[\{\}\];:'",<.\>/?  
    >-   The password cannot be the same as the username or reverse username.  

4.  Click  **OK**. Log in to MRS Manager again with the new password.

