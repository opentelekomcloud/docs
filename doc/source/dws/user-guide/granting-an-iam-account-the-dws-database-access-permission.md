# Granting an IAM Account the DWS Database Access Permission<a name="dws_01_0135"></a>

The IAM account you use to access a database must be granted with the  **DWS Database Access**  permission. Without this permission, access to databases will fail due to authentication failure. Using the  **DWS Database Access**  permission helps to control access to databases.

The  **DWS Database Access**  permission can only be granted to user groups. Ensure that your IAM account is in a user group with this permission.

On IAM, only users in the  **admin**  group have the rights to manage users. This requires that your IAM account be in the  **admin**  user group. Otherwise, contact the administrator to grant your IAM account this permission.

## Procedure<a name="section183185863313"></a>

1.  Log in to the management console. Grant the  **DWS Database Access**  permission to an IAM user group \(if there is none, create one\).
2.  Add your IAM account into the user group. After doing this, your IAM account has the  **DWS Database Access**  permission.

    For detailed operation, see the  _Identity and Access Management User Guide_.


