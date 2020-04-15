# Downloading a User Authentication File<a name="EN-US_TOPIC_0125375983"></a>

## Scenario<a name="sa5702491ae2d4fbda8ab1d5158a4a85e"></a>

When a user develops big data applications and runs them in an MRS cluster that supports Kerberos authentication, the user needs to prepare a  **Machine-machine**  user authentication file for accessing the MRS cluster. The keytab file in the authentication file can be used for user authentication.

This section describes how to download a  **Machine-machine**  user authentication file and export the keytab file on MRS Manager.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>Before you download a  **Human-machine** user authentication file, change the password for the user on MRS Manager to make the initial password set by the administrator invalid. Otherwise, the exported keytab file cannot be used. For details, see [Changing the Password of an Operation User](changing-the-password-of-an-operation-user.md).  

## Procedure<a name="s8e230768fd9d469fb2fc5ee7b4a82697"></a>

1.  On MRS Manager, click  **System**.
2.  In the  **Permission** area, click **Manage User**.
3.  In the row of a user for whom you want to export the keytab file, choose  **More**  \>  **Download authentication credential**  to download the authentication file. After the file is automatically generated, save it to a specified path and keep it secure.
4.  Open the authentication file with a decompression program.
    -   **user.keytab**  indicates a user keytab file used for user authentication.
    -   **krb5.conf**  indicates the configuration file of the authentication server. The application connects to the authentication server according to the configuration file information when authenticating users.


