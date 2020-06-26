# Changing the Password for a Component Database User<a name="EN-US_TOPIC_0221415062"></a>

## Scenario<a name="section3506183102342"></a>

Periodically change the password for each component database user to improve the system O&M security.

## Impact on the System<a name="section55096479102413"></a>

The services need to be restarted for the new password to take effect. Services are unavailable during the restart.

## Procedure<a name="section48346204102418"></a>

1.  On the MRS cluster details page, click  **Services**.
2.  Click the name of the database user service to be modified.
3.  Determine the component database user whose password is to be changed.

    -   To change the password for the DBService database user, go to  [4](#li30220842102536).
    -   To change the password for the Hive, Hue or Loader database user, you must stop the service first, and go to [4](#li30220842102536).

    Click  **Stop Service**  to stop the service.

4.  <a name="li30220842102536"></a>Choose  **More**  \>  **Change Password**.
5.  In the displayed window, enter the old and new passwords as prompted.

    The password complexity requirements are as follows:

    -   The password for a DBService database user must contain 16 to 32 characters; the password for a Hive, Hue or Loader database user must contain 8 to 32 characters.
    -   The password must contain at least three types of the following: lowercase letters, uppercase letters, digits, and special characters which can only be \~\`!@\#$%^&\*\(\)-+\_=\\|\[\{\}\];:",<.\>/?
    -   The password cannot be the same as the username or reverse username.
    -   The password cannot be the same as the last 20 historical passwords.

6.  Click  **OK**. The system automatically restarts the service. After **Operation succeeded** is displayed, click **Finish**.

