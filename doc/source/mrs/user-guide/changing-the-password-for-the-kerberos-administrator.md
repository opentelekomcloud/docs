# Changing the Password for the Kerberos Administrator<a name="EN-US_TOPIC_0221415056"></a>

## Scenario<a name="section293727014453"></a>

Periodically change the password for the Kerberos administrator  **kadmin**  of the MRS cluster to improve the system O&M security.

If the password is changed, the downloaded user credential will be unavailable. You need to download the authentication credential again, and replace the old credential with new one.

## Prerequisites<a name="section64718576144528"></a>

A client has been prepared on the Master1 node.

## Procedure<a name="section65388622144546"></a>

1.  Log in to the Master1 node.
2.  \(Optional\) If you want to change the password as user  **omm**, run the following command to switch the user:

    **sudo su - omm**

3.  Run the following command to go to client directory  **/opt/client**.

    **cd /opt/client**

4.  Run the following command to configure the environment variables:

    **source bigdata\_env**

5.  Run the following command to change the password for  **kadmin/admin**. The password change takes effect on all servers.

    **kpasswd kadmin/admin**

    For the MRS 1.6.3 or later cluster, the password complexity requirements are as follows:

    -   The password must contain at least 8 characters.
    -   The password must contain at least three types of the following: lowercase letters, uppercase letters, digits, spaces, and special characters which can only be \~\`!?,.:;-\_'\(\)\{\}\[\]/<\>@\#$%^&\*+|\\=
    -   The password cannot be the same as the username or reverse username.


