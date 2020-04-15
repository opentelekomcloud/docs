# Changing the Password for the LDAP Administrator and the LDAP User \(including OMS LDAP\)<a name="EN-US_TOPIC_0221415058"></a>

## Scenario<a name="section446724189518"></a>

Periodically change the password for LDAP administrator  **rootdn:cn=root,dc=hadoop,dc=com** and LDAP user **pg\_search\_dn:cn=pg\_search\_dn,ou=Users,dc=hadoop,dc=com**  of the MRS cluster to improve the system O&M security.

## Impact on the System<a name="section2536914895153"></a>

All services need to be restarted for the new password to take effect. Services are unavailable during the restart.

## Procedure<a name="section1075407895245"></a>

1.  On the MRS cluster details page, click  **Services**.
2.  Choose  **LdapServer \> More \> Change Password**.
3.  In the  **Change Password** dialog box, select the user that you want to change the password from **User Information**.
4.  In the  **Change Password** dialog box, enter the old password in **Old Password** and the new password in **New Password** and **Confirm Password**.

    The password complexity requirements are as follows:

    -   The password must contain 16 to 32 characters.
    -   The password must contain at least three types of the following: lowercase letters, uppercase letters, digits, and special characters which can only be \`\~!@\#$%^&\*\(\)-\_=+\\|\[\{\}\];:'",<.\>/?
    -   The password cannot be the same as the username or reverse username.
    -   The password cannot be the same as the previous password.

5.  Select  **I have read the information and understand the impact**, and click **OK**  to confirm the password change and restart the service.

