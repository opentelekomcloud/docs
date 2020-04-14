# Setting Account Security Policies<a name="en-us_topic_0046611308"></a>

Users with the  **Security Administrator**  permission can set a login authentication policy, password policy, ACL, and operation security protection to improve user information and system security.

## Procedure<a name="section13189358"></a>

1.  Set login verification policies.
    1.  In the navigation pane, choose  **Account Settings**  \>  **Login Authentication Policies**.
    2.  In the  **Account Disabling Policy**  area, select  **If an account is not used within the validity period, it will be disabled.**  Then set  **Account Expiration**. If the user does not access the cloud system through the management console or API within the set  **Account Expiration**, the account will be disabled.

        **Account Disabling Policy**  is set to protect the account. After the account is disabled, resources in the account are not affected. You can contact the administrator to enable the account again.

    3.  In the  **Session Timeout Policy**  area, set  **Session Timeout Duration**. The default value is  **15**  minutes. You can set the session timeout duration from 15 minutes to 24 hours. If the user does not perform any operation within the specified duration, the user needs to log in again.
    4.  In the  **Recent Login Information**  area, select  **Display last login information upon a successful login**.

        Users can view login information, such as the time of their last login, on the  **Login Verification**  page.

    5.  In the  **Login Verification Information**  area, customize the verification information, which is displayed upon a successful login.

        Users can view this customized information on the  **Login Verification**  page.

    6.  Click  **OK**.

2.  Set an ACL.
    1.  In the navigation pane, choose  **Account Settings**  \>  **ACLs**.

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >ACL validation conditions:  
        >-   Accessing cloud services by using the management console: An ACL takes effect for the users in the account but not for the account itself.  
        >-   Accessing cloud services by calling APIs: An ACL takes effect for the account itself and the users in the account. When an ACL is modified, it takes effect two hours later.  

    2.  On the  **ACLs**  page, enter the allowed IP addresses or network segments.

        -   **Allowed IP Address Range**: only allows users to access the system using specified IP addresses.
        -   **Allowed IP Addresses or Network Segments**: only allows users to access the system using specified IP addresses or network segments.

            For example: 10.10.10.10/32.

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >-   You can click  **Restore Defaults**  to restore the allowed IP address range to the default value,  **0.0.0.0**-**255.255.255.255**, and to clear  **Allowed IP Addresses or Network Segments**.  
        >-   If both  **Allowed IP Address Range**  and  **Allowed IP Addresses or Network Segments**  are set, users are allowed to access the system if their IP address meets the conditions specified by either of the two parameters.  

    3.  Click  **Apply**.

3.  Set operation security protection. If this function is enabled, authentication is required for high-risk operations. For example, a user needs to enter the verification code when deleting an access key.
    1.  In the navigation pane, choose  **Account Settings**  \>  **Operation Security**.
    2.  Enable operation security protection.

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >-   Operation security protection is disabled by default.  
        >-   High-risk operations are defined by each service.  
        >-   When a user performs a high-risk operation, the  **Operation Security**  page is displayed. Select a verification mode, email verification or phone verification.  
        >    -   If users have bound only mobile numbers to their accounts, only phone verification can be selected.  
        >    -   If users have bound only email addresses to their accounts, only email verification can be selected.  
        >    -   If users have bound both mobile numbers and email addresses to their accounts, phone verification is selected by default. Users can manually change the verification mode to email verification.  
        >    -   If users have not bound mobile numbers or email addresses to their accounts, operation security verification does not take effect. The operation is allowed by default.  



