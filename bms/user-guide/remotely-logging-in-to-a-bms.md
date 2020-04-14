# Remotely Logging In to a BMS<a name="EN-US_TOPIC_0075481007"></a>

## Scenarios<a name="section192043306319"></a>

If common remote connection software \(such as PuTTY\) is unavailable, you can use the remote login function on the management console to log in to a BMS.

## Constraints<a name="section4546057154615"></a>

-   Only Linux BMSs support remote login.
-   Only the user who creates a BMS or users with the Tenant Administrator or Server Administrator role can log in to the BMS remotely.
-   The remote login page does not support Chinese input or desktop GUI-based operations.
-   When you log in to a BMS remotely, shortcut keys such as Ctrl and Alt are not well supported. For example, if you enter  **Alt + **_ASCII code_, multiple special characters are displayed.
-   Before exiting the management console, log out of the OS.

## Prerequisites<a name="section201143143517"></a>

-   The BMS must be in  **Running**  state.
-   If you selected the key pair login mode when creating the BMS, log in to the BMS by following the instructions in  [SSH Key Pair](logging-in-to-a-bms-using-an-ssh-key-pair.md)  and set a password for the BMS. The detailed operations are as follows:

    Log in to the BMS using the key pair, switch to user  **root**, and run the  **passwd**  command to set a password for user  **root**.

    **Figure  1**  Setting a password for user  **root**<a name="fig12841654173518"></a>  
    ![](figures/setting-a-password-for-user-root.png "setting-a-password-for-user-root")


## Procedure<a name="section157410149552"></a>

1.  Log in to the management console.
2.  Under  **Computing**, click  **Bare Metal Server**.

    The BMS console is displayed.

3.  Locate the row that contains the target BMS and click  **Remote Login**  in the  **Operation**  column.

    After about one minute, the login page is displayed. Press  **Enter**  and enter username  **root**  and password to log in.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   If you do not log in within 10 minutes after obtaining the remote login link, it will become invalid.  
    >-   If you do not perform any operation on the remote login page within 10 minutes, you need to obtain the link again.  
    >-   If the login page does not respond after you press  **Enter**, a possible cause is that remote login is not configured for the BMS image. You can resolve the issue by following the instructions in  [What Can I Do If the Login Page Does Not Respond?](what-can-i-do-if-the-login-page-does-not-respond.md)  
    >-   If the BMS console is displayed improperly \(such as broken lines and garbled characters\) after you remotely log in to it, see  [What Can I Do If the BMS Console Is Displayed Improperly After I Remotely Log In to a BMS?](what-can-i-do-if-the-bms-console-is-displayed-improperly-after-i-remotely-log-in-to-a-bms.md)  


