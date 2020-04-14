# Resetting the Password of the Cluster Administrator<a name="dws_01_0026"></a>

## Scenario<a name="section43782126162722"></a>

This section describes how to reset the password of the cluster administrator account on the  **Cluster Management**  page when the administrator forgets the password or the administrator account is locked after 10 consecutive incorrect password attempts.

## Procedure<a name="section59074732104918"></a>

1.  Log in to the management console at  [https://console.otc.t-systems.com/dws/](https://console.otc.t-systems.com/dws/).
2.  Click  **Cluster Management**.
3.  In the  **Operation**  column of the target cluster, choose  **More**  \>  **Reset Password**.

    **Figure  1**  Password resetting<a name="fig6184953135917"></a>  
    ![](figures/password-resetting.png "password-resetting")

4.  On the displayed  **Reset Password**  page, set a new password, confirm the password, and then click  **OK**.

    The password complexity requirements are as follows:

    -   Consists of 8 to 32 characters.
    -   Cannot be the same as the username or the username written in reverse order.
    -   Must contain at least 3 of the following character types: uppercase letters, lowercase letters, digits, and special characters \~!@\#%^&\*\(\)-\_=+|\[\{\}\];:,<.\>/?
    -   Passes the weak password check.

    -   Be different from the old password and cannot be the reverse of the old password.
    -   Cannot use a history password.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If the default administrator account of the cluster is deleted or renamed, password resetting fails.  


