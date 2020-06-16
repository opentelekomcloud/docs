# Initializing the Password of a System User<a name="EN-US_TOPIC_0125376061"></a>

## Scenario<a name="s7e6c429d95304231b44076624b81ed88"></a>

This section describes how to initialize a password on MRS Manager if a user forgets the password or the password of a public account needs to be changed regularly. After password initialization, the user must change the password upon the first login. You have obtained a cluster with Kerberos authentication enabled or a normal cluster with the EIP function enabled.

## Impact on the System<a name="s97011bd2cd534a1d8c17ae1557dc77e2"></a>

If you have downloaded a user authentication file, download it again and obtain the keytab file after initializing the password of the MRS cluster user.

## Initializing the Password of a  **Human-machine**  User<a name="section60390340173321"></a>

1.  On MRS Manager, click  **System**.
2.  In the  **Permission** area, click **Manage User**.
3.  In the row that contains the user whose password is to be initialized, click  **More**  \>  **Initialize password**  and change the password as prompted.

    In the window that is displayed, enter the password of the current administrator account and click  **OK**. Then in **Initialize Password**, click **OK**.

    For the MRS 1.6.3 or later cluster, the password complexity requirements are as follows:

    -   The password must contain 8 to 32 characters.
    -   The password must contain at least three types of the following: lowercase letters, uppercase letters, digits, spaces, and special characters which can only be \~\`!?,.:;-\_'\(\)\{\}\[\]/<\>@\#$%^&\*+|\\=
    -   The password cannot be the same as the username or reverse username.


## Initializing the Password of a  **Machine-machine**  User<a name="section6672636417347"></a>

1.  Prepare a client based on service conditions and log in to the node with the client installed.
2.  Run the following command to switch the user:

    **sudo su - omm**

3.  Run the following command to switch to the client directory, for example,  **/opt/client**:

    **cd /opt/client**

4.  Run the following command to configure the environment variables:

    **source bigdata\_env**

5.  Run the following command to log in to the console as user  **kadmin/admin**:

    **kadmin -p kadmin/admin**

6.  Run the following command to reset the password of a component running user: This operation takes effect for all servers.

    **cpw** _Component running user name_

    For example,  **cpw oms/manager**.

    For the MRS 1.6.3 or later cluster, the password complexity requirements are as follows:

    -   The password must contain 8 to 32 characters.
    -   The password must contain at least three types of the following: lowercase letters, uppercase letters, digits, spaces, and special characters which can only be \~\`!?,.:;-\_'\(\)\{\}\[\]/<\>@\#$%^&\*+|\\=
    -   The password cannot be the same as the username or reverse username.


