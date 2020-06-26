# Changing the Password for the Data Access User of the OMS Database<a name="EN-US_TOPIC_0221415061"></a>

## Scenario<a name="section623381471013"></a>

Periodically change the password for the OMS data access user to ensure the system O&M security.

## Impact on the System<a name="section5745835010120"></a>

The OMS service needs to be restarted for the new password to take effect. The service is unavailable during the restart.

## Procedure<a name="section2407101410135"></a>

1.  On MRS Manager, click  **System**.
2.  In the  **Permission** area, click **Change OMS Database Password**.
3.  Locate the row that contains user  **omm** and click **Change password** in **Operation**  to change the password for the OMS database user.

    The password complexity requirements are as follows:

    -   The password must contain 8 to 32 characters.
    -   The password must contain at least three types of the following: lowercase letters, uppercase letters, digits, and special characters which can only be \~\`!@\#$%^&\*\(\)-+\_=\\|\[\{\}\];:",<.\>/?
    -   The password cannot be the same as the username or reverse username.
    -   The password cannot be the same as the last 20 historical passwords.

4.  Click  **OK**. After **Operation succeeded** is displayed, click **Finish**.
5.  Locate the row that contains user  **omm** and click **Restart the OMS service** in **Operation**  to restart the OMS database.

    >![](/images/icon-note.gif) **NOTE:**   
    >If you do not restart the OMS database after changing the password, the status of user  **omm** changes to **Waiting to restart**. In this state, you cannot change its password again until the OMS database is restarted.  

6.  In the dialog box that is displayed, select  **I have read the information and understand the impact**, click **OK**, and then restart the OMS service.

